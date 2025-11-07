#!/bin/bash
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
