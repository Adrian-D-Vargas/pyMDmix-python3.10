#!/usr/bin/env python3
"""
Script to fix remaining Python 2 to 3 compatibility issues
"""
import os
import re
from pathlib import Path

def fix_imports(filepath):
    """Fix remaining import issues"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content
    
    # Fix cPickle imports
    content = re.sub(r'\bimport cPickle\b', r'import pickle', content)
    content = re.sub(r'\bcPickle\.', r'pickle.', content)
    
    # Fix user import (Python 2 only module)
    content = re.sub(r'\bimport user\b', r'import os', content)
    content = re.sub(r'\buser\.home\b', r'os.path.expanduser("~")', content)
    
    # Fix string join with newlines - common Python 3 issue
    content = re.sub(r"print\('\\n'\)\.join\(", r"print('\\n'.join(", content)
    
    # Fix SafeConfigParser (deprecated in Python 3)
    content = re.sub(r'configparser\.SafeConfigParser', r'configparser.ConfigParser', content)
    
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
    """Main function"""
    base_dir = Path(__file__).parent
    
    # Find all Python files
    py_files = []
    for root, dirs, files in os.walk(base_dir):
        if any(skip in root for skip in ['.git', '__pycache__', 'build', 'dist', '.egg-info']):
            continue
        
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    
    print(f"\nFixing remaining imports in {len(py_files)} Python files\n")
    
    updated = 0
    for filepath in sorted(py_files):
        if fix_imports(filepath):
            updated += 1
    
    print(f"\n{'='*60}")
    print(f"Import fixes complete!")
    print(f"Updated {updated} out of {len(py_files)} files")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()