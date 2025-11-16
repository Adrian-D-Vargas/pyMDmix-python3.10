# 🚀 Guía Rápida de Instalación - pyMDMix Python 3.10

## Método Recomendado: Script Automatizado

```bash
cd /home/sauron/Dropbox/home/proyectos/pyMDmix-python3.10

# Activar entorno
conda activate mdmix-env

# Ejecutar script de instalación
bash install.sh
```

El script maneja automáticamente:
- ✅ Limpieza de instalaciones previas
- ✅ Limpieza de builds temporales
- ✅ Instalación en modo desarrollo
- ✅ Validación completa
- ✅ Verificación del comando mdmix

## Método Manual (si el script falla)

### Paso 1: Limpiar
```bash
cd /home/sauron/Dropbox/home/proyectos/pyMDmix-python3.10
conda activate mdmix-env

# Desinstalar versión anterior
pip uninstall -y pyMDMix

# Limpiar builds
rm -rf build/ dist/ *.egg-info
find . -name "__pycache__" -type d -exec rm -rf {} +
```

### Paso 2: Configurar AMBERHOME (opcional)
```bash
# Si tienes AmberTools instalado:
export AMBERHOME=/path/to/amber

# O usar el entorno conda como temporal:
export AMBERHOME=$CONDA_PREFIX
```

### Paso 3: Instalar
```bash
# Opción A: Modo desarrollo (recomendado)
pip install -e . --no-build-isolation

# Opción B: Si falla, sin dependencias de build
pip install -e . --no-build-isolation --no-deps
```

### Paso 4: Validar
```bash
# Test básico
python -c "import pyMDMix; print('✅ OK')"

# Validación completa
python validate_installation.py

# Probar comando
mdmix -h
```

## Solución de Problemas

### Error: "Permission denied: ANTWAT20.off"
**Solución:** Usar el script `install.sh` que limpia correctamente los builds.

### Error: "AMBERHOME env variable not set"
**Solución 1:** Instalar AmberTools en el entorno:
```bash
conda install -c conda-forge ambertools
```

**Solución 2:** Configurar temporalmente:
```bash
export AMBERHOME=$CONDA_PREFIX
```

**Solución 3:** Editar `setup.py` y comentar la verificación de AMBERHOME (líneas 15-17).

### Error: "Failed building wheel"
```bash
# Limpiar todo y reinstalar
rm -rf build/ dist/ *.egg-info
pip install -e . --no-build-isolation
```

### Comando 'mdmix' no encontrado
```bash
# El ejecutable debería estar en:
ls $CONDA_PREFIX/bin/mdmix

# Si no existe, usar:
python -m pyMDMix
```

## Verificación Post-Instalación

```bash
# 1. Import funciona
python -c "import pyMDMix"

# 2. Comandos funcionan
python -c "from pyMDMix.Commands import Create, Info"

# 3. Comando mdmix disponible
mdmix -h

# 4. Validación completa
python validate_installation.py
```

## Dependencias Requeridas

El sistema instalará automáticamente:
- numpy
- scipy
- matplotlib
- netCDF4
- biopython

Opcional (para algunas funcionalidades):
- griddataformats (se instala automáticamente)
- ambertools (recomendado para funcionalidad completa)

## Reinstalación Rápida

Si ya instalaste y hay actualizaciones:
```bash
cd /home/sauron/Dropbox/home/proyectos/pyMDmix-python3.10
conda activate mdmix-env
bash reinstall.sh
```

## Notas Importantes

1. **Modo desarrollo (`-e`)**: Los cambios en el código se reflejan inmediatamente sin reinstalar
2. **No build isolation**: Evita problemas con setuptools modernos
3. **AMBERHOME**: No es crítico para import básico, pero necesario para algunas funcionalidades

## Ayuda Adicional

Si los problemas persisten:
```bash
# Ver logs detallados
pip install -e . -v

# O crear issue con el output completo
```
