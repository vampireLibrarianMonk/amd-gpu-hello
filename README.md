# Foreword
This repo was created for anyone curious as to what is going on with AMD GPUs,ROCm (Radeon Open Compute) and the machine learning space. 

The GPUs referenced in this tutorial:
  * AMD Radeon RX 6600 XT 8 GB.
  * MSI Gaming Radeon 7900 XTX 24 GB.

One thing of annoyance is the long term support of GPUs with a ongoing comment section [here](https://github.com/ROCm/ROCm/issues/2308). To summarize NVIDIA usually supports their GPUs for 8+ years and it looks like AMD only for ~4 years. Keep this in mind when working with these GPUs!

Tensorflow directions yet to be implemented from [here](https://cprimozic.net/notes/posts/setting-up-tensorflow-with-rocm-on-7900-xtx/) for the 7900 XTX. 

[ROCM Version List](https://rocm.docs.amd.com/en/latest/release/versions.html)

For each ROCm version ensure you check the [GPU Support and OS Compatibility (Linux)](https://rocm.docs.amd.com/en/docs-5.7.0/release/gpu_os_support.html) first prior to obtaining and using an AMD GPU.

Pytorch Version List TBD

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

3. Install pip dependencies for rocm in Base OS Python section.

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
device name [0]: AMD Radeon RX 6600 XT
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

0. If using the 6600 XT (gfx1032) use the following command
```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0 # This will allow the gfx1032 to work with pytorch
```

2. Run the following command to test the hello world.
```bash
python pytorch_mnist_numbers.py
```

Result:
```bash
(pytorch-rocm) flaniganp@amd-lite-machine:~/Documents/repos/amd-gpu-hello$ python pytorch_mnist_numbers.py 
This is an experimnental Hello World using ROCm.
	PyTorch Version: 2.0.1+rocm5.7
	Torchvision Version: 0.15.2+rocm5.7
	Using [cpu|cuda]: cuda
	Using device: AMD Radeon RX 6600 XT
	Devices Available 1
Train Epoch: 1

Test set: Average loss: 0.1162, Accuracy: 9656/10000 (97%)

Train Epoch: 2

Test set: Average loss: 0.0780, Accuracy: 9752/10000 (98%)

Train Epoch: 3

Test set: Average loss: 0.0617, Accuracy: 9809/10000 (98%)

Train Epoch: 4

Test set: Average loss: 0.0490, Accuracy: 9844/10000 (98%)

Train Epoch: 5

Test set: Average loss: 0.0451, Accuracy: 9843/10000 (98%)

Train Epoch: 6

Test set: Average loss: 0.0418, Accuracy: 9862/10000 (99%)

Train Epoch: 7

Test set: Average loss: 0.0383, Accuracy: 9868/10000 (99%)

Train Epoch: 8

Test set: Average loss: 0.0451, Accuracy: 9851/10000 (99%)

Train Epoch: 9

Test set: Average loss: 0.0362, Accuracy: 9881/10000 (99%)
```

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
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
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
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

7. The following script will now work.
```bash
python tensorflow-rocm.py
```

Result: 
```bash
2024-01-01 09:37:59.114894: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
TensorFlow version: 2.13.0.570
CUDA version: None
cuDNN version: None
2024-01-01 09:37:59.991442: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-01-01 09:38:00.006591: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-01-01 09:38:00.006647: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-01-01 09:38:00.006761: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero

GPU Details: {'device_name': 'AMD Radeon RX 6600 XT'}
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-labels-idx1-ubyte.gz
29515/29515 [==============================] - 0s 0us/step
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-images-idx3-ubyte.gz
26421880/26421880 [==============================] - 0s 0us/step
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-labels-idx1-ubyte.gz
5148/5148 [==============================] - 0s 0us/step
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-images-idx3-ubyte.gz
4422102/4422102 [==============================] - 0s 0us/step
Original Label: 9
One-Hot Encoded Label: [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
Label: 1
Class Name: Trouser
Image Shape: (28, 28)
Print the train image shape (60000, 28, 28).
Print the train labels shape (60000,).
2024-01-01 09:38:01.304567: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-01-01 09:38:01.304652: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-01-01 09:38:01.304689: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-01-01 09:38:01.304796: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-01-01 09:38:01.304838: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-01-01 09:38:01.304875: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:838] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2024-01-01 09:38:01.304897: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1639] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 7556 MB memory:  -> device: 0, name: AMD Radeon RX 6600 XT, pci bus id: 0000:2d:00.0
2024-01-01 09:38:01.468501: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:01.702180: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:01.702731: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:01.704916: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:01.705515: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:01.705942: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:01.708065: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:01.708871: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
Training model...
2024-01-01 09:38:01.965532: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:01.967473: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.021397: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.022163: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.027477: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.028583: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.099869: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.101187: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.105876: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.106609: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.107197: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.107826: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.108394: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.108829: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.111439: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.112455: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.112850: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.116665: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.119706: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.122040: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
Epoch 1/10
2024-01-01 09:38:02.142350: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.144089: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.145705: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.146574: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.147379: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.148169: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.148654: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.149418: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.149855: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.154734: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.155182: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.165462: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.165944: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.166594: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.167032: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:02.463564: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:03.530729: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7f4ff3c967e0 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2024-01-01 09:38:03.530755: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): AMD Radeon RX 6600 XT, AMDGPU ISA version: gfx1030
2024-01-01 09:38:03.533716: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:255] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.
2024-01-01 09:38:03.727399: I ./tensorflow/compiler/jit/device_compiler.h:186] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.
1868/1875 [============================>.] - ETA: 0s - loss: 0.5459 - accuracy: 0.80202024-01-01 09:38:11.761524: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.762324: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.762989: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.820229: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.820901: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.826612: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.827366: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.838967: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.839486: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.843582: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.844244: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.844802: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.845396: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.848352: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.851626: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.855061: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.857416: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.858299: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:11.938181: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 10s 4ms/step - loss: 0.5457 - accuracy: 0.8022 - val_loss: 0.4102 - val_accuracy: 0.8505
Epoch 2/10
1863/1875 [============================>.] - ETA: 0s - loss: 0.3632 - accuracy: 0.87002024-01-01 09:38:19.907496: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:19.912569: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:19.916383: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 8s 4ms/step - loss: 0.3634 - accuracy: 0.8699 - val_loss: 0.3704 - val_accuracy: 0.8653
Epoch 3/10
1870/1875 [============================>.] - ETA: 0s - loss: 0.3159 - accuracy: 0.88582024-01-01 09:38:27.277862: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:27.282865: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:27.287231: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 7s 4ms/step - loss: 0.3159 - accuracy: 0.8858 - val_loss: 0.3324 - val_accuracy: 0.8832
Epoch 4/10
1872/1875 [============================>.] - ETA: 0s - loss: 0.2889 - accuracy: 0.89522024-01-01 09:38:43.167533: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:43.172763: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:43.176725: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 16s 8ms/step - loss: 0.2890 - accuracy: 0.8951 - val_loss: 0.3347 - val_accuracy: 0.8816
Epoch 5/10
1875/1875 [==============================] - ETA: 0s - loss: 0.2698 - accuracy: 0.90222024-01-01 09:38:51.114836: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:51.119853: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:51.123796: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 8s 4ms/step - loss: 0.2698 - accuracy: 0.9022 - val_loss: 0.2982 - val_accuracy: 0.8927
Epoch 6/10
1865/1875 [============================>.] - ETA: 0s - loss: 0.2517 - accuracy: 0.90902024-01-01 09:38:58.498805: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:58.503742: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:38:58.507554: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 7s 4ms/step - loss: 0.2518 - accuracy: 0.9089 - val_loss: 0.3032 - val_accuracy: 0.8926
Epoch 7/10
1874/1875 [============================>.] - ETA: 0s - loss: 0.2382 - accuracy: 0.91342024-01-01 09:39:06.015766: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:06.020733: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:06.024544: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 8s 4ms/step - loss: 0.2382 - accuracy: 0.9134 - val_loss: 0.2829 - val_accuracy: 0.8956
Epoch 8/10
1861/1875 [============================>.] - ETA: 0s - loss: 0.2272 - accuracy: 0.91742024-01-01 09:39:13.237387: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:13.243402: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:13.247480: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 7s 4ms/step - loss: 0.2272 - accuracy: 0.9174 - val_loss: 0.3059 - val_accuracy: 0.8899
Epoch 9/10
1863/1875 [============================>.] - ETA: 0s - loss: 0.2189 - accuracy: 0.91922024-01-01 09:39:21.041438: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:21.045696: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:21.049384: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 8s 4ms/step - loss: 0.2185 - accuracy: 0.9193 - val_loss: 0.2896 - val_accuracy: 0.8965
Epoch 10/10
1869/1875 [============================>.] - ETA: 0s - loss: 0.2081 - accuracy: 0.92322024-01-01 09:39:28.668377: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:28.673420: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:28.677318: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
1875/1875 [==============================] - 8s 4ms/step - loss: 0.2080 - accuracy: 0.9233 - val_loss: 0.2971 - val_accuracy: 0.8981
Evaluating model...
2024-01-01 09:39:29.246230: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:29.251652: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:29.258628: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:29.263333: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:29.266280: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:29.268687: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
313/313 [==============================] - 1s 2ms/step - loss: 0.2971 - accuracy: 0.8981
/home/flaniganp/mambaforge/envs/tensorflow-rocm/lib/python3.10/site-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
2024-01-01 09:39:29.893372: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:29.894316: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:29.896121: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:29.899235: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
2024-01-01 09:39:29.900196: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:508] ROCm Fusion is enabled.
```
