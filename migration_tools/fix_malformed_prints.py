#!/usr/bin/env python3
"""
Script para corregir print statements malformados por el script anterior
"""
import re
import os

def fix_malformed_prints_in_file(filepath):
    """Corrige prints malformados que quedaron después del script automático"""
    print(f"🔧 Corrigiendo prints malformados en {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        print(f"❌ No se pudo leer {filepath}")
        return False
    
    original_content = content
    
    # Corregir prints malformados tipo print("\1", \2)
    content = re.sub(r'print\("\\1", \\2\)', 'print("")', content)
    content = re.sub(r'print\("\\1", \\2\),([^\\n]*)', r'print("", \\1)', content)
    content = re.sub(r'#print\("\\1", \\2\)([^\\n]*)', r'#print("" \\1)', content)
    
    # Escribir solo si hubo cambios
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Corregido {filepath}")
        return True
    return False

def main():
    print("🔧 Corrigiendo prints malformados...")
    
    files_to_fix = [
        'pyMDMix/GridData.py',
        'pyMDMix/NamdDCDParser.py'
    ]
    
    corrected_files = 0
    for filepath in files_to_fix:
        if os.path.exists(filepath) and fix_malformed_prints_in_file(filepath):
            corrected_files += 1
    
    print(f"✅ Proceso completado. {corrected_files} archivos corregidos")

if __name__ == "__main__":
    main()