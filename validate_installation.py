#!/usr/bin/env python3
"""
Script de validación rápida de pyMDMix
Ejecutar después de la instalación para verificar que todo funciona correctamente.
"""

import sys

print("="*60)
print("VALIDACIÓN RÁPIDA DE PYMDMIX")
print("="*60)

# Test 1: Import básico
print("\n✓ Probando import de pyMDMix...")
try:
    import pyMDMix
    print(f"  ✅ pyMDMix v{pyMDMix.__version__ if hasattr(pyMDMix, '__version__') else 'importado correctamente'}")
except ImportError as e:
    print(f"  ❌ Error: {e}")
    print("\n💡 Asegúrate de haber instalado pyMDMix correctamente:")
    print("   python -m pip install -e .")
    sys.exit(1)

# Test 2: Módulos principales
print("\n✓ Verificando módulos principales...")
modules = ['Solvents', 'Systems', 'Replicas', 'Projects', 'Analysis']
for mod in modules:
    try:
        __import__(f'pyMDMix.{mod}')
        print(f"  ✅ pyMDMix.{mod}")
    except Exception as e:
        print(f"  ❌ pyMDMix.{mod}: {e}")

# Test 3: Dependencias
print("\n✓ Verificando dependencias científicas...")
deps = ['numpy', 'scipy', 'matplotlib', 'netCDF4', 'Bio']
for dep in deps:
    try:
        __import__(dep)
        print(f"  ✅ {dep}")
    except ImportError:
        print(f"  ⚠️  {dep} no encontrado (puede ser opcional)")

print("\n" + "="*60)
print("✅ VALIDACIÓN COMPLETADA")
print("="*60)
print("\nPara más información, consulta la documentación en:")
print("http://mdmix.sourceforge.net")
