#!/usr/bin/env python3
"""
Script para corregir imports malformados del tipo "from Module from . import Class"
"""

import os
import re

def fix_malformed_imports():
    """Corregir imports malformados"""
    
    project_root = "/home/sauron/Dropbox/home/proyectos/pyMDmix-python3.10"
    pymdmix_dir = os.path.join(project_root, "pyMDMix")
    
    # Patrón para detectar imports malformados: "from Module from . import Class"
    pattern = r'from (\w+) from \. import (\w+)'
    
    # Archivos a procesar
    files_to_process = []
    
    for root, dirs, files in os.walk(pymdmix_dir):
        for file in files:
            if file.endswith('.py'):
                files_to_process.append(os.path.join(root, file))
    
    modified_files = []
    
    for file_path in files_to_process:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Corregir imports malformados
            def replace_import(match):
                module = match.group(1)
                class_name = match.group(2)
                return f'from .{module} import {class_name}'
            
            content = re.sub(pattern, replace_import, content)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_files.append(file_path)
                print(f"Corregido: {os.path.relpath(file_path, project_root)}")
        
        except Exception as e:
            print(f"Error procesando {file_path}: {e}")
    
    print(f"\nArchivos modificados: {len(modified_files)}")
    return modified_files

if __name__ == "__main__":
    fix_malformed_imports()