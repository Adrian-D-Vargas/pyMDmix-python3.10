#!/usr/bin/env python3
"""
Script para corregir problemas de indentación mixta en todos los archivos Python
"""

import os
import glob

def fix_all_indentation():
    """Corregir indentación mixta en todos los archivos .py"""
    
    project_dir = "/home/sauron/Dropbox/home/proyectos/pyMDmix-python3.10"
    
    # Encontrar todos los archivos .py en pyMDMix
    pattern = os.path.join(project_dir, "pyMDMix", "**", "*.py")
    files = glob.glob(pattern, recursive=True)
    
    modified_files = []
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Reemplazar tabs por espacios (4 espacios por tab)
            content = content.expandtabs(4)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_files.append(file_path)
                print(f"✅ Corregido: {os.path.relpath(file_path, project_dir)}")
        
        except Exception as e:
            print(f"❌ Error procesando {file_path}: {e}")
    
    print(f"\n✅ {len(modified_files)} archivos corregidos")
    return modified_files

if __name__ == "__main__":
    print("🔧 Corrigiendo indentación en todos los archivos Python...")
    fix_all_indentation()
    print("✅ Proceso completado")