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

## ROCm System Management Interface (SMI)
Monitor the GPU with [rocm-smi](https://manpages.debian.org/experimental/rocm-smi/rocm-smi.1.en.html).

Usage (use watch -n 1 # replace 1 with second duration for continuous monitoring):
```bash
rocm-smi
```

# PyTorch:
PyTorch is an open-source deep learning framework known for its dynamic computation graph, making it flexible for experimentation and debugging. It's Pythonic, easy to learn, and widely used in research for tasks like computer vision, natural language processing, and reinforcement learning.

Version Used:
  * [torch==2.3.0.dev20240219+rocm6.0](https://download.pytorch.org/whl/nightly/rocm6.0/torch-2.3.0.dev20240219%2Brocm6.0-cp310-cp310-linux_x86_64.whl)
  * [torchvision==0.18.0.dev20240115+rocm6.0](https://download.pytorch.org/whl/nightly/torchvision-0.18.0.dev20240115-cp310-cp310-linux_aarch64.whl)

## Comments: 
  * Pytorch has not been as big of a pain setting up as Tensorflow. Go back in versions and try it, unless asked I'll just try later versions). 

# TensorFlow:
TensorFlow, developed by Google Brain, is an open-source machine learning framework with a static computation graph, optimized for production deployments. It's scalable, works on CPUs and GPUs, and offers TensorFlow Serving for model deployment. TensorFlow provides high-level APIs like Keras and is used in various machine learning applications, including computer vision, natural language processing, and recommendation systems.

Version Used [2.16.0.600-dev20240219](http://ml-ci.amd.com:21096/job/tensorflow/job/nightly-rocmfork-develop-upstream/job/nightly-build-whl/lastSuccessfulBuild/artifact/packages-3.10/tf_nightly_rocm-2.16.0.600.dev20240219-cp310-cp310-manylinux2014_x86_64.whl)

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

3. Add the ROCm repository:
```bash
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/6.0 jammy main" \
    | sudo tee --append /etc/apt/sources.list.d/rocm.list
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' \
    | sudo tee /etc/apt/preferences.d/rocm-pin-600
```

4. Install kernel driver:
```bash
sudo apt-get install -y amdgpu-dkms
```

5. Reboot:
```bash
sudo reboot
```

7. Update package list:
```bash
sudo apt-get update
```

8. Install ROCm packages:
```bash
sudo apt-get install -y rocm-hip-sdk
```

9. Add yourself to the rend and video group:
```bash
sudo usermod -a -G render,video $LOGNAME
```

10. Reboot, for changes to take effect:
```bash
sudo reboot
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
echo 'export PATH=$PATH:/opt/rocm-6.0.0/bin' >> ~/.bashrc
```

3. Close and open your terminal or use the following command:
```bash
source ~/.bashrc
```

4. Verify kernel-mode driver installation.
```bash
dkms status
```

5. Verify ROCm installation.
```bash
rocminfo
```

Result:
```bash
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 9 5900X 12-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 5900X 12-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3700                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            24                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    131816192(0x7db5b00) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131816192(0x7db5b00) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131816192(0x7db5b00) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
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

6. Verify system management interface (smi)
```bash
rocm-smi
```

Result:
```bash
====================================== ROCm System Management Interface ======================================
================================================ Concise Info ================================================
Device  [Model : Revision]    Temp    Power  Partitions      SCLK   MCLK     Fan  Perf  PwrCap  VRAM%  GPU%  
        Name (20 chars)       (Edge)  (Avg)  (Mem, Compute)                                                  
==============================================================================================================
0       [0x5200 : 0xc8]       45.0°C  74.0W  N/A, N/A        42Mhz  1249Mhz  0%   auto  291.0W    2%   2%    
        0x744c                                                                                               
==============================================================================================================
============================================ End of ROCm SMI Log =============================================
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
  * `libstdc++-12-dev` Development package for the GNU Standard C++ Library version 12 (solves cmath not found error)
  * `make` A tool which controls the generation of executables and other non-source files of a program from the program's source files.
  * `rpm` Builder for rpms (Fixes RPM package requires rpmbuild executable).
  * `texlive-full` A comprehensive TeX document production system.

```bash
sudo apt-get install -y cmake doxygen gcc graphviz g++ libatomic1 libstdc++-12-dev make rpm texlive-full
```

5. Build the Project
```bash
bash build.sh
```

6. Change directory to build
```bash
cd build
```

7. Compile Custom Test (Optional)
```bash
make mytest
```

Result:
```bash
[  3%] Built target dlopen
[  8%] Built target util
[ 22%] Built target roctracer
[ 26%] Built target roctracer_tool
[ 29%] Built target hip_stats
[ 33%] Built target roctx
[ 36%] Built target MatrixTranspose
[ 40%] Built target MatrixTranspose_test
[ 43%] Built target MatrixTranspose_hipaact_test
[ 47%] Built target MatrixTranspose_mgpu
[ 52%] Built target MatrixTranspose_ctest
[ 56%] Built target codeobj_test
[ 71%] Built target hsaco_targets
[ 75%] Built target copy
[ 78%] Built target roctx_test
[ 82%] Built target backward_compat_test
[ 85%] Built target load_unload_reload_test
[ 89%] Built target trace_buffer
[ 92%] Built target memory_pool
[ 96%] Built target activity_and_callback
[100%] Built target multi_pool_activities
[100%] Built target mytest
```
 
8. Use make to install build.

```bash
sudo make install
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

## Mamba Pytorch Installation
1. Create a Python Environment in mamba

```bash
mamba create --name pytorch-rocm python=3.10 -y
mamba activate pytorch-rocm
```

2. Install pip dependencies for rocm.

## Pytorch for ROCM Stable and Nightly from AMD
Important! AMD recommends proceeding with ROCm WHLs available, noting the proper ROCm version at [repo.radeon.com](https://repo.radeon.com/rocm/manylinux/). 

Here is a [sample](https://repo.radeon.com/rocm/manylinux/rocm-rel-6.0/README.html) direction set that was referenced.

1. Here is an example as of the writing of these directions:
```bash
pip3 install torch==2.1.1 torchvision==0.16.1 -f https://repo.radeon.com/rocm/manylinux/rocm-rel-6.0/ 
```

The ROCm WHLs available at PyTorch.org are not tested extensively by AMD as the WHLs change regularly when the nightly builds are updated.

2. Using these steps from [here](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/how-to/3rd-party/pytorch-install.html#using-a-wheels-package). Note that I updated the rocm version in the url.
```bash
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.0/
```

Note: This may take several minutes. 


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
device name [0]: Radeon RX 7900 XTX
```

4. Enter command to display component information within the current PyTorch environment.
```bash
python3 -m torch.utils.collect_env
```

Expected result (repo.radeon.com):
```bash
Collecting environment information...
PyTorch version: 2.1.1+rocm6.0
Is debug build: False
CUDA used to build PyTorch: N/A
ROCM used to build PyTorch: 6.0.32830-d62f6a171

OS: Ubuntu 22.04.4 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 15:36:39) [GCC 12.3.0] (64-bit runtime)
Python platform: Linux-6.5.0-18-generic-x86_64-with-glibc2.35
Is CUDA available: True
CUDA runtime version: Could not collect
CUDA_MODULE_LOADING set to: LAZY
GPU models and configuration: Radeon RX 7900 XTX
Nvidia driver version: Could not collect
cuDNN version: Could not collect
HIP runtime version: 6.0.32830
MIOpen runtime version: 3.0.0
Is XNNPACK available: True

CPU:
Architecture:                       x86_64
CPU op-mode(s):                     32-bit, 64-bit
Address sizes:                      48 bits physical, 48 bits virtual
Byte Order:                         Little Endian
CPU(s):                             24
On-line CPU(s) list:                0-23
Vendor ID:                          AuthenticAMD
Model name:                         AMD Ryzen 9 5900X 12-Core Processor
CPU family:                         25
Model:                              33
Thread(s) per core:                 2
Core(s) per socket:                 12
Socket(s):                          1
Stepping:                           2
Frequency boost:                    enabled
CPU max MHz:                        4950.1948
CPU min MHz:                        2200.0000
BogoMIPS:                           7400.37
Flags:                              fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm
Virtualization:                     AMD-V
L1d cache:                          384 KiB (12 instances)
L1i cache:                          384 KiB (12 instances)
L2 cache:                           6 MiB (12 instances)
L3 cache:                           64 MiB (2 instances)
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-23
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Mitigation; safe RET
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:           Mitigation; Retpolines, IBPB conditional, IBRS_FW, STIBP always-on, RSB filling, PBRSB-eIBRS Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] torch==2.1.1+rocm6.0
[pip3] torchvision==0.16.1+rocm6.0
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] torch                     2.1.1+rocm6.0            pypi_0    pypi
[conda] torchvision               0.16.1+rocm6.0           pypi_0    pypi
```

Environment set-up is complete, and the system is ready for use with PyTorch to work with machine learning models, and algorithms.

## Pycharm Integrated Development Environment
1. Download [here](https://www.jetbrains.com/pycharm/download/other.html).
```bash
PyCharm 2023.2.6 (Community Edition)
Build #PC-232.10300.41, built on February 14, 2024
Runtime version: 17.0.10+7-b1000.48 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Linux 6.5.0-18-generic
GC: G1 Young Generation, G1 Old Generation
Memory: 1500M
Cores: 24
Registry:
    ide.experimental.ui=true


Current Desktop: ubuntu:GNOME
```

2. Use the following command, onnce environment setup (i.e. conda, mamba etc.) to find the python path.
```bash
which python3
```

3. Use the following [instruction set](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html) to set your python interpreter to use your python environment with the result of the last step.

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
This is an experimnental Hello World using ROCm.
        PyTorch Version: 2.1.1+rocm6.0
        Torchvision Version: 0.16.1+rocm6.0
        Using [cpu|cuda]: cuda
        Using device: Radeon RX 7900 XTX
        Devices Available 1

Epoch: 1
Test set: Average loss: 0.1299, Accuracy: 9608/10000 (96%)


Epoch: 2
Test set: Average loss: 0.0811, Accuracy: 9754/10000 (98%)


Epoch: 3
Test set: Average loss: 0.0629, Accuracy: 9801/10000 (98%)


Epoch: 4
Test set: Average loss: 0.0665, Accuracy: 9780/10000 (98%)


Epoch: 5
Test set: Average loss: 0.0480, Accuracy: 9842/10000 (98%)


Epoch: 6
Test set: Average loss: 0.0486, Accuracy: 9839/10000 (98%)


Epoch: 7
Test set: Average loss: 0.0409, Accuracy: 9870/10000 (99%)


Epoch: 8
Test set: Average loss: 0.0373, Accuracy: 9873/10000 (99%)


Epoch: 9
Test set: Average loss: 0.0383, Accuracy: 9866/10000 (99%)
```

## Mamba Tensorflow for ROCM Installation
1. Create a Python Environment in mamba

```bash
mamba create --name pytorch-rocm python=3.10 -y
mamba activate pytorch-rocm
```

2. Install pip dependencies for rocm.

## Pytorch for Tensorflow ROCm Nightly 
1. Create a Python Environment

```bash
mamba create --name tensorflow-rocm python=3.10 -y
mamba activate tensorflow-rocm
```

2. Install pip dependencies:
```bash
pip3 install http://ml-ci.amd.com:21096/job/tensorflow/job/nightly-rocmfork-develop-upstream/job/nightly-build-whl/lastSuccessfulBuild/artifact/packages-3.10/tf_nightly_rocm-2.16.0.600.dev20240219-cp310-cp310-manylinux2014_x86_64.whl
```

## Tensorflow ROCm Build From Source
Use the following script to build from source, presently it builds from r2.,15-rocm-enhanced:
```bash
cd scripts/test-build-env-tensorflow
sudo bash build_tensorflow.sh $(rocm-smi --version | grep ROCM-SMI-LIB | awk '{print $NF}')
```

## Verify tensorflow installation.
1. The following worked in the python terminal:
```bash
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

Result:
```bash
(tensorflow-rocm) flaniganp@amd-gpu-machine:~/Downloads/roctracer/build$ python
Python 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 15:36:39) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from tensorflow.python.client import device_lib
2024-02-19 10:12:34.866913: E external/local_xla/xla/stream_executor/plugin_registry.cc:91] Invalid plugin kind specified: DNN
2024-02-19 10:12:34.902824: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-02-19 10:12:35.190644: E external/local_xla/xla/stream_executor/plugin_registry.cc:91] Invalid plugin kind specified: DNN
>>> print(device_lib.list_local_devices())
2024-02-19 10:12:36.669985: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:12:36.689453: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:12:36.689504: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:12:36.690504: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:12:36.690550: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:12:36.690596: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:12:36.690622: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1928] Created device /device:GPU:0 with 23466 MB memory:  -> device: 0, name: Radeon RX 7900 XTX, pci bus id: 0000:2d:00.0
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 16497019316532335090
xla_global_id: -1
, name: "/device:GPU:0"
device_type: "GPU"
memory_limit: 24605884416
locality {
  bus_id: 1
  links {
  }
}
incarnation: 17729530124763235462
physical_device_desc: "device: 0, name: Radeon RX 7900 XTX, pci bus id: 0000:2d:00.0"
xla_global_id: 416903419
]
```

4. The following script will now work.
```bash
python tensorflow-rocm.py
```

Result: 
```bash
(tensorflow-rocm) flaniganp@amd-gpu-machine:~/Documents/repos/amd-gpu-hello$ python tensorflow-rocm.py
2024-02-19 10:13:23.619015: E external/local_xla/xla/stream_executor/plugin_registry.cc:91] Invalid plugin kind specified: DNN
2024-02-19 10:13:23.658474: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-02-19 10:13:23.971159: E external/local_xla/xla/stream_executor/plugin_registry.cc:91] Invalid plugin kind specified: DNN
TensorFlow version: 2.16.0.600-dev20240219
CUDA version: None
cuDNN version: None
2024-02-19 10:13:24.618800: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:13:24.640243: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:13:24.640300: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:13:24.640414: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero

GPU Details: {'device_name': 'Radeon RX 7900 XTX'}
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-labels-idx1-ubyte.gz
29515/29515 ━━━━━━━━━━━━━━━━━━━━ 0s 1us/step
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-images-idx3-ubyte.gz
26421880/26421880 ━━━━━━━━━━━━━━━━━━━━ 0s 0us/step
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-labels-idx1-ubyte.gz
5148/5148 ━━━━━━━━━━━━━━━━━━━━ 0s 1us/step
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-images-idx3-ubyte.gz
4422102/4422102 ━━━━━━━━━━━━━━━━━━━━ 0s 0us/step
Original Label: 9
One-Hot Encoded Label: [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
Label: 4
Class Name: Coat
Image Shape: (28, 28)
Print the train image shape (60000, 28, 28).
Print the train labels shape (60000,).
2024-02-19 10:13:25.921355: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:13:25.921447: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:13:25.921482: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:13:25.921588: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:13:25.921630: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:13:25.921670: I external/local_xla/xla/stream_executor/rocm/rocm_executor.cc:874] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-02-19 10:13:25.921692: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1928] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 23450 MB memory:  -> device: 0, name: Radeon RX 7900 XTX, pci bus id: 0000:2d:00.0
Training model...
Epoch 1/10
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1708355607.215073   31946 service.cc:145] XLA service 0x7f1f58003d30 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
I0000 00:00:1708355607.215104   31946 service.cc:153]   StreamExecutor device (0): Radeon RX 7900 XTX, AMDGPU ISA version: gfx1100
2024-02-19 10:13:27.235619: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:268] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.
I0000 00:00:1708355608.478721   31946 device_compiler.h:187] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 5s 2ms/step - accuracy: 0.7301 - loss: 0.7512 - val_accuracy: 0.8580 - val_loss: 0.4015
Epoch 2/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.8678 - loss: 0.3665 - val_accuracy: 0.8736 - val_loss: 0.3542
Epoch 3/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.8809 - loss: 0.3262 - val_accuracy: 0.8854 - val_loss: 0.3259
Epoch 4/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.8957 - loss: 0.2883 - val_accuracy: 0.8909 - val_loss: 0.3089
Epoch 5/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.9013 - loss: 0.2688 - val_accuracy: 0.8925 - val_loss: 0.3001
Epoch 6/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.9080 - loss: 0.2539 - val_accuracy: 0.8993 - val_loss: 0.2838
Epoch 7/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.9118 - loss: 0.2377 - val_accuracy: 0.8985 - val_loss: 0.2798
Epoch 8/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.9186 - loss: 0.2243 - val_accuracy: 0.8993 - val_loss: 0.2809
Epoch 9/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.9229 - loss: 0.2105 - val_accuracy: 0.8986 - val_loss: 0.2837
Epoch 10/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.9246 - loss: 0.2056 - val_accuracy: 0.9066 - val_loss: 0.2697
Evaluating model...
313/313 ━━━━━━━━━━━━━━━━━━━━ 0s 700us/step - accuracy: 0.9082 - loss: 0.2783
WARNING:absl:You are saving your model as an HDF5 file via `model.save()` or `keras.saving.save_model(model)`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')` or `keras.saving.save_model(model, 'my_model.keras')`. 
```
