#!/usr/bin/env python3
"""
Script de configuración del entorno productivo para pyMDMix Python 3.10

Este script:
1. Verifica las dependencias instaladas
2. Configura variables de entorno necesarias
3. Valida la instalación completa
4. Proporciona guía de configuración
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path

class EnvironmentSetup:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.success = []
        
    def check_python_version(self):
        """Verificar versión de Python"""
        print("🔍 Verificando versión de Python...")
        version = sys.version_info
        
        if version.major == 3 and version.minor >= 8:
            self.success.append(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
            return True
        else:
            self.errors.append(f"❌ Python {version.major}.{version.minor} - Se requiere Python 3.8+")
            return False
    
    def check_dependencies(self):
        """Verificar dependencias de Python"""
        print("\n🔍 Verificando dependencias de Python...")
        
        required_packages = {
            'numpy': '1.21.0',
            'scipy': '1.7.0', 
            'matplotlib': '3.5.0',
            'netCDF4': '1.6.0',
            'biopython': '1.79',
            'griddataformats': '1.0.0'
        }
        
        optional_packages = {
            'mechanize': 'Para funcionalidad PDB2PQR',
            'openmm': 'Para simulaciones OpenMM',
            'mdtraj': 'Para análisis de trayectorias'
        }
        
        for package, min_version in required_packages.items():
            try:
                module = importlib.import_module(package.replace('-', '_'))
                version = getattr(module, '__version__', 'desconocida')
                self.success.append(f"✅ {package} {version}")
            except ImportError:
                self.errors.append(f"❌ {package} >= {min_version} - NO INSTALADO")
        
        print("\n📦 Paquetes opcionales:")
        for package, description in optional_packages.items():
            try:
                importlib.import_module(package)
                print(f"✅ {package} - {description}")
            except ImportError:
                print(f"⚠️  {package} - {description} (no instalado)")
    
    def check_environment_variables(self):
        """Verificar variables de entorno"""
        print("\n🔍 Verificando variables de entorno...")
        
        required_vars = {
            'AMBERHOME': 'Ruta de instalación de AMBER',
        }
        
        optional_vars = {
            'NAMD_EXE': 'Ejecutable de NAMD',
            'VMD_EXE': 'Ejecutable de VMD',
            'OPENMM_PLUGIN_DIR': 'Directorio de plugins OpenMM'
        }
        
        for var, description in required_vars.items():
            value = os.environ.get(var)
            if value and os.path.exists(value):
                self.success.append(f"✅ {var}={value}")
            elif value:
                self.warnings.append(f"⚠️  {var}={value} - Ruta no existe")
            else:
                self.errors.append(f"❌ {var} - No definida ({description})")
        
        print("\n🔧 Variables opcionales:")
        for var, description in optional_vars.items():
            value = os.environ.get(var)
            if value:
                print(f"✅ {var}={value}")
            else:
                print(f"⚠️  {var} - No definida ({description})")
    
    def test_pymdmix_import(self):
        """Probar importación de pyMDMix"""
        print("\n🔍 Probando importación de pyMDMix...")
        
        try:
            # Cambiar al directorio del proyecto
            project_dir = Path(__file__).parent
            original_cwd = os.getcwd()
            os.chdir(project_dir)
            
            # Intentar importar
            import pyMDMix
            self.success.append("✅ pyMDMix se importa correctamente")
            
            # Verificar módulos principales
            modules_to_test = [
                'pyMDMix.settings',
                'pyMDMix.tools', 
                'pyMDMix.Systems',
                'pyMDMix.Replicas',
                'pyMDMix.Projects'
            ]
            
            for module_name in modules_to_test:
                try:
                    importlib.import_module(module_name)
                    print(f"  ✅ {module_name}")
                except Exception as e:
                    print(f"  ❌ {module_name}: {e}")
                    
            os.chdir(original_cwd)
            return True
            
        except Exception as e:
            self.errors.append(f"❌ Error importando pyMDMix: {e}")
            if 'original_cwd' in locals():
                os.chdir(original_cwd)
            return False
    
    def create_environment_script(self):
        """Crear script de configuración de entorno"""
        print("\n📝 Creando script de configuración...")
        
        script_content = '''#!/bin/bash
# Script de configuración de entorno para pyMDMix Python 3.10
# Uso: source setup_env.sh

echo "🚀 Configurando entorno pyMDMix..."

# Directorio del proyecto
export PYMDMIX_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$PYMDMIX_ROOT:$PYTHONPATH"

# Variables AMBER (REQUERIDO)
# Descomenta y configura según tu instalación:
# export AMBERHOME="/path/to/amber"
# export PATH="$AMBERHOME/bin:$PATH"

# Variables opcionales para otros programas
# export NAMD_EXE="/path/to/namd2"
# export VMD_EXE="/path/to/vmd"

# Verificar configuración
if [ -z "$AMBERHOME" ]; then
    echo "⚠️  ADVERTENCIA: AMBERHOME no está configurado"
    echo "   Configura en este archivo: export AMBERHOME=/path/to/amber"
fi

# Verificar pyMDMix
cd "$PYMDMIX_ROOT"
if python3 -c "import pyMDMix; print('✅ pyMDMix disponible')" 2>/dev/null; then
    echo "✅ Entorno pyMDMix configurado correctamente"
else
    echo "❌ Error: No se puede importar pyMDMix"
fi

echo "💡 Uso: python3 -m pyMDMix --help"
'''
        
        with open('setup_env.sh', 'w') as f:
            f.write(script_content)
        
        os.chmod('setup_env.sh', 0o755)
        self.success.append("✅ Creado setup_env.sh")
    
    def create_install_dependencies_script(self):
        """Crear script para instalar dependencias"""
        print("\n📝 Creando script de instalación de dependencias...")
        
        script_content = '''#!/bin/bash
# Script de instalación de dependencias para pyMDMix Python 3.10
# Uso: ./install_dependencies.sh

echo "📦 Instalando dependencias de pyMDMix..."

# Verificar pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 no encontrado"
    exit 1
fi

# Instalar dependencias básicas
echo "🔧 Instalando dependencias básicas..."
pip3 install numpy>=1.21.0 scipy>=1.7.0 matplotlib>=3.5.0

# Instalar dependencias científicas
echo "🧬 Instalando dependencias científicas..."
pip3 install netCDF4>=1.6.0 biopython>=1.79 griddataformats>=1.0.0

# Dependencias opcionales
echo "🔧 Instalando dependencias opcionales..."
pip3 install mechanize || echo "⚠️  mechanize no disponible"

# Verificar instalación
echo "✅ Verificando instalación..."
python3 -c "
import sys
modules = ['numpy', 'scipy', 'matplotlib', 'netCDF4', 'Bio', 'griddataformats']
for module in modules:
    try:
        __import__(module)
        print(f'✅ {module}')
    except ImportError:
        print(f'❌ {module} - Error de importación')
        sys.exit(1)
print('🎉 Todas las dependencias instaladas correctamente')
"

echo "✅ Instalación completada"
echo "💡 Siguiente paso: configurar variables de entorno con source setup_env.sh"
'''
        
        with open('install_dependencies.sh', 'w') as f:
            f.write(script_content)
        
        os.chmod('install_dependencies.sh', 0o755)
        self.success.append("✅ Creado install_dependencies.sh")
    
    def create_example_usage(self):
        """Crear ejemplos de uso"""
        print("\n📝 Creando ejemplos de uso...")
        
        example_content = '''#!/usr/bin/env python3
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
    
    print("\\n🏗️  Ejemplo de creación de proyecto...")
    
    try:
        # Esto es un ejemplo - no ejecutar sin archivos PDB reales
        print("📝 Para crear un proyecto:")
        print("   1. Preparar archivo PDB de la proteína")
        print("   2. Configurar archivo de sistema (.cfg)")
        print("   3. Ejecutar: python3 -m pyMDMix create <config_file>")
        
        print("\\n💡 Consulta la documentación para ejemplos completos")
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
        print("\\n🎉 Todas las pruebas completadas exitosamente")
    else:
        print("\\n❌ Algunas pruebas fallaron")
        sys.exit(1)
'''
        
        with open('test_functionality.py', 'w') as f:
            f.write(example_content)
        
        os.chmod('test_functionality.py', 0o755)
        self.success.append("✅ Creado test_functionality.py")
    
    def generate_report(self):
        """Generar reporte final"""
        print("\n" + "="*60)
        print("📋 REPORTE DE CONFIGURACIÓN DEL ENTORNO")
        print("="*60)
        
        if self.success:
            print("\n✅ ÉXITOS:")
            for item in self.success:
                print(f"  {item}")
        
        if self.warnings:
            print("\n⚠️  ADVERTENCIAS:")
            for item in self.warnings:
                print(f"  {item}")
        
        if self.errors:
            print("\n❌ ERRORES A CORREGIR:")
            for item in self.errors:
                print(f"  {item}")
            print("\n🔧 ACCIONES REQUERIDAS:")
            print("  1. Instalar dependencias faltantes: ./install_dependencies.sh")
            print("  2. Configurar variables de entorno: editar setup_env.sh")
            print("  3. Cargar configuración: source setup_env.sh")
        else:
            print("\n🎉 ¡ENTORNO CONFIGURADO CORRECTAMENTE!")
            print("💡 Uso: source setup_env.sh && python3 test_functionality.py")

def main():
    """Función principal"""
    setup = EnvironmentSetup()
    
    print("🚀 CONFIGURACIÓN DEL ENTORNO PYMDMIX PYTHON 3.10")
    print("="*55)
    
    # Ejecutar verificaciones
    setup.check_python_version()
    setup.check_dependencies()
    setup.check_environment_variables()
    setup.test_pymdmix_import()
    
    # Crear archivos de configuración
    setup.create_environment_script()
    setup.create_install_dependencies_script() 
    setup.create_example_usage()
    
    # Reporte final
    setup.generate_report()

if __name__ == "__main__":
    main()