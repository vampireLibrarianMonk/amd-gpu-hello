# Radeon Open Compute (ROCm)

ROCm is a robust open-source platform that empowers developers and researchers to harness the computational power of AMD GPUs for a wide range of applications. With its comprehensive set of tools, libraries, and compatibility with popular frameworks, ROCm plays a pivotal role in advancing GPU computing across various domains, including scientific research, machine learning, and high-performance computing. It continues to evolve and expand its capabilities, making it an essential tool for those seeking GPU acceleration on AMD hardware.

Key Components of ROCm:

  * ROCm Runtime: ROCm includes a runtime that provides the necessary low-level GPU support, including hardware abstraction, memory management, and kernel execution. It allows developers to write and execute GPU-accelerated code using a variety of programming languages, including C, C++, and Python.

  * ROCm Math Libraries (RocBLAS, RocFFT, etc.): ROCm provides a suite of math libraries optimized for AMD GPUs. These libraries include linear algebra routines (RocBLAS), Fast Fourier Transform (FFT) operations (RocFFT), and more. They are crucial for scientific and engineering applications.

  * HIP (Heterogeneous-Compute Interface for Portability): HIP is a key component of ROCm that allows developers to write GPU-accelerated code in a way that can be easily ported between AMD and NVIDIA GPUs. It offers a high-level API and tools for GPU application development.

  * ROCr (ROCm Runtime API): ROCr is an API that provides low-level control and management of AMD GPUs. It allows developers to interact directly with the GPU hardware and execute custom kernels.

  * ROCProfiler: ROCProfiler is a profiling tool that helps developers analyze the performance of GPU-accelerated code. It provides insights into kernel execution times, memory usage, and other performance metrics.

  * ROCTracer: This tool enables fine-grained GPU kernel tracing and profiling, making it easier to identify performance bottlenecks and optimize GPU code.

  * ROCm SMI (System Management Interface): ROCm SMI allows users to monitor and manage the health and performance of AMD GPUs. It provides information about GPU temperature, power consumption, and other metrics.

Supported Frameworks:
ROCm is compatible with popular machine learning and deep learning frameworks, including TensorFlow and PyTorch. This compatibility allows researchers and data scientists to leverage the power of AMD GPUs for training and inference in machine learning models.

ROCm Use Cases:

  * Scientific Computing: ROCm is widely used in scientific research for simulations, computational fluid dynamics, molecular modeling, and other scientific computations that benefit from GPU acceleration.

  * Machine Learning: ROCm enables training and inference for deep learning models, making it valuable for AI and machine learning applications.

  * Data Analytics: ROCm can accelerate data analytics tasks, helping organizations process large datasets more efficiently.

  * High-Performance Computing (HPC): ROCm is suitable for HPC clusters and supercomputers, where GPU acceleration is essential for scientific simulations and numerical calculations.

Community and Open Source:
ROCm is developed as an open-source project, fostering a collaborative community of developers, researchers, and enthusiasts. The open nature of ROCm encourages contributions, improvements, and the development of custom solutions for specific use cases.

Compatibility:
ROCm is primarily designed for AMD GPUs, including Radeon Instinct and Radeon Pro series cards. It is compatible with Linux-based operating systems and is often used with popular Linux distributions such as Ubuntu and CentOS.

[ROCM Documentation]()
[Compatible GPU List]()

# Current GPU
The [MSI Gaming Radeon RX 7900 XTX](https://www.amd.com/en/products/graphics/amd-radeon-rx-7900xtx) is a high-end graphics card designed for gaming and demanding graphics workloads. With 24GB of GDDR6 memory and support for PCI Express 4.0, it delivers excellent performance and is suitable for gamers and professionals looking for top-tier graphics capabilities.

| **Technical Specifications**              | **Details**                                      |
|-------------------------------------------|--------------------------------------------------|
| **Graphics Processing Unit**              | AMD Radeon RX 7900 XTX (Navi 31)                 |
| **Architecture**                          | RDNA 3 (gfx1100)                                 |
| **Core Clock**                            | Up to 2340 MHz (Boost Clock)                     |
| **Compute Units**                         | 96                                               |
| **Boost Frequency**                       | Up to 2500 MHz                                   |
| **Stream Processors**                     | 6144                                             |
| **AI Accelerators**                       | 192                                              |
| **Peak Pixel Fill-Rate**                  | Up to 480 GP/s                                   |
| **Peak Texture Fill-Rate**                | Up to 960 GT/s                                   |
| **Peak Half Precision Compute Performance**| 123 TFLOPs                                       |
| **Peak Single Precision Compute Performance**| 61 TFLOPs                                      |
| **ROPs**                                  | 192                                              |
| **Texture Units**                         | 384                                              |
| **Transistor Count**                      | 58 B                                             |
| **Memory**                                | 24GB GDDR6                                       |
| **Memory Speed**                          | Up to 20 Gbps (Effective)                        |
| **Memory Type**                           | GDDR6                                            |
| **Memory Bus**                            | 384-bit                                          |
| **Memory Bandwidth**                      | Up to 960 GB/s                                   |
| **Effective Memory Bandwidth**            | Up to 3500 GB/s                                  |
| **AMD Infinity Cache Technology**         | 96 MB                                            |
| **PCI Express Version**                   | PCIe 4.0                                         |
| **TDP (Thermal Design Power)**            | 330W                                             |
| **Typical Board Power (Desktop)**         | 355 W                                            |
| **Minimum PSU Recommendation**            | 800 W                                            |
| **Power Connectors**                      | 2 x 8-pin PCIe                                   |
| **Display Outputs**                       | - 3 x DisplayPort 1.4a                           |
|                                           | - 1 x HDMI 2.1                                   |
| **DirectX Support**                       | DirectX 12 Ultimate                             |
| **Ray Tracing Support**                   | AMD Ray Accelerator, Ray Tracing Support         |
| **VR Ready**                              | Yes                                              |
| **CrossFire Support**                     | Yes (With compatible AMD GPUs)                   |
| **RGB Lighting**                          | Mystic Light RGB lighting                        |
| **Form Factor**                           | ATX                                              |
| **Dimensions (L X W X H)**                                | 325 mm (12.8 inches) X 141 mm (5.6 inches) X 56 mm (2.2 inches)                                         |
| **Slot Size**                             | 2.5 slots                                        |
| **Cooling**                               | Triple-fan cooling system with Zero Frozr        |
| **Recommended PSU**                       | Minimum 750W                                     |
| **Operating Systems**                     | - Windows 10/11 (64-bit)                         |
|                                           | - Linux (64-bit)                                 |
| **Warranty**                              | 3 years                                          |

The MSI Gaming Radeon RX 7900 XTX is a powerful graphics card that boasts 24GB of GDDR6 memory and supports PCI Express 4.0, making it ideal for high-resolution gaming, content creation, and professional applications. Its triple-fan cooling system ensures efficient heat dissipation, and it features RGB lighting for customization. With DirectX 12 Ultimate support and ray tracing capabilities, it provides an immersive gaming experience. Additionally, it supports CrossFire for multi-GPU setups and is VR-ready. This graphics card is a solid choice for enthusiasts and gamers seeking top-notch performance.

# Walkthrough

## Install Ubuntu 22.4.03
* Minimal Installation
* Download updates

## ROCm and driver installation

1. Make the directory if it doesn't exist yet. This location is recommended by the distribution maintainers.
```bash
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
```

2. Download the key, convert the signing-key to a full keyring required by apt and store in the keyring directory.
```bash
wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | \
    gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null
```

3. Register kernel-mode driver. Add the AMDGPU repository for the driver.
```bash
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/6.0/ubuntu jammy main" \
    | sudo tee /etc/apt/sources.list.d/amdgpu.list
sudo apt update
```

4. Register ROCm packages and add the ROCm repository.
```bash
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/6.0 jammy main" \
    | sudo tee --append /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' \
    | sudo tee /etc/apt/preferences.d/rocm-pin-600
```

5. Install kernel driver
```bash
sudo apt install amdgpu-dkms
```

6. Reboot.
```bash
sudo reboot
```

7. Install ROCm packages
```bash
sudo apt install rocm-hip-sdk
```

9. Add the current user to the "render" and "video" groups.
```bash
sudo usermod -a -G render,video $LOGNAME
```

8. To install the necessary Linux kernel headers and extra modules for your system, execute the command. This will automatically download and install the appropriate versions matching your current kernel.
```bash
sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
```

9. Configure PATH. Add binary paths to the PATH environment variable.
```bash
export PATH=$PATH:/opt/rocm-6.0/bin
```

## Check settings
1. Verify kernel-mode driver installation.
```bash
dkms status
```
2. Verify ROCm installation.
```bash
/opt/rocm-6.0/bin/rocminfo
/opt/rocm-6.0/bin/clinfo
```

3. Verify package installation.
```bash
sudo apt list --installed
```

## Repo setup
1. Install git
```bash
sudo apt install git -y
```

2. Clone repo containing hello world files
```bash
git clone https://github.com/vampireLibrarianMonk/amd-gpu-hello.git
```

## Python environment setup
Substitute conda for mamba.
[Command Cheat Sheet](https://www.datacamp.com/cheat-sheet/conda-cheat-sheet)

### Pytorch

1. Create torch mamba environment
```bash
mamba create --name pytorch-rocm python=3.10 -y
mamba activate pytorch-rocm
```

2. Install [reference](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/install-pytorch.html)
```bash
wget https://repo.radeon.com/rocm/manylinux/rocm-rel-5.7/torch-2.0.1%2Brocm5.7-cp310-cp310-linux_x86_64.whl
wget https://repo.radeon.com/rocm/manylinux/rocm-rel-5.7/torchvision-0.15.2%2Brocm5.7-cp310-cp310-linux_x86_64.whl
pip3 install --force-reinstall torch-2.0.1+rocm5.7-cp310-cp310-linux_x86_64.whl torchvision-0.15.2+rocm5.7-cp310-cp310-linux_x86_64.whl 
```

3. Verify if Pytorch is installed and detecting the GPU compute device.
```bash
python3 -c 'import torch' 2> /dev/null && echo 'Success' || echo 'Failure'
```

4. Enter command to test if the GPU is available.
```bash
python3 -c 'import torch; print(torch.cuda.is_available())'
```

5. Enter command to display installed GPU device name.
```bash
python3 -c "import torch; print(f'device name [0]:', torch.cuda.get_device_name(0))"
```

6. Run the preliminary hello world
```bash
python pytorch_mnist_numbers.py 
```

Result:

### Tensorflow
1. Create tensorflow mamba environment
```bash
mamba create --name tensorflow-rocm python=3.10 -y
mamba activate tensorflow-rocm
```

2. Was told to use this build in lieu of all the other version issues recently experienced.
Issues encountered was missing comma keeping gfx1100 from being a valid card.
```bash
pip install http://ml-ci.amd.com:21096/job/tensorflow/job/nightly-rocmfork-develop-upstream/job/nightly-build-whl/lastSuccessfulBuild/artifact/packages-3.10/tf_nightly_rocm-2.16.0.600.dev20240109-cp310-cp310-manylinux2014_x86_64.whl
```

3. Had to install this library as well
```bash
pip3 install requests
```

4. Default way I test if tensorflow can see the GPU
```bash
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

5. Run the preliminary hello world
```bash
python tensorflow-rocm.py 
```

Result:
