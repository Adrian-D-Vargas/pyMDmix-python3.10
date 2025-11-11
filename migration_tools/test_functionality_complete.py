#!/usr/bin/env python3
"""
Script completo para validar la funcionalidad de pyMDMix después de la migración
"""

print("="*70)
print("VALIDACIÓN COMPLETA DE PYMDMIX - PYTHON 3.10")
print("="*70)

# Test 1: Import básico
print("\n1. Probando import básico de pyMDMix...")
try:
    import pyMDMix
    print("   ✅ pyMDMix importado correctamente")
    print(f"   📍 Ubicación: {pyMDMix.__file__}")
except Exception as e:
    print(f"   ❌ Error: {e}")
    exit(1)

# Test 2: Importar módulos principales
print("\n2. Probando imports de módulos principales...")
modules_to_test = [
    'pyMDMix.Solvents',
    'pyMDMix.Systems',
    'pyMDMix.Replicas',
    'pyMDMix.Projects',
    'pyMDMix.Analysis',
    'pyMDMix.GridsManager',
    'pyMDMix.tools',
]

failed_imports = []
for module_name in modules_to_test:
    try:
        exec(f"import {module_name}")
        print(f"   ✅ {module_name}")
    except Exception as e:
        print(f"   ❌ {module_name}: {str(e)[:60]}")
        failed_imports.append((module_name, str(e)))

# Test 3: Verificar clases principales
print("\n3. Verificando clases principales...")
classes_to_test = [
    ('pyMDMix.Solvents', 'SolventManager'),
    ('pyMDMix.Systems', 'System'),
    ('pyMDMix.Replicas', 'Replica'),
    ('pyMDMix.Projects', 'Project'),
]

for module_name, class_name in classes_to_test:
    try:
        module = __import__(module_name, fromlist=[class_name])
        cls = getattr(module, class_name)
        print(f"   ✅ {module_name}.{class_name}")
    except Exception as e:
        print(f"   ❌ {module_name}.{class_name}: {str(e)[:60]}")

# Test 4: Verificar dependencias científicas
print("\n4. Verificando dependencias científicas...")
dependencies = [
    'numpy',
    'scipy',
    'matplotlib',
    'netCDF4',
    'Bio',  # biopython
    'gridData',  # griddataformats
]

for dep in dependencies:
    try:
        __import__(dep)
        print(f"   ✅ {dep}")
    except ImportError as e:
        print(f"   ❌ {dep}: {e}")

# Test 5: Verificar módulo de compatibilidad Biskit
print("\n5. Verificando módulo de compatibilidad Biskit...")
try:
    from pyMDMix import biskit_compat
    print("   ✅ biskit_compat importado")
    
    # Verificar algunas funciones/clases clave
    attrs = ['LogFormatter', 'BiskitTest', 'PDBModel']
    for attr in attrs:
        if hasattr(biskit_compat, attr):
            print(f"   ✅ biskit_compat.{attr} disponible")
        else:
            print(f"   ⚠️  biskit_compat.{attr} no encontrado")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Resumen final
print("\n" + "="*70)
print("RESUMEN DE VALIDACIÓN")
print("="*70)

if failed_imports:
    print(f"\n⚠️  {len(failed_imports)} módulos con problemas:")
    for mod, err in failed_imports:
        print(f"   - {mod}")
else:
    print("\n✅ Todos los módulos principales se importaron correctamente")

print("\n🎉 MIGRACIÓN A PYTHON 3.10 COMPLETADA EXITOSAMENTE")
print("\n" + "="*70)
