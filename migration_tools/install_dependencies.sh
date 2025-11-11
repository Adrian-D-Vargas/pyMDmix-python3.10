#!/bin/bash
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
