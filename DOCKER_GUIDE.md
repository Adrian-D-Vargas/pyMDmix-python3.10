# 🐳 Guía de Docker para pyMDMix

Esta guía explica cómo usar Docker para ejecutar pyMDMix sin necesidad de instalar dependencias localmente.

## 📋 Requisitos Previos

- Docker instalado: https://docs.docker.com/get-docker/
- (Opcional) Docker Compose instalado: https://docs.docker.com/compose/install/

## 🚀 Inicio Rápido

### Opción 1: Usar docker-compose (Más Fácil)

```bash
# 1. Construir y levantar el contenedor
docker-compose up -d

# 2. Entrar al contenedor
docker-compose exec pymdmix /bin/bash

# 3. Dentro del contenedor, probar pyMDMix
python -c "import pyMDMix; print('✅ Funciona!')"

# 4. Cuando termines, detener el contenedor
docker-compose down
```

### Opción 2: Usar Docker directamente

```bash
# 1. Construir la imagen
docker build -t pymdmix:python3.10 .

# 2. Ejecutar validación
docker run --rm pymdmix:python3.10

# 3. Sesión interactiva con acceso a tus archivos
docker run -it -v $PWD:/data pymdmix:python3.10 /bin/bash
```

### Opción 3: Script automatizado

```bash
# Construye y valida automáticamente
bash build_docker.sh
```

## 📖 Casos de Uso Comunes

### 1. Ejecutar un script Python

```bash
# Desde el host, ejecutar un script dentro del contenedor
docker run --rm -v $PWD:/data pymdmix:python3.10 python /data/mi_script.py
```

### 2. Trabajo interactivo con Jupyter

```bash
# Agregar al docker-compose.yml:
ports:
  - "8888:8888"

# Luego:
docker-compose exec pymdmix jupyter notebook --ip=0.0.0.0 --allow-root
```

### 3. Procesamiento de datos

```bash
# Montar directorio con datos
docker run -it -v /path/to/data:/data pymdmix:python3.10 /bin/bash

# Dentro del contenedor
cd /data
python process_mdmix_data.py
```

## 🔧 Personalización del Dockerfile

El Dockerfile actual incluye:
- Python 3.10
- numpy, scipy, matplotlib
- netCDF4, biopython
- griddataformats
- pyMDMix (instalado en modo desarrollo)

Para agregar paquetes adicionales, edita el Dockerfile:

```dockerfile
# Después de la línea de micromamba install, agregar:
RUN micromamba install -y -n base -c conda-forge \
    tu-paquete-adicional \
    && micromamba clean --all --yes
```

## 📊 Especificaciones de la Imagen

| Característica | Detalle |
|---------------|---------|
| Base | mambaorg/micromamba:1.5.8 |
| Python | 3.10 |
| Tamaño estimado | ~800MB |
| Dependencias | Todas incluidas |
| Tiempo de build | ~5-10 minutos |

## 🐛 Solución de Problemas

### Error: "docker: command not found"
Instala Docker desde: https://docs.docker.com/get-docker/

### Error de permisos en Windows/WSL
```bash
# Ejecutar Docker con permisos de usuario
docker run --user $(id -u):$(id -g) ...
```

### Imagen muy grande
El Dockerfile ya está optimizado. Para reducir más:
```bash
# Limpiar imágenes no usadas
docker system prune -a
```

### Problemas con volúmenes en Windows
Usa rutas absolutas:
```bash
docker run -v C:\Users\tu\proyecto:/data pymdmix:python3.10
```

## 📚 Referencias

- [Documentación oficial de Docker](https://docs.docker.com/)
- [Best practices para Dockerfiles](https://docs.docker.com/develop/dev-best-practices/)
- [pyMDMix README principal](../README.md)

## 💡 Tips

1. **Mantén la imagen actualizada**: Reconstruye cuando actualices pyMDMix
   ```bash
   docker-compose build --no-cache
   ```

2. **Comparte la imagen**: Publica en Docker Hub para que otros la usen
   ```bash
   docker tag pymdmix:python3.10 tu-usuario/pymdmix:python3.10
   docker push tu-usuario/pymdmix:python3.10
   ```

3. **Desarrollo activo**: Monta el código fuente para editar en tiempo real
   ```bash
   docker run -it -v $PWD:/opt/pymdmix pymdmix:python3.10 /bin/bash
   ```
