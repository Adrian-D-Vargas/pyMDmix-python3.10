#!/usr/bin/env python3
"""
Script para reemplazar imports de Biskit con módulo de compatibilidad
"""

import os
import re
import sys

def replace_biskit_imports():
    """Reemplazar imports de Biskit con módulo de compatibilidad"""
    
    # Directorio del proyecto
    project_root = "/home/sauron/Dropbox/home/proyectos/pyMDmix-python3.10"
    pymdmix_dir = os.path.join(project_root, "pyMDMix")
    
    # Patrones de reemplazo
    replacements = [
        # Biskit.test imports
        (r'import Biskit\.test as BT', 'from . import biskit_compat as BT'),
        (r'from Biskit\.test import \*', 'from .biskit_compat import BiskitTest, localTest, FUTURE'),
        (r'BT\.BiskitTest', 'BT.BiskitTest'),
        (r'BT\.localTest', 'BT.localTest'),
        (r'BT\.FUTURE', 'BT.FUTURE'),
        
        # Biskit as bi imports
        (r'import Biskit as bi', 'from . import biskit_compat as bi'),
        (r'bi\.PDBModel', 'bi.PDBModel'),
        (r'bi\.AmberCrdParser', 'bi.AmberCrdParser'),
        (r'bi\.AmberParmBuilder', 'bi.AmberParmBuilder'),
        
        # Biskit.tools imports en NamdDCDParser
        (r'import Biskit\.tools as T', 'from . import tools as T'),
        (r'from Biskit\.PDBModel import PDBModel', 'from .biskit_compat import PDBModel'),
        (r'from Biskit\.LogFile import StdLog', 'from .biskit_compat import StdLog'),
    ]
    
    # Archivos a procesar
    files_to_process = []
    
    # Encontrar todos los archivos .py en pyMDMix
    for root, dirs, files in os.walk(pymdmix_dir):
        for file in files:
            if file.endswith('.py') and file != 'biskit_compat.py':
                files_to_process.append(os.path.join(root, file))
    
    modified_files = []
    
    for file_path in files_to_process:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Aplicar reemplazos
            for pattern, replacement in replacements:
                content = re.sub(pattern, replacement, content)
            
            # Si hubo cambios, escribir el archivo
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_files.append(file_path)
                print(f"Modificado: {file_path}")
        
        except Exception as e:
            print(f"Error procesando {file_path}: {e}")
    
    print(f"\nArchivos modificados: {len(modified_files)}")
    for file in modified_files:
        print(f"  - {os.path.relpath(file, project_root)}")
    
    return modified_files

if __name__ == "__main__":
    modified_files = replace_biskit_imports()
    print(f"\n✓ Proceso completado. {len(modified_files)} archivos modificados.")