#!/bin/bash
# Script para construir y probar la imagen Docker de pyMDMix

set -e

echo "======================================================================"
echo "  pyMDMix Docker Build Script"
echo "======================================================================"
echo ""

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar que Docker está instalado
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Error: Docker no está instalado${NC}"
    echo "Por favor instala Docker desde: https://docs.docker.com/get-docker/"
    exit 1
fi

echo -e "${GREEN}✓${NC} Docker encontrado: $(docker --version)"
echo ""

# Nombre de la imagen
IMAGE_NAME="pymdmix:python3.10"

# Construir la imagen
echo "======================================================================"
echo "  Construyendo imagen Docker..."
echo "======================================================================"
echo ""
docker build -t $IMAGE_NAME .

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Imagen construida exitosamente: $IMAGE_NAME${NC}"
    echo ""
else
    echo ""
    echo -e "${RED}❌ Error al construir la imagen${NC}"
    exit 1
fi

# Probar la imagen
echo "======================================================================"
echo "  Probando la imagen Docker..."
echo "======================================================================"
echo ""
docker run --rm $IMAGE_NAME

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Imagen validada exitosamente${NC}"
    echo ""
else
    echo ""
    echo -e "${YELLOW}⚠️  Imagen construida pero la validación tuvo problemas${NC}"
    echo ""
fi

# Mostrar información de la imagen
echo "======================================================================"
echo "  Información de la imagen"
echo "======================================================================"
docker images $IMAGE_NAME

echo ""
echo "======================================================================"
echo "  Uso rápido:"
echo "======================================================================"
echo ""
echo "  # Ejecutar sesión interactiva:"
echo "  docker run -it -v \$PWD:/data $IMAGE_NAME /bin/bash"
echo ""
echo "  # O usar docker-compose:"
echo "  docker-compose up -d"
echo "  docker-compose exec pymdmix /bin/bash"
echo ""
echo "======================================================================"
