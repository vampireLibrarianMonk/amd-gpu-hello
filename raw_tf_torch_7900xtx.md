# Radeon Open Compute (ROCm)

Version Used[6.0.0](https://rocm.docs.amd.com/en/docs-6.0.0/)

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

8. Instruct the system linker where to find shared objects (.so-files) for ROCm applications.
```bash
sudo tee --append /etc/ld.so.conf.d/rocm.conf <<EOF
/opt/rocm/lib
/opt/rocm/lib64
EOF
sudo ldconfig
```

9. Add the current user to the "render" and "video" groups.
```bash
sudo usermod -a -G render,video $LOGNAME
```

10. Note that rocm-libs and rccl are related to AMD's ROCm (Radeon Open Compute) platform, which is an open-source framework for GPU computing on AMD GPUs. Here's a brief explanation of each:
    
  * rocm-libs: rocm-libs stands for ROCm Libraries.
    
    * These libraries are part of the ROCm software stack, which is designed to provide an open-source GPU compute platform for AMD GPUs.
      
    * ROCm Libraries include various GPU-accelerated libraries and tools for high-performance computing (HPC), scientific computing, machine learning, and deep learning workloads.
      
    * Some of the key libraries included in rocm-libs are ROCm Math Libraries (RocBLAS, rocSOLVER, etc.), ROCm Communication Libraries (RCCL, HIPCL, etc.), and other optimized GPU libraries.

  * rccl (ROCm Communication Collectives Library):
    
    * rccl is a specific library within the ROCm stack.
      
    * It is designed to provide optimized GPU communication primitives and collectives for parallel computing workloads.
      
    * rccl is used to improve communication and synchronization between GPUs in multi-GPU systems, making it particularly valuable for applications that require distributed GPU computing, like deep learning training on multiple GPUs.
      
    * This library enhances the performance and scalability of GPU-based parallel computing applications by providing efficient implementations of communication operations like reductions, broadcasts, and all-reduces across multiple GPUs.

When you install rocm-libs and rccl, you are essentially adding these GPU-accelerated libraries to your system. These libraries can be used by software applications and frameworks that require GPU acceleration and are compatible with ROCm, such as some machine learning frameworks and HPC applications.

```bash
sudo apt install rocm-libs rccl -y
```

11. Configure PATH. Add binary paths to the PATH environment variable.
```bash
export PATH=$PATH:/opt/rocm-6.0.0/bin
```

## Check settings
1. Verify kernel-mode driver installation.
```bash
dkms status
```
2. Verify ROCm installation.
```bash
rocminfo
```

Example Result:
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
      Size:                    131816200(0x7db5b08) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131816200(0x7db5b08) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131816200(0x7db5b08) KB            
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
```

3. Use the following command to actively monitor your gpu:
```bash
watch -n 1 rocm-smi
```

Example Result: 
```bash
====================================== ROCm System Management Interface ======================================
================================================ Concise Info ================================================
Device  [Model : Revision]    Temp    Power  Partitions      SCLK   MCLK     Fan  Perf  PwrCap  VRAM%  GPU%  
        Name (20 chars)       (Edge)  (Avg)  (Mem, Compute)                                                  
==============================================================================================================
0       [0x5200 : 0xc8]       46.0°C  72.0W  N/A, N/A        21Mhz  1249Mhz  0%   auto  291.0W    4%   1%    
        0x744c                                                                                               
==============================================================================================================
============================================ End of ROCm SMI Log =============================================

```

clinfo is a command-line utility that provides detailed information about OpenCL (Open Computing Language) platforms and devices available on your system. It displays information such as the number of OpenCL platforms, the types of devices (e.g., GPUs, CPUs) supported by each platform, their capabilities, and other relevant details. clinfo is commonly used by developers and users to inspect and diagnose OpenCL configurations on their systems, helping them understand the available computing resources for GPU-accelerated applications and tasks.

4. Install and check clinfo
```bash
sudo apt install clinfo -y
```

5. Check clinfo:
```bash
clinfo
```

Example Result:
```bash
Number of platforms                               2
  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 23.0.4-0ubuntu1~22.04.1
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3602.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD
  Platform Host timer resolution                  1ns

  Platform Name                                   Clover
Number of devices                                 1
  Device Name                                     Radeon RX 7900 XTX (gfx1100, LLVM 15.0.7, DRM 3.56, 6.5.0-14-generic)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 23.0.4-0ubuntu1~22.04.1
  Device Numeric Version                          0x401000 (1.1.0)
  Driver Version                                  23.0.4-0ubuntu1~22.04.1
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Max compute units                               96
  Max clock frequency                             2304MHz
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
=== CL_PROGRAM_BUILD_LOG ===
fatal error: cannot open file '/usr/lib/clc/gfx1100-amdgcn-mesa-mesa3d.bc': No such file or directory
  Preferred work group size multiple (kernel)     <getWGsizes:1504: create kernel : error -46>
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                                8 / 8       
    int                                                  4 / 4       
    long                                                 2 / 2       
    half                                                 0 / 0        (n/a)
    float                                                4 / 4       
    double                                               2 / 2        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              25769803776 (24GiB)
  Error Correction support                        No
  Max memory allocation                           6442450944 (6GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       32768 bits (4096 bytes)
  Global Memory cache type                        None
  Image support                                   No
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Max number of constant args                     16
  Max constant buffer size                        67108864 (64MiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Profiling timer resolution                      0ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    ILs with version                              SPIR-V                                                           0x400000 (1.0.0)
  Built-in kernels with version                   (n/a)
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_extended_versioning
  Device Extensions with Version                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_khr_int64_base_atomics                                        0x400000 (1.0.0)
                                                  cl_khr_int64_extended_atomics                                    0x400000 (1.0.0)
                                                  cl_khr_fp64                                                      0x400000 (1.0.0)
                                                  cl_khr_extended_versioning                                       0x400000 (1.0.0)

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx1100
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0 
  Driver Version                                  3602.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Radeon RX 7900 XTX
  Device PCI-e ID (AMD)                           0x744c
  Device Topology (AMD)                           PCI-E, 0000:2d:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               48
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                32
  SIMD instruction width (AMD)                    1
  Max clock frequency                             2304MHz
  Graphics IP (AMD)                               11.0
  Device Partition                                (core)
    Max number of sub-devices                     48
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple (kernel)     32
  Wavefront width (AMD)                           32
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              25753026560 (23.98GiB)
  Global free memory (AMD)                        24899584 (23.75GiB) 24899584 (23.75GiB)
  Global memory channels (AMD)                    12
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           21890072576 (20.39GiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics                 
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    21890072576 (20.39GiB)
  Preferred total size of global vars             25753026560 (23.98GiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        32768 (32KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 8192 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             16384x16384x8192 pixels
    Max number of read image args                 128
    Max number of write image args                8
    Max number of read/write image args           64
  Max number of pipe args                         16
  Max active pipe reservations                    16
  Max pipe packet size                            415236096 (396MiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory size per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        21890072576 (20.39GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties (on host)                      
    Out-of-order execution                        No
    Profiling                                     Yes
  Queue properties (on device)                    
    Out-of-order execution                        Yes
    Profiling                                     Yes
    Preferred size                                262144 (256KiB)
    Max size                                      8388608 (8MiB)
  Max queues on device                            1
  Max events on device                            1024
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 19:00:00 1969)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             48
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 


NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [MESA]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 Clover
    Device Name                                   Radeon RX 7900 XTX (gfx1100, LLVM 15.0.7, DRM 3.56, 6.5.0-14-generic)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 Clover
    Device Name                                   Radeon RX 7900 XTX (gfx1100, LLVM 15.0.7, DRM 3.56, 6.5.0-14-generic)
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 Clover
    Device Name                                   Radeon RX 7900 XTX (gfx1100, LLVM 15.0.7, DRM 3.56, 6.5.0-14-generic)
```

mesa-opencl-icd is an implementation of the OpenCL (Open Computing Language) ICD (Installable Client Driver) for Mesa, an open-source graphics library. It allows software applications to utilize OpenCL for GPU-accelerated computing tasks on systems with Mesa-supported graphics hardware. This package helps bridge the gap between Mesa's graphics capabilities and OpenCL, enabling developers to run OpenCL applications on systems using Mesa graphics drivers.

6. Install mesa-opencl-icd
```bash
sudo apt install mesa-opencl-icd -y
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

## Python environment setup via Mamba Environment Manager
Substitute conda for mamba.
[Command Cheat Sheet](https://www.datacamp.com/cheat-sheet/conda-cheat-sheet)

1. We’ll use the Mamba package manager to create the Python environment. You can learn more about it in my getting started tutorial.

The following bash commands will download the latest release, install it, and relaunch the current bash shell to apply the relevant changes:
```bash
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh -b
~/mambaforge/bin/mamba init
bash
```

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

Result: 
```bash
Success
```

4. Enter command to test if the GPU is available.
```bash
python3 -c 'import torch; print(torch.cuda.is_available())'
```

Result:
```bash
True
```

5. Enter command to display installed GPU device name.
```bash
python3 -c "import torch; print(f'device name [0]:', torch.cuda.get_device_name(0))"
```

Result:
```bash
device name [0]: Radeon RX 7900 XTX
```

6. Run the preliminary hello world
```bash
python pytorch_mnist_numbers.py 
```

Result:
```bash
This is an experimnental Hello World using ROCm.
	PyTorch Version: 2.0.1+rocm5.7
	Torchvision Version: 0.15.2+rocm5.7
	Using [cpu|cuda]: cuda
	Using device: Radeon RX 7900 XTX
	Devices Available 1

Training log info...

Test set: Average loss: 0.0446, Accuracy: 9842/10000 (98%)
```

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
pip install requests
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
