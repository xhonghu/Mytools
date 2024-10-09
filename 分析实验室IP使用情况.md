

# **分析实验室IP占用情况：**

## ping网段的所有地址：

1.首先在windows的终端指定的目录下创建一个ip-info.txt文档，用来存储ping各个ip的信息

2.在cmd中执行下面语句

```python
for /l %i in (0,1,255) do (ping xxx.xxx.xxx.%i -n 1 >>ip-info.txt)

#其中xxx.xxx.xxx.代表你实验室所在的局域网网段，例如我们实验室的网段在10.12.44.XXX下则执行

for /l %i in (0,1,255) do (ping 10.12.44.%i -n 1 >>ip-info.txt)
```

3.待终端脚本执行结束之后，将终端指定的目录下的ip-info.txt打开将内容复制到python文件ipinfo.py同级目录下。

***（注意最好是在ipinfo.py目录下重新创建ip-info.txt文件，然后将终端目录下的ip-info.txt内容复制过去，而不是直接把文件复制过去，不然可能会出现乱码的现象）***

ipinfo.py文件代码如下所示：

```python
def PrintIP(list):
    for i in list:
        print("10.12.44." + str(i))
    print()

f=open("ipinfo.txt",encoding='utf_8')
occupation = []
available = []
all = [i for i in range(0, 256)]
for i in range(0,1763):
    data = f.readline()
    data1 = list(data)
    if(len(data1) > 8):
        if(data1[-8] == 'T' or data1[-7] == 'T'):
            occupation.append(int(data[12:15]))
    if(data[20:29] == '无法访问目标主机。' ):
        available.append(int(data2[17:-14]))
    data2 = data
overtime = list(set(all)-set(occupation)-set(available))

print("已经占用ip有以下：" + str(len(occupation)) +"个")
PrintIP(occupation)
print("可用ip还有以下：" + str(len(available)) +"个")
PrintIP(available)
print("请求超时的ip有以下：" + str(len(overtime)) +"个")
PrintIP(overtime)
f.close()
```

4.执行ipinfo.py,其中ip已经被占用的就不要使用了，请求超时的ip也不要使用。可以从可用的ip里选一个使用，值越大越好。



