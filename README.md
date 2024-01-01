# Foreword
This repo was created for anyone curious as to what is going on with AMD GPUs,ROCm (Radeon Open Compute) and the machine learning space. 

The GPU referred to in this tutorial is an MSI Gaming Radeon 7900 XTX 24 GB.

One thing of annoyance is the long term support of GPUs with a ongoing comment section [here](https://github.com/ROCm/ROCm/issues/2308). To summarize NVIDIA usually supports their GPUs for 8+ years and it looks like AMD only for ~4 years. Keep this in mind when working with these GPUs!

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

## GPU
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
## Radeon™ Software for Linux® version 23.20.00.48 for Ubuntu 22.04.3 HWE with [ROCm 5.7](https://rocm.docs.amd.com/en/docs-5.7.1/release/gpu_os_support.html) [ROCm latest](https://rocm.docs.amd.com/en/latest/)
I used the following [link](https://www.amd.com/en/support/graphics/amd-radeon-rx-7000-series/amd-radeon-rx-7900-series/amd-radeon-rx-7900xtx) to get my GPU's supporting software installed.

1. The following steps were used to get the software installed.
```bash
sudo apt update
wget https://repo.radeon.com/amdgpu-install/23.20.00.48/ubuntu/jammy/amdgpu-install_5.7.00.48.50700-1_all.deb
sudo apt install ./amdgpu-install_5.7.00.48.50700-1_all.deb
sudo amdgpu-install -y --usecase=graphics,rocm
sudo usermod -a -G render,video $LOGNAME
```

## Monitoring GPU
Monitor the GPU with [rocm-smi](https://manpages.debian.org/experimental/rocm-smi/rocm-smi.1.en.html).

Usage (use watch -n 1 # replace 1 with second duration):
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

## Driver Signing
Record how I got driver signing to work. TBD for next fresh installation.

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

Result for Mamba:

```bash
~/mambaforge/envs/pytorch-rocm/bin/python3
```

Result for Base OS:

```bash
/usr/bin/python3
```

3. Use the following [instruction set](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html) to set your python interpreter to use your python environment.

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

```bash
wget https://repo.radeon.com/rocm/manylinux/rocm-rel-5.7/torch-2.0.1%2Brocm5.7-cp310-cp310-linux_x86_64.whl
wget https://repo.radeon.com/rocm/manylinux/rocm-rel-5.7/torchvision-0.15.2%2Brocm5.7-cp310-cp310-linux_x86_64.whl
pip3 install --force-reinstall torch-2.0.1+rocm5.7-cp310-cp310-linux_x86_64.whl torchvision-0.15.2+rocm5.7-cp310-cp310-linux_x86_64.whl 
```

This may take several minutes. 

Important! AMD recommends proceeding with ROCm WHLs available at repo.radeon.com. 

The ROCm WHLs available at PyTorch.org are not tested extensively by AMD as the WHLs change regularly when the nightly builds are updated.


## Mamba Pytorch Installation
1. Create a Python Environment

```bash
mamba create --name pytorch-rocm python=3.10 -y
mamba activate pytorch-rocm
```

3Install pip dependencies for rocm in Base OS Python section.

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

Expected result:
```bash
Collecting environment information...
PyTorch version: 2.0.1+rocm5.7
Is debug build: False
CUDA used to build PyTorch: N/A
ROCM used to build PyTorch: 5.7.31921-d1770ee1b

OS: Ubuntu 22.04.3 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.27.9
Libc version: glibc-2.35

Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-6.2.0-37-generic-x86_64-with-glibc2.35
Is CUDA available: True
CUDA runtime version: Could not collect
CUDA_MODULE_LOADING set to: LAZY
GPU models and configuration: Radeon RX 7900 XTX
Nvidia driver version: Could not collect
cuDNN version: Could not collect
HIP runtime version: 5.7.31921
MIOpen runtime version: 2.20.0
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
BogoMIPS:                           7400.07
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
[pip3] numpy==1.26.2
[pip3] pytorch-triton-rocm==2.0.2
[pip3] torch==2.0.1+rocm5.7
[pip3] torchvision==0.15.2+rocm5.7
[conda] Could not collect
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

## Tensorflow Pre-requisites
### Note: Instructions for tensorflow with rocm 6.0.0 support for possible gfx1100 and gfx1030 directions reference [here](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/1956) then [here](https://gist.github.com/briansp2020/1e8c3e5735087398ebfd9514f26a0007). As of the writing of these directions tensorflow-rocm does not have this version ready.

1. Install [ROCm libraries](https://rocmdocs.amd.com/en/latest/reference/library-index.html) and [Radeon Collective Communications Library (RCCL)](https://rocmdocs.amd.com/en/latest/reference/library-index.html#rccl).
```bash
sudo apt install rocm-libs rccl
```

## Mamba Tensorflow Installation 
1. Create a Python Environment

```bash
mamba create --name tensorflow-rocm python=3.10 -y
mamba activate tensorflow-rocm
```

2. Install pip dependencies:

```bash
pip3 install tensorflow-rocm==2.13.0.570
```

3. Enter a python terminal 
```bash
python
```

4. The following is a bookmark until the 7900 XTX (gfx1100) starts working with ROCm. Note that docker was tried and resulted in the same message.
```bash
import random
import tensorflow as tf
from tensorflow.keras import datasets, layers
from tensorflow.python.platform import build_info as tf_build_info
tf.config.list_physical_devices('GPU')
```

Result:
```bash
2023-12-17 14:27:12.731221: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-17 14:27:12.744650: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-17 14:27:12.744697: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-17 14:27:12.744715: I tensorflow/core/common_runtime/gpu/gpu_device.cc:2015] Ignoring visible gpu device (device: 0, name: Radeon RX 7900 XTX, pci bus id: 0000:2d:00.0) with AMDGPU version : gfx1100. The supported AMDGPU versions are gfx1030, gfx900, gfx906, gfx908, gfx90a, gfx940, gfx941, gfx942.
[]
```

5. However, with the following adjustment prior to opening a python terminal on the 6600 XT (gfx1032).
```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0 # This will allow the gfx1032 to work with tensorflow
```

6. The following worked in the python terminal:
```bash
(tensorflow-rocm) flaniganp@amd-lit-machine:~/Documents/repos/amd-gpu-hello$ python
Python 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 15:36:39) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from tensorflow.python.client import device_lib
2023-12-31 20:00:29.188187: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
>>> print(device_lib.list_local_devices())
2023-12-31 20:00:34.262795: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:00:34.282199: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:00:34.282247: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:00:34.282366: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:00:34.282408: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:00:34.282445: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:00:34.282471: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1639] Created device /device:GPU:0 with 7556 MB memory:  -> device: 0, name: AMD Radeon RX 6600 XT, pci bus id: 0000:2d:00.0
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 2343097017648306979
xla_global_id: -1
, name: "/device:GPU:0"
device_type: "GPU"
memory_limit: 7923040256
locality {
  bus_id: 1
  links {
  }
}
incarnation: 9876148064928784728
physical_device_desc: "device: 0, name: AMD Radeon RX 6600 XT, pci bus id: 0000:2d:00.0"
xla_global_id: 416903419
]
```

7. The following script will now work.
   ```bash
   python tensorflow-rocm.py
   ```

Result: 
```bash
(tensorflow-rocm) flaniganp@amd-lit-machine:~/Documents/repos/amd-gpu-hello$ python tensorflow-rocm.py 
2023-12-31 20:08:51.061805: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
TensorFlow version: 2.13.0.570
CUDA version: None
cuDNN version: None
2023-12-31 20:08:51.870628: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:08:51.884016: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:08:51.884065: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:08:51.884177: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero

GPU Details: {'device_name': 'AMD Radeon RX 6600 XT'}
Original Label: 9
One-Hot Encoded Label: [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
Label: 7
Class Name: Sneaker
Image Shape: (28, 28)
Print the train image shape (60000, 28, 28).
Print the train labels shape (60000,).
2023-12-31 20:08:52.141613: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:08:52.141713: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:08:52.141754: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:08:52.141869: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:08:52.141916: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:08:52.141957: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-12-31 20:08:52.141981: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1639] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 7588 MB memory:  -> device: 0, name: AMD Radeon RX 6600 XT, pci bus id: 0000:2d:00.0
2023-12-31 20:08:52.294782: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.498633: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.499161: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.501222: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.501822: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.502213: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.504239: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.505030: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
Training model...
2023-12-31 20:08:52.785612: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.787471: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.825286: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.825916: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.830358: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.831123: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.900568: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.901803: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.906232: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.906894: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.907427: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.907992: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.908492: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.908880: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.911438: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.912384: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.912746: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.916624: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.919487: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.921599: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
Epoch 1/10
2023-12-31 20:08:52.939920: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.941586: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.943255: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.944050: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.944806: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.945571: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.946023: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.946744: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.947158: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.951883: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.952331: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.960996: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.961421: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.962007: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:52.962410: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:53.239382: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:08:53.733246: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7f231f4a96c0 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2023-12-31 20:08:53.733271: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): AMD Radeon RX 6600 XT, AMDGPU ISA version: gfx1030
2023-12-31 20:08:53.736158: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:255] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.
2023-12-31 20:08:53.884795: I ./tensorflow/compiler/jit/device_compiler.h:186] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.
1864/1875 [============================>.] - ETA: 0s - loss: 0.5325 - accuracy: 0.80802023-12-31 20:09:01.701389: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.701893: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.702301: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.758605: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.759347: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.764561: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.765291: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.776704: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.777232: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.781093: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.781760: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.782300: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.782872: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.785768: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.788881: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.791756: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.794046: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.794923: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:01.874774: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 9s 4ms/step - loss: 0.5316 - accuracy: 0.8084 - val_loss: 0.4107 - val_accuracy: 0.8559
Epoch 2/10
1862/1875 [============================>.] - ETA: 0s - loss: 0.3518 - accuracy: 0.87412023-12-31 20:09:12.733672: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:12.736675: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:12.738894: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 11s 6ms/step - loss: 0.3519 - accuracy: 0.8741 - val_loss: 0.3432 - val_accuracy: 0.8769
Epoch 3/10
1853/1875 [============================>.] - ETA: 0s - loss: 0.3103 - accuracy: 0.88692023-12-31 20:09:17.201575: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:17.204493: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:17.206724: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 7s 4ms/step - loss: 0.3103 - accuracy: 0.8870 - val_loss: 0.3344 - val_accuracy: 0.8797
Epoch 4/10
1869/1875 [============================>.] - ETA: 0s - loss: 0.2835 - accuracy: 0.89722023-12-31 20:09:28.142161: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:28.147057: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:28.150815: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 9s 5ms/step - loss: 0.2836 - accuracy: 0.8971 - val_loss: 0.3157 - val_accuracy: 0.8832
Epoch 5/10
1873/1875 [============================>.] - ETA: 0s - loss: 0.2652 - accuracy: 0.90312023-12-31 20:09:35.235655: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:35.241208: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:35.245189: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 7s 4ms/step - loss: 0.2651 - accuracy: 0.9031 - val_loss: 0.2909 - val_accuracy: 0.8940
Epoch 6/10
1869/1875 [============================>.] - ETA: 0s - loss: 0.2481 - accuracy: 0.90912023-12-31 20:09:47.118881: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:47.123734: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:47.127474: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 12s 6ms/step - loss: 0.2480 - accuracy: 0.9091 - val_loss: 0.2821 - val_accuracy: 0.9002
Epoch 7/10
1865/1875 [============================>.] - ETA: 0s - loss: 0.2345 - accuracy: 0.91312023-12-31 20:09:56.939045: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:56.943949: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:09:56.947790: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 10s 5ms/step - loss: 0.2348 - accuracy: 0.9129 - val_loss: 0.2852 - val_accuracy: 0.8963
Epoch 8/10
1865/1875 [============================>.] - ETA: 0s - loss: 0.2220 - accuracy: 0.91842023-12-31 20:10:13.090012: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:13.093251: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:13.095695: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 17s 9ms/step - loss: 0.2219 - accuracy: 0.9184 - val_loss: 0.2788 - val_accuracy: 0.9000
Epoch 9/10
1866/1875 [============================>.] - ETA: 0s - loss: 0.2109 - accuracy: 0.92262023-12-31 20:10:25.807495: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:25.810573: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:25.812873: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 13s 7ms/step - loss: 0.2108 - accuracy: 0.9227 - val_loss: 0.3079 - val_accuracy: 0.8888
Epoch 10/10
1863/1875 [============================>.] - ETA: 0s - loss: 0.2024 - accuracy: 0.92452023-12-31 20:10:40.572477: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:40.575667: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:40.577970: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 15s 8ms/step - loss: 0.2023 - accuracy: 0.9246 - val_loss: 0.2773 - val_accuracy: 0.9013
Evaluating model...
2023-12-31 20:10:41.911983: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:41.917158: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:41.933317: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:41.937954: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:41.940764: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:41.942969: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
313/313 [==============================] - 6s 18ms/step - loss: 0.2773 - accuracy: 0.9013
/home/flaniganp/mambaforge/envs/tensorflow-rocm/lib/python3.10/site-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
2023-12-31 20:10:47.678182: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:47.678816: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:47.679957: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:47.681988: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2023-12-31 20:10:47.682583: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
```
