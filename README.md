## pyMDMix 

🎉 **This version has been migrated to Python 3.10!** 🎉

The program is distributed under GNU GPLv3 license.

## 🐍 Python 3.10 Migration

This repository contains pyMDMix migrated from Python 2.7 to Python 3.10.

### Migration Details
- **Original Version**: Python 2.7
- **Target Version**: Python 3.10.19
- **Migration Method**: AI-assisted migration using **Claude Sonnet 4.5** (Anthropic)
- **GitHub Copilot**: Used as AI assistant interface in VS Code

### Key Changes
- ✅ All Python 2 syntax updated to Python 3.10
- ✅ Import system modernized (relative imports, importlib)
- ✅ Print statements converted to functions
- ✅ Exception handling syntax updated
- ✅ String formatting modernized
- ✅ Biskit dependency replaced with compatibility module
- ✅ Cross-platform installation support (symlink issues resolved)
- ✅ Module import errors fixed (tools, Actions, Commands)
- ✅ Full validation and testing passed

**Note**: This migration was performed with AI assistance (Claude Sonnet 4.5 via GitHub Copilot) to ensure systematic and comprehensive code modernization while maintaining original functionality.

See [migration_tools/MIGRATION_SUMMARY.md](migration_tools/MIGRATION_SUMMARY.md) for detailed technical documentation.

INSTALLATION
============

1- Dependencies
---------------
This version of pyMDMix depends on:
  - **Python >= 3.10**
  - ambertools
  - numpy, scipy, matplotlib
  - netCDF4
  - biopython
  - griddataformats

Make sure ambertools environment variables are set

2 - Installation process
------------------------
It is advised to install pyMDMix in a virtual environment

Use conda or mamba: we will first create the correct conda environment which will already contain ambertools. We will then set the AMBERHOME variable within the environment and finally proceed to install pymdmix from the local git cloned files. Make sure `$CONDA_PREFIX` points to the conda installation directory (it may happen when you activate the new environment this varaible is lost, in that case change the variable for the explicit path). 

```bash
git clone https://github.com/Adrian-D-Vargas/pyMDmix-python3.10.git
cd pyMDmix-python3.10
mamba env create -f environment_p27.yml
mamba activate mdmix-env
mamba env config vars set AMBERHOME=$CONDA_PREFIX/envs/mdmix-env
pip install .
```

3 - Testing & Validation
------------------------

After installation, validate that pyMDMix works correctly:

```bash
# Quick validation
python validate_installation.py
```

For comprehensive testing, see scripts in `migration_tools/` directory.

The main script should have been installed correclty also. check it by running
`mdmix -h`

4 - Using Docker 🐳
-------------------

### Quick Start with Docker

**Option 1: Using docker-compose (Recommended)**
```bash
# Build and start container
docker-compose up -d

# Enter the container
docker-compose exec pymdmix /bin/bash

# Inside container, validate installation
python validate_installation.py

# Run pyMDMix
python -m pyMDMix
```

**Option 2: Using Docker directly**
```bash
# Build the image
docker build -t pymdmix:python3.10 .

# Run validation
docker run --rm pymdmix:python3.10

# Interactive session with data volume
docker run -it -v $PWD:/data pymdmix:python3.10 /bin/bash
```

**Option 3: Pull pre-built image (if available)**
```bash
docker pull username/pymdmix:python3.10
docker run -it -v $PWD:/data username/pymdmix:python3.10
```

### Docker Image Details
- **Base**: micromamba (fast package manager)
- **Python**: 3.10
- **Includes**: All scientific dependencies (numpy, scipy, matplotlib, netCDF4, biopython, griddataformats)
- **Size**: ~800MB (optimized)

See `Dockerfile` for complete build details.

The docker run command will mount the current working directory (windows users should replace $PWD by %cd%) so the container has access to the current location. Output will be also in the current working directory. 
s

4 - Enjoy!
----------
Read program usage at online documentation.


