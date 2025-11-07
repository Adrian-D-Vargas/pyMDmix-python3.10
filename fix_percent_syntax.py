#!/usr/bin/env python3
"""
Script para corregir errores de sintaxis de % malformados en SettingsParser.py
"""

import re

def fix_percent_syntax():
    """Corregir sintaxis de % malformada"""
    
    file_path = "/home/sauron/Dropbox/home/proyectos/pyMDmix-python3.10/pyMDMix/SettingsParser.py"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Patrón para encontrar y corregir líneas con % malformado
    patterns = [
        # Patrón: 'texto' % \) -> 'texto' % (args))
        (r"% \\\)\s*\n\s*(.+)", r"% (\1))"),
        
        # Patrón: 'texto' % \ seguido de argumentos en la siguiente línea
        (r"% \\\s*\n\s*(.+)", r"% (\1)"),
        
        # Patrón más específico para el caso actual
        (r"raise.*'.*' % \\\)\s*\n\s*(.+)", lambda m: m.group(0).replace('% \\)', '% (').replace('\n', '') + ')'),
    ]
    
    for pattern, replacement in patterns:
        if callable(replacement):
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        else:
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    
    # Correcciones específicas
    specific_fixes = [
        # Línea 307 y similares
        ("raise InvalidFile('Error parsing settings file %s: ' % \\)", 
         "raise InvalidFile('Error parsing settings file %s: ' %"),
    ]
    
    for old, new in specific_fixes:
        if old in content:
            content = content.replace(old, new)
            print(f"Corregido: {old}")
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ SettingsParser.py corregido")
        return True
    else:
        print("No se encontraron errores para corregir")
        return False

if __name__ == "__main__":
    fix_percent_syntax()