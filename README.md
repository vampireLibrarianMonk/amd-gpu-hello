# Foreword
This repo was created for anyone curious as to what is going on with AMD GPUs and the machine learning space. 

The GPU referred to in this tutorial is an MSI Gaming Radeon 7900 XTX 24 GB.

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
## Radeon™ Software for Linux® version 23.20.00.48 for Ubuntu 22.04.3 HWE with ROCm 5.7
I used the following [link](https://www.amd.com/en/support/graphics/amd-radeon-rx-7000-series/amd-radeon-rx-7900-series/amd-radeon-rx-7900xtx) to get my GPU's supporting software installed.

1. The following steps were used to get the software installed.
```bash
sudo apt update
wget https://repo.radeon.com/amdgpu-install/23.20.00.48/ubuntu/jammy/amdgpu-install_5.7.00.48.50700-1_all.deb
sudo apt install ./amdgpu-install_5.7.00.48.50700-1_all.deb
sudo amdgpu-install -y --usecase=graphics,rocm
sudo usermod -a -G render,video $LOGNAME
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


## Mamba Environment Manager, Pytorch Installation
1. We’ll use the Mamba package manager to create the Python environment. You can learn more about it in my getting started tutorial.

The following bash commands will download the latest release, install it, and relaunch the current bash shell to apply the relevant changes:
```bash
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh -b
~/mambaforge/bin/mamba init
bash
```

2. Create a Python Environment

Next, we’ll create a Python environment and activate it. The current version of the extension supports Python 3.10, so we’ll use that.
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