# **安装unbantu时分区：**

   ## 系统盘：

/EFI    300M       文件类型efi

/swap   和内存大小一致      文件类型swap

/            系统盘剩下的容量全部给根目录     文件类型ext4

   ## home目录：用来存放用户数据的

/home   多余的磁盘全部挂载给home     文件类型ext4



## 查看unbantu内存条情况：

sudo dmidecode|grep -P -A5 "Memory\s+Device"|grep Size|grep -v Range

   # **根目录一些文件夹放的内容**：

/usr 最庞大的目录，要用到的应用程序和文件几乎都在这个目录。其中包含：  16G

/usr/X11R6 存放X window的目录

/usr/bin 众多的应用程序

/usr/sbin 超级用户的一些管理程序

/usr/doc linux文档

/usr/include linux下开发和编译应用程序所需要的头文件

/usr/lib 常用的动态链接库和软件包的配置文件

/usr/man 帮助文档

/usr/src 源代码，linux内核的源代码就放在/usr/src/linux里

/usr/local/bin 本地增加的命令

/usr/local/lib 本地增加的库                                                          

/home 用户主目录的基点，比如用户user的主目录就是/home/user，可以用~user表示

/bin 二进制可执行命令

/dev 设备特殊文件

/var 某些大文件的溢出区，比方说各种服务的日志文件                

/etc 系统管理和配置文件

/etc/rc.d 启动的配置文件和脚本



# **挂载磁盘操作：**

```python
# 创建要挂载的文件夹
mkdir /data

# 找到要挂载的磁盘
sudo fdisk -l

# 挂载硬盘到该文件夹上（临时挂载）
mount /dev/sde /data

# 查看该磁盘的UUID
sudo blkid

UUID="a27baf71-57ee-4c59-91a7-4a419478a5fb" TYPE="ext4"
# 进入 fstab 修改配置
vim /etc/fstab

# 在最后面加入指定信息（完成永久磁盘挂载）
UUID=a27baf71-57ee-4c59-91a7-4a419478a5fb /data ext4 defaults 0 3

# 取消挂载
umount /dev/sde

```



# **安装显卡驱动：**

1.  **驱动管理程序来安装显卡驱动: 系统设置 -> 软件和更新 -> 附加驱动。**

   seeting->Software & Updatas ->Additional Drivers

   选择一个专业的显卡驱动下载一下。

   安装重启后，输入`nvidia-smi`会有显卡信息


​            2. **安装cuda11.8。其他版本在这个网站[CUDA Toolkit Archive | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)**

```python
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
     
sudo sh cuda_11.8.0_520.61.05_linux.run

## 输入accept进行后续操作，随即出现的界面，由于我们在安装cuda之前已经安装了Nvidia的驱动，因此这里的第一项Driver我们必须取消勾选，选择不安装驱动，随后选择Install进行后续操作。
```




3. **安装成功后：**


   ```python
   Driver:   Not Selected
   Toolkit:  Installed in /usr/local/cuda-11.1/
   Samples:  Installed in /home/hhx22/, but missing recommended libraries
   
   Please make sure that
   
    -   PATH includes /usr/local/cuda-11.1/bin
    -   LD_LIBRARY_PATH includes /usr/local/cuda-11.1/lib64, or, add /usr/local/cuda-11.1/lib64 to /etc/ld.so.conf and run ldconfig as root
   
   To uninstall the CUDA Toolkit, run cuda-uninstaller in /usr/local/cuda-11.1/bin
   ***WARNING: Incomplete installation! This installation did not install the CUDA Driver. A driver of version at least 455.00 is required for CUDA 11.1 functionality to work.
   To install the driver using this installer, run the following command, replacing <CudaInstaller> with the name of this run file:
       sudo <CudaInstaller>.run --silent --driver
   
   Logfile is /var/log/cuda-installer.log 
   
   ```

4. **配置一下.bashrc文件**

```python
   export CUDA_HOME=/usr/local/cuda-11.8
   export LD_LIBRARY_PATH=${CUDA_HOME}/lib64
   export PATH=${CUDA_HOME}/bin:${PATH}
```

#    **安装Anaconda：**

1. **从这个网站下载需要的anaconda版本[Index of /anaconda/archive/](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)**

   

2. **`bash Anaconda3-2020.02-Linux-x86_64.sh`。bash 加你下的包版本。后面跟随步骤就装好了。重新打开终端就能使用conda环境了**

   

3. **打开.bashrc文件可以找到以下conda配置,别的用户可以在自己的.bashrc文件里添加下面代码来引用conda环境**

      ~~~python
      ```
      # >>> conda initialize >>>
      # !! Contents within this block are managed by 'conda init' !!
      __conda_setup="$('/home/andrew/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
      if [ $? -eq 0 ]; then
          eval "$__conda_setup"
      else
          if [ -f "/home/andrew/anaconda3/etc/profile.d/conda.sh" ]; then
              . "/home/andrew/anaconda3/etc/profile.d/conda.sh"
          else
              export PATH="/home/andrew/anaconda3/bin:$PATH"
          fi
      fi
      unset __conda_setup
      # <<< conda initialize <<<
      
      ```
      ~~~
      
4. **配置conda的源以及包安装信息，添加一个文件.condarc内容如下**

      ````python
      ```
      channels:
        - defaults
      show_channel_urls: true
      channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
      default_channels:
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
      custom_channels:
        conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
        msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
        bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
        menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
        pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
        simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      
      ##这里配置自己环境和包安装位置
      envs_dirs:
        - /home/hhx22/conda_env
      pkgs_dirs:
        - /home/hhx22/conda_pkgs
      
      ````


5. **conda的一些用法：**

   ```python
   ##创建一个conda环境
   conda create -neme env python=3.7
   
   ##激活一个conda环境
   conda activate env
   
   ##删除一个conda换进
   conda remove -n env --all
   
   ##查看所有的conda环境
   conda info -e
   ```

   | 序号 | 功能 | 命令 |
   | :--- | --- | --- |
   | 1    | 查看conda 版本 | conda --version，conda -V |
   | 2    | 更新conda | conda update conda |
   | 3    | 查看conda帮助(对初学者很有用的命令) | conda --help，conda -h |
   | 4    | 新建虚拟环境 | conda create --name <env_name>                             |
   | 5    | 切换conda环境 | conda activate env_name |
   | 6    | 退出虚拟环境 | conda deactivate |
   | 7    | 列出所有虚拟环境 | conda info --envs       conda info -e       conda env list |
   | 8    | 复制环境 | conda create --name new_env_name --clone copied_env_name |
   | 9    | 删除环境 | conda remove --name env_name --all |
   | 10   | 精确查找包 | conda search --full-name <package_name> |
   | 11   | 模糊查找包 | conda search <something for search> |
   | 12   | 获取当前环境中已安装的包信息 | conda list |
   | 13   | 指定环境安装包 | conda install --name <env_name> <package_name=version> |
   | 14   | 在当前环境中安装包 | conda install <package_names> |
   | 15 | pip安装 | pip install <package_names> |

# **查看虚拟环境里的cuda版本：**

`conda list | grep cuda`



# **查看端口号对应的PID进程：**

查看端口号对应进程：  `netstat -tunp | grep 端口号`

杀死这个进程： `kill -9 PID号`



# **将训练脚本在后台挂起：**

**运行命令格式：**

```
nohup \
训练所需要的脚本 \
& 
```

紧接着终端会输出：nohup: ignoring input and appending output to 'nohup.out'

这样就可以在当前文件夹下的nohup.out中看到终端的所有命令

# **Vscode连接不上：**

vscode连接不上，本地删除known_hosts和known_hosts.old，路径一般是C:\Users\$(usrname)\.ssh



# **如果想设置多卡跑代码可以这样设置。**

CUDA_VISIBLE_DEVICES=0,1  python train.py 



# **linux查看目录下文件数量命令：**

**```ls | wc -l```**

