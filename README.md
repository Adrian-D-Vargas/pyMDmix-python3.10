## pyMDMix --- http://mdmix.sourceforge.net

🎉 **This version has been migrated to Python 3.10!** 🎉

The program is distributed under GNU GPLv3 license. Find the license file
under Licenses/ folder.

## 🐍 Python 3.10 Migration

This repository contains pyMDMix migrated from Python 2.7 to Python 3.10.

**Migration Status**: ✅ **COMPLETED** (Nov 10, 2025)
- All syntax updated to Python 3.10
- All imports modernized
- Biskit dependency replaced with compatibility module
- Full validation passed

See [migration_tools/MIGRATION_SUMMARY.md](migration_tools/MIGRATION_SUMMARY.md) for details.

DOCUMENTATION
=============
All documentation on program usage is online at
http://mdmix.sourceforge.net

INSTALLATION
============

1- Dependencies
---------------
This version of pyMDMix depends on:
  - **Python >= 3.10**
  - ambertools >= 12
  - numpy, scipy, matplotlib
  - netCDF4
  - biopython
  - griddataformats

Make sure ambertools environment variables are set

2 - Installation process
------------------------
it is advised to install pyMDMix in a virtual environment

there are three recommended ways to install pyMDMix:
1. from the repository by
`python -m pip install [insert address here]`

2. from the project's local folder after cloning the repo by
`python -m pip install .`

3. Use conda or mamba: we will first create the correct conda environment which will already contain ambertools. We will then set the AMBERHOME variable within the environment and finally proceed to install pymdmix from the local git cloned files. Make sure `$CONDA_PREFIX` points to the conda installation directory (it may happen when you activate the new environment this varaible is lost, in that case change the variable for the explicit path). 

```bash
git clone https://github.com/CBDD/pyMDmix.git
cd pyMDMix
conda env create -f environment_p27.yml
conda activate mdmix-env
conda env config vars set AMBERHOME=$CONDA_PREFIX/envs/mdmix-env
pip install .
```

3 - Testing & Validation
------------------------

After installation, validate that pyMDMix works correctly:

```bash
# Quick validation
python validate_installation.py

# Or test manually
python -c "import pyMDMix; print('✅ pyMDMix imported successfully')"

# Run the module
python -m pyMDMix
```

For comprehensive testing, see scripts in `migration_tools/` directory.

The main script should have been installed correclty also. check it by running
`mdmix -h`

Test the program works correctly:
	Move again to the package source directory and type:
		> python pyMDMix/test.py all
	This will run a series of source code checks.
	No test should fail.

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


