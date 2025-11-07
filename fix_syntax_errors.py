#!/usr/bin/env python3
"""
Script para corregir automáticamente errores comunes de sintaxis Python 2→3
"""
import os
import re
import glob

def fix_imports_in_file(filepath):
    """Corrige imports relativos y absolutos en un archivo"""
    print(f"🔧 Corrigiendo imports en {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='latin-1') as f:
                content = f.read()
        except:
            print(f"❌ No se pudo leer {filepath}")
            return False
    
    original_content = content
    
    # Corregir imports malformados
    content = re.sub(r'from pyMDMix\.(\w+) from \. import', r'from ..\\1 import', content)
    content = re.sub(r'from (\w+) import \*$', r'from .\\1 import *', content, flags=re.MULTILINE)
    
    # Corregir lambda syntax
    content = re.sub(r'lambda \(([^)]+)\):', r'lambda \\1:', content)
    
    # Corregir print statements
    content = re.sub(r'print\s*\(\s*"([^"]*)"?\s*\)\s*,\s*([^,\n]+)', r'print("\\1", \\2)', content)
    content = re.sub(r'print\s+"([^"]*)",\s*([^,\n]+)', r'print("\\1", \\2)', content)
    
    # Escribir solo si hubo cambios
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Corregido {filepath}")
        return True
    return False

def main():
    print("🔧 Iniciando corrección automática de sintaxis...")
    
    # Buscar todos los archivos Python
    python_files = []
    for root, dirs, files in os.walk('pyMDMix'):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    corrected_files = 0
    for filepath in python_files:
        if fix_imports_in_file(filepath):
            corrected_files += 1
    
    print(f"✅ Proceso completado. {corrected_files} archivos corregidos de {len(python_files)} revisados")

if __name__ == "__main__":
    main()