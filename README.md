# Foreword
This repo was created for anyone curious as to what is going on with AMD GPUs,ROCm (Radeon Open Compute) and the machine learning space. 

The GPUs referenced in this tutorial:
  * MSI Gaming Radeon 7900 XTX 24 GB.

One thing of annoyance is the long term support of GPUs with a ongoing comment section [here](https://github.com/ROCm/ROCm/issues/2308). To summarize NVIDIA usually supports their GPUs for 8+ years and it looks like AMD only for ~4 years. Keep this in mind when working with these GPUs!

[ROCM Version List](https://rocm.docs.amd.com/en/latest/release/versions.html)

For each ROCm version ensure you check the [GPU Support and OS Compatibility (Linux)](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/reference/system-requirements.html) first prior to obtaining and using an AMD GPU.

[Tensorflow-rocm Version List](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-rocm-release.md)

# Build
## Case
[LINK](https://www.newegg.com/black-jonsbo-mesh-screen-mtx-case-micro-atx/p/2AM-006A-000B8?Item=9SIAY3SJNH9664) JONSBO D31 MESH SC BLACK Micro ATX Computer Case with Sub HD-LCD Display, M-ATX/DTX/ITX Mainboard/Support RTX 4090(335-400mm) GPU 360/280AIO,Power ATX/SFX: 100mm-220mm Multiple Tool-free Design,Black

## Cooling Accessories
### AIO
[LINK](https://www.newegg.com/be-quiet-liquid-cooling-system/p/2YM-0069-00004?Item=9SIA68VBZU7750) be quiet! PURE LOOP 360mm AIO CPU Water Cooler | All In One Water Cooling System | Intel and AMD Support | Low Noise | BW008

[LINK](https://www.newegg.com/icegale-fixed-case-fan/p/1YF-0184-00053?Item=9SIAT5SJH17984) Iceberg Thermal IceGALE Silent 120mm (Black) 3-PACK Quiet Optimized Airflow 3-Pin Case Fans

[LINK](https://www.newegg.com/bgears-vortex-120-case-fan/p/N82E16835132054?Item=N82E16835132054) Bgears Vortex 120 ARGB LED Case Fans b-ARGB Vortex 120

[LINK](https://www.newegg.com/thermal-grizzly/p/13C-003E-00004?Item=9SIA4RE6M28090) Thermal Grizzly Kryonaut Thermal Grease Paste - 1.0 Gram

## CPU
[LINK](https://www.newegg.com/amd-ryzen-9-5900x/p/N82E16819113664?Item=N82E16819113664) AMD Ryzen 9 5900X - Ryzen 9 5000 Series Vermeer (Zen 3) 12-Core 3.7 GHz Socket AM4 105W None Integrated Graphics Desktop Processor - 100-100000061WOF

## GPUs
[LINK](https://www.amazon.com/MSI-RX-6600-XT-MECH/dp/B09BK8NCPB/ref=sr_1_2?crid=3RW8YE5OCGXNU&keywords=MSI+Gaming+AMD+Radeon+RX+6600+XT+128-bit+8GB&qid=1704119107&sprefix=msi+gaming+amd+radeon+rx+6600+xt+128-bit+8gb%2Caps%2C58&sr=8-2) MSI Gaming AMD Radeon RX 6600 XT 128-bit 8GB GDDR6 DP/HDMI Dual Torx Fans FreeSync DirectX 12 VR Ready OC Graphics Card (RX 6600 XT MECH 2X 8G OC) 
[LINK](https://www.newegg.com/msi-radeon-rx-7900-xtx-rx-7900-xtx-gaming-trio-classic-24g/p/N82E16814137781?Item=N82E16814137781) MSI Gaming Radeon RX 7900 XTX 24GB GDDR6 PCI Express 4.0 ATX Video Card RX 7900 XTX GAMING TRIO CLASSIC 24G

## Hard Drive(s)
### Ubuntu Linux
[LINK] (https://www.newegg.com/samsung-970-evo-plus-500gb/p/N82E16820147742?Item=N82E16820147742) SAMSUNG 970 EVO PLUS M.2 2280 500GB PCIe Gen 3.0 x4, NVMe 1.3 V-NAND Internal Solid State Drive (SSD) MZ-V7S500B/AM 

### Windows 11 Professional
[LINK](https://www.samsung.com/us/computing/memory-storage/solid-state-drives/990-pro-w-heatsink-pcie-4-0-nvme-ssd-1tb-mz-v9p1t0cw/?cid=pla-ecomm-pfs-mms-us-google-na-03042022-170119-&ds_e=GOOGLE-cr:0-pl:267548417-&ds_c=FF~Memory+PMax_CN~Memory+PMax_ID~B0000PWD_PH~on_MK~us_BS~ms_PR~ecom_SB~memcross_FS~hqloe_CA~smp_KS~nag_MT~na-&ds_ag=-&ds_k=&gad_source=1&gclid=CjwKCAiA1fqrBhA1EiwAMU5m_zGVd5S4llCHabWb0dBGGrnaAD4y-z5oO5w4VcCuGRn1VwT-98lt_RoC5osQAvD_BwE&gclsrc=aw.ds) 990 PRO w/ Heatsink PCIe®4.0 NVMe™ SSD 1TB

## Memory
[LINK](https://www.newegg.com/g-skill-128gb-288-pin-ddr4-sdram/p/N82E16820232992?Item=N82E16820232992) G.SKILL TridentZ RGB Series 128GB (4 x 32GB) 288-Pin PC RAM DDR4 3600 (PC4 28800) Desktop Memory Model F4-3600C18Q-128GTZR

## Motherboard
[LINK](https://www.newegg.com/msi-mag-b550m-mortar-max-wifi/p/N82E16813144636?Item=N82E16813144636) MSI MAG B550M MORTAR MAX WIFI DDR4 AM4 AMD B550 SATA 6Gb/s Micro-ATX Wi-Fi 6E 2.5Gbps LAN M.2 (Key-E) Motherboards - AMD

## Power Supply
[LINK](https://www.newegg.com/deepcool-r-pq850m-fa0b-us-850-w/p/N82E16817328036?Item=N82E16817328036) Deepcool PQ850M R-PQ850M-FA0B-US 850 W ATX12V V2.4 80 PLUS GOLD Certified Full Modular Active PFC Power Supply

# Getting Started
## Radeon Open Compute (ROCm)
Version Used [6.0.0](https://rocm.docs.amd.com/en/docs-6.0.0/) [Compatible GPU List](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/reference/system-requirements.html)

ROCm is an open-source stack, composed primarily of open-source software, designed for graphics processing unit (GPU) computation. ROCm consists of a collection of drivers, development tools, and APIs that enable GPU programming from low-level kernel to end-user applications.

With ROCm, you can customize your GPU software to meet your specific needs. You can develop, collaborate, test, and deploy your applications in a free, open source, integrated, and secure software ecosystem. ROCm is particularly well-suited to GPU-accelerated high-performance computing (HPC), artificial intelligence (AI), scientific computing, and computer aided design (CAD).

ROCm is powered by AMD’s Heterogeneous-computing Interface for Portability (HIP), an open-source software C++ GPU programming environment and its corresponding runtime. HIP allows ROCm developers to create portable applications on different platforms by deploying code on a range of platforms, from dedicated gaming GPUs to exascale HPC clusters.

ROCm supports programming models, such as OpenMP and OpenCL, and includes all necessary open source software compilers, debuggers, and libraries. ROCm is fully integrated into machine learning (ML) frameworks, such as PyTorch and TensorFlow.Key Components of ROCm:

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

ROCm Packages:

  * rocm-dkms (ROCm Dynamic Kernel Module Support):

    * rocm-dkms is a package that provides Dynamic Kernel Module Support (DKMS) for the ROCm (Radeon Open Compute) software stack.
      
      * Dynamic Kernel Module Support (DKMS):
        
      * DKMS is a framework that enables automatic building and installation of kernel modules when the Linux kernel is updated.
        
      * It ensures that ROCm-specific kernel modules stay compatible with different kernel versions without manual intervention.
        
      * Ensures ROCm compatibility with various Linux kernels, making it easier to maintain ROCm functionality.

  * rocm-libs:
    
      * rocm-libs contains GPU-accelerated libraries and tools for high-performance computing, machine learning, and more, as part of the ROCm software stack.
        
        * ROCm is an open-source framework for GPU computing on AMD GPUs.
          
        * rocm-libs is a fundamental part of this stack, providing essential libraries.
          
        * ROCm Libraries include optimized GPU libraries such as ROCm Math Libraries (RocBLAS, rocSOLVER) and ROCm Communication Libraries (RCCL).
          
        * These libraries enhance performance for various computing workloads.
          
        * Provides GPU-accelerated capabilities for scientific computing, machine learning, and deep learning tasks.
          
        * Optimized libraries improve the efficiency of GPU-based applications.

  * rccl (ROCm Communication Collectives Library):
    
    * rccl is a specific library within the ROCm stack, designed to optimize GPU communication and synchronization for parallel computing workloads.
      
      * rccl focuses on optimizing communication primitives and collectives for multi-GPU parallel computing.
        
      * It enhances synchronization and data exchange between GPUs.
        
      * Valuable for distributed GPU computing, especially in deep learning training across multiple GPUs.
        
      * Improves the performance and scalability of GPU-accelerated parallel computing applications.
        
      * Enables efficient communication and coordination between GPUs in multi-GPU systems.

Why They Are Important:

    rocm-dkms: Ensures that ROCm remains compatible with different Linux kernel versions, simplifying the maintenance of GPU compute capabilities on AMD GPUs.

    rocm-libs: Provides essential GPU-accelerated libraries for various high-performance computing tasks, making it easier to develop efficient applications.

    rccl: Optimizes GPU communication for parallel computing, enhancing the performance and scalability of multi-GPU applications, particularly valuable in deep learning and scientific computing.

# PyTorch:
PyTorch is an open-source deep learning framework known for its dynamic computation graph, making it flexible for experimentation and debugging. It's Pythonic, easy to learn, and widely used in research for tasks like computer vision, natural language processing, and reinforcement learning.

Version Used:
  * [torch==2.3.0.dev20240110+rocm5.7]([2.3.0.dev20240110+rocm5.7](https://download.pytorch.org/whl/nightly/rocm5.7/torch-2.3.0.dev20240110%2Brocm5.7-cp310-cp310-linux_x86_64.whl))
  * [torchvision==0.18.0.dev20240110+rocm5.7](https://download.pytorch.org/whl/nightly/rocm5.7/torchvision-0.18.0.dev20240110%2Brocm5.7-cp310-cp310-linux_x86_64.whl)

## Comments: 
  * Pytorch has not been as big of a pain setting up as Tensorflow. Go back in versions and try it, unless asked I'll just try later versions). 

# TensorFlow:
TensorFlow, developed by Google Brain, is an open-source machine learning framework with a static computation graph, optimized for production deployments. It's scalable, works on CPUs and GPUs, and offers TensorFlow Serving for model deployment. TensorFlow provides high-level APIs like Keras and is used in various machine learning applications, including computer vision, natural language processing, and recommendation systems.

Version Used [2.16.0.600-dev20240109](http://ml-ci.amd.com:21096/job/tensorflow/job/nightly-rocmfork-develop-upstream/job/nightly-build-whl/lastSuccessfulBuild/artifact/packages-3.10/tf_nightly_rocm-2.16.0.600.dev20240109-cp310-cp310-manylinux2014_x86_64.whl)

## Comments:
 * [2.15.0.600](http://ml-ci.amd.com:21096/job/tensorflow/job/release-rocmfork-r215-rocm-enhanced/job/release-build-whl/) specifically this [one](http://ml-ci.amd.com:21096/job/tensorflow/job/release-rocmfork-r215-rocm-enhanced/job/release-build-whl/lastSuccessfulBuild/artifact/packages-3.10/tensorflow_rocm-2.15.0.600-cp310-cp310-manylinux2014_x86_64.whl) works.
 * 2.14.0.600: The supported AMDGPU versions are gfx1030gfx1100, gfx900, gfx906, gfx908, gfx90a, gfx940, gfx941, gfx942.
   * Yes a comma prevents this version from running.
   * Recompilation at tensorflow/compiler/xla/stream_executor/device_description.h line 184, which takes an hour on the above build will get tried and this instruction updated if it works. 
 * 2.13.1.600: The supported AMDGPU versions are gfx1030, gfx900, gfx906, gfx908, gfx90a, gfx940, gfx941, gfx942.

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

## ROCm Driver and Package Installation
ROCm Platform: Offers a comprehensive foundation for HPC, machine learning, and scientific research on AMD GPUs.
 
Installation instructions take from [here](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/how-to/native-install/ubuntu.html)
 
1. Download and convert the package signing key.   
```bash
# Make the directory if it doesn't exist yet.
# This location is recommended by the distribution maintainers.
sudo mkdir --parents --mode=0755 /etc/apt/keyrings

# Download the key, convert the signing-key to a full
# keyring required by apt and store in the keyring directory
wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null
```   
 
Note: 
The GPG key may change; ensure it is updated when installing a new release. If the key signature verification fails while updating, re-add the key from the ROCm to the apt repository as mentioned above. The current rocm.gpg.key is not available in a standard key ring distribution but has the following SHA1 sum hash: 73f5d8100de6048aa38a8b84cd9a87f05177d208 rocm.gpg.key
  
2. Add the AMDGPU repository for the driver.  
```bash
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/6.0/ubuntu jammy main" \
    | sudo tee /etc/apt/sources.list.d/amdgpu.list
sudo apt update
```

3. Add the ROCm repository.
```bash
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/6.0 jammy main" \
    | sudo tee --append /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' \
    | sudo tee /etc/apt/preferences.d/rocm-pin-600
```

4. Install kernel driver
```bash
sudo apt-get install -y amdgpu-dkms
```

5. Install ROCm packages
```bash
sudo apt-get install -y rocm-hip-sdk
```

6. Add yourself to the rend and video group
```bash
sudo usermod -a -G render,video $LOGNAME
```
 
## Post Installation Instructions.
Instructions taken from [here](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/how-to/native-install/post-install.html)

1. Configure the system linker. Instruct the system linker where to find shared objects (.so-files) for ROCm applications.

```bash
sudo tee --append /etc/ld.so.conf.d/rocm.conf <<EOF
/opt/rocm/lib
/opt/rocm/lib64
EOF
sudo ldconfig
```

2. Configure PATH. Add binary paths to the PATH environment variable.
```bash
export PATH=$PATH:/opt/rocm-6.0.0/bin
```

3. Verify kernel-mode driver installation.
```bash
dkms status
```

4. Verify ROCm installation.
```bash
rocminfo
```

5. Verify system management interface (smi)
```bash
rocm-smi
```

## ROCm Development Tools 
1. Install Python Packages

`CppHeaderParser` A Python library that parses C++ header files to facilitate easy automation of code generation or documentation preparation tasks.

`argparse` A standard Python library for parsing command-line arguments; useful for building user-friendly command-line tools.

```bash
pip3 install CppHeaderParser argparse
```
    
2. Clone ROCm-Developer-Tools Repository, roctracer is a tool for tracing ROCm APIs, facilitating debugging and performance analysis.
```bash
git clone -b amd-master https://github.com/ROCm-Developer-Tools/roctracer
```

3. Navigate to the cloned directory, changes the current directory to roctracer, where you can build the project and explore its contents.
```bash
cd roctracer
```

4. Install dependencies:

  * `cmake` An open-source, cross-platform family of tools designed to build, test, and package software.
  * `doxygen` A documentation generator for various programming languages.
  * `gcc & g++` The GNU Compiler Collection includes front ends for C and C++, among others.
  * `graphviz` Provides a way of representing structural information as diagrams of abstract graphs and networks.
  * `libatomic1` Provides support for atomic operations in GCC.
  * `make` A tool which controls the generation of executables and other non-source files of a program from the program's source files.
  * `texlive-full` A comprehensive TeX document production system.

```bash
sudo apt-get install -y cmake doxygen gcc graphviz g++ libatomic1 make texlive-full
```

5. Build the Project
```bash
build.sh
```

6. Compile Custom Test (Optional)
```bash
make mytest
```
 
7. Use make to install build.

```bash
sudo make install
```

## ROCm Libraries and Radeon Collective Communication Library (RCCL) Installation Command

`[rccl](https://rocmdocs.amd.com/en/latest/reference/library-index.html#rccl)` facilitates efficient communication across GPUs in multi-GPU configurations, essential for distributed deep learning and parallel computing tasks.

`[rocm-libs](https://rocmdocs.amd.com/en/latest/reference/library-index.html)` is a comprehensive suite of AMD-specific, device-side language runtime libraries designed to support the development and execution of high-performance computing applications on AMD GPUs. 

These libraries are pivotal for developers aiming to leverage AMD's GPU computing capabilities across a wide range of scientific, data analysis, and machine learning applications, providing the foundational components for building and executing compute-intensive applications on AMD's GPU architecture​

1. Install rccm and rocm-libs.
```bash
sudo apt-get install -y rccl rocm-libs
``` 

## ROCm Enumerate Agents 
A tool shipped with this [script](https://github.com/ROCm/rocminfo) to enumerate GPU agents available on a working ROCm stack.

```bash
rocminfo
```

Result:
```bash
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-69e905a91bab9202               
  Marketing Name:          Radeon RX 7900 XTX                 
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      6144(0x1800) KB                    
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2304                               
  BDFID:                   11520                              
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 550                                
  SDMA engine uCode::      19                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    25149440(0x17fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1100         
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***
```

## ROCm System Management Interface (SMI)
Monitor the GPU with [rocm-smi](https://manpages.debian.org/experimental/rocm-smi/rocm-smi.1.en.html).

Usage (use watch -n 1 # replace 1 with second duration for continuous monitoring):
```bash
rocm-smi
```

Result:
```bash
========================= ROCm System Management Interface =========================
=================================== Concise Info ===================================
GPU  Temp (DieEdge)  AvgPwr  SCLK    MCLK     Fan  Perf  PwrCap  VRAM%  GPU%  
0    37.0c           19.0W   800Mhz  1000Mhz  0%   auto  140.0W   14%   0%    
====================================================================================
=============================== End of ROCm SMI Log ================================
```

## Mamba Environment Manager
1. We’ll use the Mamba package manager to create the Python environment. You can learn more about it in my getting started tutorial.

The following bash commands will download the latest release, install it, and relaunch the current bash shell to apply the relevant changes:
```bash
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh -b
~/mambaforge/bin/mamba init
bash
```

## Base OS Python, Pytorch Installation
1. Install pytorch for ROCm via this [link](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/install-pytorch.html).
```bash
sudo apt install python3-pip -y
```

## Pycharm Integrated Development Environment
1. Download [here](https://www.jetbrains.com/pycharm/download/other.html).
```bash
PyCharm 2023.2.5 (Community Edition)
Build #PC-232.10227.11, built on November 13, 2023
Runtime version: 17.0.9+7-b1000.46 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Linux 6.2.0-37-generic
GC: G1 Young Generation, G1 Old Generation
Memory: 4096M
Cores: 24
Registry:
    ide.experimental.ui=true


Current Desktop: ubuntu:GNOME
```

2. Use the following command to find the python path.
```bash
which python3
```

3. Use the following [instruction set](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html) to set your python interpreter to use your python environment with the result of the last step.

## Pytorch for ROCM
1. Using these steps from [here](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/how-to/3rd-party/pytorch-install.html#using-a-wheels-package). Note that I updated the rocm version in the url.
```bash
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.0/
```

This may take several minutes. 

Important! AMD recommends proceeding with ROCm WHLs available at repo.radeon.com. 

The ROCm WHLs available at PyTorch.org are not tested extensively by AMD as the WHLs change regularly when the nightly builds are updated.

## Mamba Pytorch Installation
1. Create a Python Environment in mamba

```bash
mamba create --name pytorch-rocm python=3.10 -y
mamba activate pytorch-rocm
```

2. Install pip dependencies for rocm in Base OS Python section.

## Verify pytorch installation.
1. Verify if Pytorch is installed and detecting the GPU compute device.
```bash
python3 -c 'import torch' 2> /dev/null && echo 'Success' || echo 'Failure'
```

Expected result:

```bash
Success
```

2. Enter command to test if the GPU is available.
```bash
python3 -c 'import torch; print(torch.cuda.is_available())'
```

Expected result:

```bash
True
```

3. Enter command to display installed GPU device name.
```bash
python3 -c "import torch; print(f'device name [0]:', torch.cuda.get_device_name(0))"
```

Expected result: 
```bash
```

4. Enter command to display component information within the current PyTorch environment.
```bash
python3 -m torch.utils.collect_env
```

Expected result:
```bash
```

Environment set-up is complete, and the system is ready for use with PyTorch to work with machine learning models, and algorithms.

## Pytorch Hello World
The MNIST dataset is an iconic and foundational dataset in the machine learning community, primarily used for training and testing models in image processing, particularly for digit recognition tasks. It has played a critical role in the evolution of machine learning techniques and continues to be a valuable resource for education and benchmarking in the field.

Origin and Composition

* Source: The MNIST (Modified National Institute of Standards and Technology) dataset was created by Yann LeCun, Corinna Cortes, and Christopher J.C. Burges.
* Contents: It contains 70,000 images of handwritten digits (0 through 9).
* Training and Testing Split: Typically, it's split into a training set of 60,000 examples and a test set of 10,000 examples.
* Image Properties: Each image is a 28x28 pixel grayscale image. The digits have been size-normalized and centered in a fixed-size (28x28) image.

Purpose and Usage

* Benchmarking: It's widely used for training and testing in the field of machine learning, particularly for benchmarking algorithms for classification, image recognition, and computer vision.
* Educational Tool: It's often the first dataset used by beginners in machine learning and deep learning due to its simplicity and manageability.

Characteristics

* Simplicity: The simplicity of the dataset makes it ideal for testing new machine learning techniques or for educational purposes.
* Variability: Despite its simplicity, it includes a wide variety of handwriting styles, making it a robust dataset for training models to recognize handwritten digits.

Historical Significance

* Impact on Research: Since its creation, MNIST has been a cornerstone dataset for machine learning research. It has played a significant role in the development and evaluation of new machine learning techniques, especially in deep learning.
* Evolution of Use: Over time, as machine learning algorithms have become more advanced, the MNIST dataset is often considered too easy and is sometimes replaced by more complex datasets like CIFAR-10, CIFAR-100, or ImageNet for cutting-edge research.

Accessibility

* Open Access: The dataset is publicly available and can be easily accessed and used through various machine learning frameworks like TensorFlow, PyTorch, etc.

1. Run the following command to test the hello world.
```bash
python pytorch_mnist_numbers.py
```

Result:
```bash
```

## Tensorflow Pre-requisites
Note: I had to manually build tensorflow with 2.15 and later due to recent addition of gfx1100 added and a missing comma preventing use. Perhaps in 2.16 the comma will update within the pypi packages. 

1. Create a Python Environment

```bash
mamba create --name tensorflow-rocm python=3.10 -y
mamba activate tensorflow-rocm
```

2. Install pip dependencies:
```bash
```

3. The following worked in the python terminal:
```bash
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

5. The following script will now work.
```bash
python tensorflow-rocm.py
```

Result: 
```bash
```
