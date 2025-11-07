#!/usr/bin/env python3
"""
Script para corregir problemas de indentación mixta (tabs/espacios) en test.py
"""

import re

def fix_indentation():
    """Corregir indentación mixta en test.py"""
    
    file_path = "/home/sauron/Dropbox/home/proyectos/pyMDmix-python3.10/pyMDMix/test.py"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reemplazar tabs por espacios (4 espacios por tab)
    content = content.expandtabs(4)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Indentación corregida en test.py")

if __name__ == "__main__":
    fix_indentation()