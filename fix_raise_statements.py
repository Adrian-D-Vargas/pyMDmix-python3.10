#!/usr/bin/env python3
"""
Script to fix raise statements with string formatting
"""
import os
import re
from pathlib import Path

def fix_raise_statements(filepath):
    """Fix raise statements that have string formatting outside parentheses"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content
    
    # Fix raise statements like: raise Error("message" % args)
    # to: raise Error("message" % args)
    content = re.sub(
        r'raise\s+(\w+)\("([^"]*)"\)\s*%\s*([^\n]+)',
        r'raise \1("\2" % \3)',
        content
    )
    
    # Fix raise statements like: raise Error('message' % args)
    # to: raise Error('message' % args)
    content = re.sub(
        r"raise\s+(\w+)\('([^']*)'\)\s*%\s*([^\n]+)",
        r"raise \1('\2' % \3)",
        content
    )
    
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
    
    print(f"\nFixing raise statements in {len(py_files)} Python files\n")
    
    updated = 0
    for filepath in sorted(py_files):
        if fix_raise_statements(filepath):
            updated += 1
    
    print(f"\n{'='*60}")
    print(f"Raise statement fixes complete!")
    print(f"Updated {updated} out of {len(py_files)} files")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()