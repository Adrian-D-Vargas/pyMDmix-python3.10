# pyMDMix Docker Image - Python 3.10
# Based on mambaorg/micromamba for faster package installation
FROM mambaorg/micromamba:1.5.8

# Metadata
LABEL maintainer="pyMDMix Contributors"
LABEL description="pyMDMix - Molecular Dynamics with Mixed Solvents (Python 3.10)"
LABEL version="3.10"

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

USER $MAMBA_USER

# Set working directory
WORKDIR /opt/pymdmix

# Copy project files
COPY --chown=$MAMBA_USER:$MAMBA_USER . /opt/pymdmix/

# Create conda environment with Python 3.10 and dependencies
RUN micromamba install -y -n base -c conda-forge \
    python=3.10 \
    numpy \
    scipy \
    matplotlib \
    netcdf4 \
    biopython \
    pip \
    && micromamba clean --all --yes

# Install griddataformats via pip (not available in conda-forge)
RUN pip install --no-cache-dir griddataformats

# Install pyMDMix in development mode
RUN pip install --no-cache-dir -e .

# Validate installation
RUN python -c "import pyMDMix; print('✅ pyMDMix imported successfully')"

# Set working directory for user data
WORKDIR /data

# Default command: run validation
CMD ["python", "/opt/pymdmix/validate_installation.py"]
