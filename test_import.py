#!/usr/bin/env python3
"""
Script de prueba para verificar la importación de pyMDMix
"""

def test_import():
    try:
        print("Intentando importar pyMDMix...")
        import pyMDMix
        print("✓ pyMDMix importado exitosamente!")
        
        # Verificar algunos componentes básicos
        print("✓ Módulo pyMDMix cargado")
        
        # Verificar la versión si está disponible
        if hasattr(pyMDMix, '__version__'):
            print(f"✓ Versión: {pyMDMix.__version__}")
        
        # Verificar algunos módulos internos
        modules_to_check = ['settings', 'tools']
        for module_name in modules_to_check:
            if hasattr(pyMDMix, module_name):
                print(f"✓ Módulo {module_name} disponible")
            else:
                print(f"⚠ Módulo {module_name} no disponible")
        
        return True
        
    except Exception as e:
        print(f"✗ Error al importar pyMDMix: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_import()
    if success:
        print("\n🎉 ¡Migración completada exitosamente!")
    else:
        print("\n❌ La migración necesita más trabajo")