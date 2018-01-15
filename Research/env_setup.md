# A documentation of setting up various environments for AFRL research purpose.

## Content
#### 1. Linux Related
       - Running Linux Ubuntu in Win 10 with WSL
       - Adding GUI for WSL with LXDE
       - Installing Google Chrome
#### 2. Docker Related
       - Requirements
       - Important documentations
       - Installing Docker on Windows if using WSL

## 1. Linux Related
- Running Linux Ubuntu in Win 10 with WSL  
To install WSL, reference [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10).  
Also, remember to install the X server for Windows [Xming](https://sourceforge.net/projects/xming/) on Windows 10.  

- Adding GUI for WSL with LXDE  
Install LXDE [via](http://blog.sqlyog.com/how-to-add-a-gui-to-the-new-bash-console-in-windows-10/):  
```
bash
sudo apt-get install lxde
sudo apt-get install synaptic // if you want it
export DISPLAY=:0
```
If all the progress is successful, you should able to launch LXDE in linux with the command
```
startlxde
```

- Installing Google Chrome  
Make sure you have Xmin installed.
```
sudo apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```
If all the progress is successful, you should able to launch Chrome in linux with the command
```
google-chrome
```

## 2. Docker Related
- Requirements  
  - Win 10 Pro (Home edition is not supported), or  
  - Linux, or  
  - Mac  
  
- Important official documentations  
  - All the documentations are [here](https://docs.docker.com/). A few important ones are provided below for convinience.  
  - [Installing](https://docs.docker.com/engine/installation/)
  - [Getting started](https://docs.docker.com/get-started/)  
  
- Installing Docker on Windows if using WSL  
Installation of Docker on both WSL _and_ Windows is necessary. A guide can be found [here](https://blog.jayway.com/2017/04/19/running-docker-on-bash-on-windows/).  
