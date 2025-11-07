#!/usr/bin/env python3
"""
Script to migrate Python 2.7 code to Python 3.10
Applies common transformations systematically
"""
import os
import re
import sys
from pathlib import Path

def migrate_file(filepath):
    """Apply Python 3 migrations to a single file"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Fix print(statements - convert print("...") to print("..."))
    # Handle simple print(statements)
    content = re.sub(r'\bprint\s+"([^"]*)"', r'print("\1")', content)
    content = re.sub(r"\bprint\s+'([^']*)'", r"print('\1')", content)
    
    # Handle print(with variables)
    content = re.sub(r'\bprint\s+([^"\'\n][^\n]*?)$', r'print(\1)', content, flags=re.MULTILINE)
    
    # Handle print(>> sys.stderr, "message")
    content = re.sub(r'print\s*>>\s*([^,]+),\s*(.+)', r'print(\2, file=\1)', content)
    
    # 2. Fix except syntax - convert except Error as e: to except Error as e:
    content = re.sub(r'except\s+(\w+(?:\.\w+)?)\s*,\s*(\w+):', r'except \1 as \2:', content)
    
    # 3. Fix raise syntax - convert raise Error("message") to raise Error("message")
    content = re.sub(r'raise\s+(\w+)\s*,\s*"([^"]*)"', r'raise \1("\2")', content)
    content = re.sub(r"raise\s+(\w+)\s*,\s*'([^']*)'", r"raise \1('\2')", content)
    content = re.sub(r'raise\s+(\w+)\s*,\s*([^"\'\n][^\n]*?)(?:\n|$)', r'raise \1(\2)', content)
    
    # 4. Fix dictionary methods - .items() -> .items()
    content = re.sub(r'\.iteritems\(\)', r'.items()', content)
    content = re.sub(r'\.iterkeys\(\)', r'.keys()', content)
    content = re.sub(r'\.itervalues\(\)', r'.values()', content)
    
    # 5. Fix range -> range
    content = re.sub(r'\bxrange\b', r'range', content)
    
    # 6. Fix imports
    # Queue -> queue
    content = re.sub(r'\bimport\s+Queue\b', r'import queue', content)
    content = re.sub(r'\bfrom\s+Queue\s+import', r'from queue import', content)
    
    # ConfigParser -> configparser
    content = re.sub(r'\bimport\s+ConfigParser\b', r'import configparser', content)
    content = re.sub(r'\bfrom\s+ConfigParser\s+import', r'from configparser import', content)
    content = re.sub(r'\bConfigParser\.', r'configparser.', content)
    
    # StringIO
    content = re.sub(r'\bfrom\s+StringIO\s+import\s+StringIO', r'from io import io', content)
    content = re.sub(r'\bimport\s+StringIO', r'import io', content)
    
    # urllib, urllib2 -> urllib.request, urllib.parse
    content = re.sub(r'\bimport\s+urllib2\b', r'import urllib.request', content)
    content = re.sub(r'\burllib2\.', r'urllib.request.', content)
    
    # 7. Fix has_key - x in dict -> x in dict
    content = re.sub(r'(\w+)\.has_key\(([^)]+)\)', r'\2 in \1', content)
    
    # Only write if content changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        print(f"  ✓ Updated: {filepath}")
        return True
    else:
        print(f"  - No changes needed: {filepath}")
        return False

def main():
    """Main migration function"""
    # Get the base directory
    base_dir = Path(__file__).parent
    
    # Find all Python files
    py_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip certain directories
        if any(skip in root for skip in ['.git', '__pycache__', 'build', 'dist', '.egg-info']):
            continue
        
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    
    print(f"\nFound {len(py_files)} Python files to process\n")
    
    updated = 0
    for filepath in sorted(py_files):
        if migrate_file(filepath):
            updated += 1
    
    print(f"\n{'='*60}")
    print(f"Migration complete!")
    print(f"Updated {updated} out of {len(py_files)} files")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
