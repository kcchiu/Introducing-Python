# A documentation of setting up various environments for AFRL research purpose.

## Topics
#### 1. Linux Related
       - Running Linux Ubuntu in Win 10 with WSL
       - Adding GUI for WSL with LXDE
       - Installing Google Chrome
#### 2. Docker Related
       - Requirements

## 1. Linux Related
- Running Linux Ubuntu in Win 10 with WSL  
To install WSL, reference [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10).  
Also, remember to install the X server for Windows [Xming](https://sourceforge.net/projects/xming/) on Windows 10.  

- Adding GUI for WSL with LXDE
```
bash
sudo apt-get install lxde
sudo apt-get install synaptic // if you want it
export DISPLAY=:0
startlxde
```
