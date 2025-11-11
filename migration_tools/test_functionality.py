#!/usr/bin/env python3
"""
Ejemplo de uso básico de pyMDMix Python 3.10

Este script demuestra:
1. Importación correcta de pyMDMix
2. Configuración básica
3. Creación de un proyecto simple
"""

import os
import sys

def test_basic_functionality():
    """Probar funcionalidad básica"""
    
    print("🧪 Probando funcionalidad básica de pyMDMix...")
    
    try:
        # Importar pyMDMix
        import pyMDMix
        print("✅ pyMDMix importado correctamente")
        
        # Verificar configuración
        import pyMDMix.settings as S
        print(f"✅ Directorio de datos: {S.DATAROOT}")
        print(f"✅ Directorio de plantillas: {S.TEMPLATE_DIR}")
        
        # Verificar herramientas
        import pyMDMix.tools as T
        print(f"✅ Directorio del proyecto: {T.projectRoot()}")
        
        # Listar solventes disponibles
        from pyMDMix.Solvents import SolventManager
        sm = SolventManager()
        solvents = sm.availableSolvents()
        print(f"✅ Solventes disponibles: {len(solvents)}")
        for solv in solvents[:3]:  # Mostrar primeros 3
            print(f"   - {solv}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def example_project_creation():
    """Ejemplo de creación de proyecto"""
    
    print("\n🏗️  Ejemplo de creación de proyecto...")
    
    try:
        # Esto es un ejemplo - no ejecutar sin archivos PDB reales
        print("📝 Para crear un proyecto:")
        print("   1. Preparar archivo PDB de la proteína")
        print("   2. Configurar archivo de sistema (.cfg)")
        print("   3. Ejecutar: python3 -m pyMDMix create <config_file>")
        
        print("\n💡 Consulta la documentación para ejemplos completos")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 pyMDMix Python 3.10 - Prueba de funcionalidad")
    print("=" * 50)
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists("pyMDMix"):
        print("❌ Error: Ejecutar desde el directorio raíz del proyecto")
        sys.exit(1)
    
    # Probar funcionalidad
    if test_basic_functionality():
        example_project_creation()
        print("\n🎉 Todas las pruebas completadas exitosamente")
    else:
        print("\n❌ Algunas pruebas fallaron")
        sys.exit(1)
