#!/usr/bin/env python3
"""
Script para convertir imports absolutos a imports relativos en el paquete pyMDMix
"""
import os
import re
from pathlib import Path

# Lista de módulos internos que deben ser imports relativos
INTERNAL_MODULES = [
    'Browser', 'tools', 'settings', 'SettingsParser', 'Projects', 'Replicas', 
    'MDSettings', 'Systems', 'Solvents', 'GridsManager', 'PDB', 'Analysis', 
    'Energy', 'Amber', 'NAMD', 'OpenMM', 'containers', 'HotSpotsManager',
    'Executor', 'Trajectory', 'QueueWriting', 'Plotter', 'GridData', 'AutoPrepare',
    'Align', 'OFFManager', 'NamdDCDParser', 'Structures'
]

def fix_imports_in_file(filepath):
    """Fix imports in a single file"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content
    
    # Solo procesar archivos dentro del directorio pyMDMix
    if 'pyMDMix' not in str(filepath):
        print(f"  - Skipping (not in pyMDMix): {filepath}")
        return False
        
    # No procesar __init__.py ya que ya lo arreglamos
    if filepath.endswith('__init__.py'):
        print(f"  - Skipping __init__.py: {filepath}")
        return False
    
    # Convertir imports de módulos internos
    for module in INTERNAL_MODULES:
        # import module as alias -> from . import module as alias
        pattern = f'\\bimport {module}(\\s+as\\s+\\w+)?'
        replacement = f'from . import {module}\\1'
        content = re.sub(pattern, replacement, content)
        
        # from module import ... -> from .module import ...
        pattern = f'\\bfrom {module} import'
        replacement = f'from .{module} import'
        content = re.sub(pattern, replacement, content)
    
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
    base_dir = Path(__file__).parent / 'pyMDMix'
    
    # Find all Python files in pyMDMix directory
    py_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip __pycache__ and other directories
        if '__pycache__' in root:
            continue
        
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    
    print(f"\nFixing imports in {len(py_files)} Python files in pyMDMix\n")
    
    updated = 0
    for filepath in sorted(py_files):
        if fix_imports_in_file(filepath):
            updated += 1
    
    print(f"\n{'='*60}")
    print(f"Import fixes complete!")
    print(f"Updated {updated} out of {len(py_files)} files")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()