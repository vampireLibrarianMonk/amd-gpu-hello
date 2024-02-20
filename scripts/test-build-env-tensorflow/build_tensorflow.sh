#!/bin/bash

# First argument: ROCm version to install
ROCM_VERSION=$1

# Stop the script if any command fails
set -e

# Ensure running as root or provide instructions to run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or use sudo."
    exit 1
fi

# Update and install necessary packages
echo "Updating system packages and installing dependencies..."
sudo apt-get update
sudo apt-get install -y patchelf curl openjdk-8-jdk openjdk-8-jre python3.10-venv python3-pip unzip wget git libstdc++-12-dev

# Create a Python virtual environment and activate it
echo "Setting up Python 3.10 virtual environment..."
python3.10 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip

# Install LLVM version 17
echo "Installing LLVM version 17..."
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
sudo ./llvm.sh 17

# Define working directory and Python paths
WORKDIR=$(pwd)
PYTHON_BIN_PATH="${WORKDIR}/venv/bin/python3"
PYTHON_LIB_PATH="${WORKDIR}/venv/lib/python3.10/site-packages"

# Setup ROCM specific environment variables
export ROCM_PATH=/opt/rocm-${ROCM_VERSION}
export TF_NEED_ROCM=1
export GPU_DEVICE_TARGETS=gfx1100

# Clone TensorFlow ROCM enhanced version if it doesn't already exist
if [ ! -d "tensorflow-upstream" ]; then
    echo "Cloning TensorFlow ROCM enhanced repository..."
    git clone --recursive https://github.com/ROCmSoftwarePlatform/tensorflow-upstream
else
    echo "TensorFlow ROCM enhanced repository already exists. Skipping clone..."
fi

cd tensorflow-upstream

# Checkout the version known to work with the specified GPU
echo "Checking out r2.15-rocm-enhanced branch..."
git checkout r2.15-rocm-enhanced

# Install Bazelisk as Bazel in the virtual environment
echo "Installing Bazelisk as Bazel..."
mkdir -p "${WORKDIR}/venv/bin/"
curl -L https://github.com/bazelbuild/bazelisk/releases/download/v1.19.0/bazelisk-linux-amd64 -o "${WORKDIR}/venv/bin/bazel"
chmod +x "${WORKDIR}/venv/bin/bazel"
export PATH="${PATH}:${WORKDIR}/venv/bin/"

# Clean any previous Bazel builds
echo "Cleaning previous builds..."
"${WORKDIR}/venv/bin/bazel" clean --expunge

# Declare build targets and set ROCM version info
echo "Setting up ROCM build targets..."
echo "${GPU_DEVICE_TARGETS}" | sudo tee -a "${ROCM_PATH}/bin/target.lst"
sudo touch "${ROCM_PATH}/.info/version"

# Install necessary Python packages for building TensorFlow
echo "Installing Python packages required for building TensorFlow..."
pip install setuptools wheel numpy packaging requests

# Build TensorFlow for ROCM
echo "Building TensorFlow for ROCM..."
bash build_rocm_python3

echo "TensorFlow ROCM setup complete."
cd ..