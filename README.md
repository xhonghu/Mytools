# **校园网命令行联网：**

```python
1、打开connection.py文件修改如下指定位置IP地址
data = {
    "c": 'Portal',
    "a": 'login',
    "callback": 'dr1003',
    "login_method": '1',
    "user_account": user_account,
    "user_password": user_password,
    ##在这里修改成服务器的所在的ip地址
    "wlan_user_ip": '10.12.44.233',
    ###############################
    "wlan_user_ipv6": '',
    "wlan_user_mac": '000000000000',
    "wlan_ac_ip": '',
    "wlan_ac_name": '',
    "jsVersion": '3.3.3',
    "v": '9749'
}

2、将connection.py文件上传到服务器并配置相关的包

3、cd到该目录执行
python connection.py 学号 密码

ping www.baidu.com 看下联网是否成功
```


# **测试服务器最适合开启的多线程数量：**

```python
1、将服务器连上网络

2、将test_numworks.py文件上传到服务器，下载相关的包

3、python test_numworks.py
   找到其中线程数对应加载数据最快的那个
```


# **烤机小脚本：**
```python
2、将gpu.py文件上传到服务器，下载相关的包

3、python gpu.py

运行脚本即可烤机，其中脚本中有个size参数，可以自己调整控制显存和计算量
```


# **git提交代码：**
```python
# 初始化git
git init
# 配置git信息
git config --global user.email XXX@qq.com
git config --global user.name XXX
# 添加需要提交内容
git add README.md
# 这句话是说把工作区的内容全部添加
git add .
# 提交暂存区并添加说明
git commit -m "first commit"
# 设置远程仓库(这里仓库需要提前建好，然后Token也需要提前生成好)
git remote add origin https://github.com/xxx/xxx.git
git remote set-url origin  https://Token@github.com/xxx/xxx.git
# 提交代码
git push -u origin master
```