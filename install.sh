#!/bin/bash
# Script mejorado de instalación de pyMDMix
# Maneja problemas de permisos y limpieza de builds anteriores

set -e

echo "======================================================================"
echo "  Instalación de pyMDMix - Python 3.10"
echo "======================================================================"
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# 1. Verificar entorno conda
if [ -z "$CONDA_DEFAULT_ENV" ]; then
    echo -e "${RED}❌ Error: No hay entorno conda activo${NC}"
    echo "Por favor activa tu entorno primero:"
    echo "  conda activate mdmix-env"
    exit 1
fi

echo -e "${GREEN}✓${NC} Entorno conda: $CONDA_DEFAULT_ENV"

# 2. Verificar AMBERHOME
if [ -z "$AMBERHOME" ]; then
    echo -e "${YELLOW}⚠️  AMBERHOME no está configurado${NC}"
    echo "Si tienes AmberTools instalado, configúralo:"
    echo "  export AMBERHOME=/path/to/amber"
    echo ""
    read -p "¿Continuar sin AMBERHOME? (s/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        exit 1
    fi
    # Set dummy AMBERHOME para que setup.py no falle
    export AMBERHOME="${CONDA_PREFIX}"
    echo -e "${YELLOW}Usando AMBERHOME temporal: $AMBERHOME${NC}"
else
    echo -e "${GREEN}✓${NC} AMBERHOME: $AMBERHOME"
fi

echo ""

# 3. Limpiar instalación anterior
echo "Limpiando instalación anterior..."
pip uninstall -y pyMDMix 2>/dev/null || true
echo -e "${GREEN}✓${NC} Desinstalado"

# 4. Limpiar directorios de build
echo "Limpiando directorios de build..."
rm -rf build/ dist/ pyMDMix.egg-info/ 2>/dev/null || true
find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
echo -e "${GREEN}✓${NC} Limpieza completa"

echo ""

# 5. Instalar en modo desarrollo (más seguro)
echo "======================================================================"
echo "Instalando pyMDMix en modo desarrollo..."
echo "======================================================================"
echo ""

pip install -e . --no-build-isolation

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ pyMDMix instalado exitosamente${NC}"
else
    echo ""
    echo -e "${RED}❌ Error durante la instalación${NC}"
    echo ""
    echo "Prueba instalación sin dependencias de build:"
    echo "  pip install -e . --no-build-isolation --no-deps"
    exit 1
fi

echo ""

# 6. Validar instalación
echo "======================================================================"
echo "Validando instalación..."
echo "======================================================================"
echo ""

python -c "import pyMDMix; print('✅ pyMDMix importado correctamente')" || {
    echo -e "${RED}❌ Error: pyMDMix no se puede importar${NC}"
    exit 1
}

# 7. Probar comando mdmix
echo ""
echo "Probando comando 'mdmix'..."
if command -v mdmix &> /dev/null; then
    mdmix -h | head -15
    echo ""
    echo -e "${GREEN}✅ Comando 'mdmix' funciona correctamente${NC}"
else
    echo -e "${YELLOW}⚠️  Comando 'mdmix' no encontrado en PATH${NC}"
    echo "Puedes usar: python -m pyMDMix"
fi

echo ""
echo "======================================================================"
echo -e "${GREEN}✅ INSTALACIÓN COMPLETADA${NC}"
echo "======================================================================"
echo ""
echo "Comandos disponibles:"
echo "  mdmix -h              # Ayuda del comando principal"
echo "  python -m pyMDMix     # Ejecutar como módulo"
echo "  python validate_installation.py  # Validación completa"
echo ""
