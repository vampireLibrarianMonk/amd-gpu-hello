#!/bin/sh

# First argument: ROCm version to install
ROCM_VERSION=$1

# Exit immediately if a command exits with a non-zero status, and print commands and their arguments as they are executed.
set -ex

# Create a Python virtual environment named 'venv'.
python3 -m venv venv

# Activate the virtual environment.
source venv/bin/activate

# Set environment variables for the build process.
export USE_CUDA=0  # Disable CUDA support.
export ROCM_PATH=/opt/rocm-${ROCM_VERSION}  # Set the ROCm installation path.
export PYTORCH_ROCM_ARCH=gfx1100  # Define the ROCm architecture to use.

# Check if the 'pytorch' directory exists to avoid re-cloning.
if [ -d "pytorch" ]; then
    echo "pytorch folder exists. Skipping git clone."
else
    # Clone the PyTorch repository recursively, including submodules.
    git clone --recursive https://github.com/pytorch/pytorch.git
fi

# Change directory to 'pytorch'.
cd pytorch

# Install CMake and Ninja build system, required for building PyTorch.
pip install cmake ninja

# Install Python dependencies listed in the PyTorch requirements file.
pip install -r requirements.txt

# Install Intel MKL and headers for optimized mathematical operations.
pip install mkl mkl-include

# Run AMD build script to prepare for ROCm build.
python3 tools/amd_build/build_amd.py

# Optionally apply a patch to the PyTorch source code.
# git apply ../patches/torch.diff

# Build PyTorch and create a wheel package for easy installation.
python setup.py bdist_wheel

# Go back to the parent directory.
cd ..

# Install the built PyTorch wheel package, upgrading any existing installation.
pip install -U pytorch/dist/*.whl
