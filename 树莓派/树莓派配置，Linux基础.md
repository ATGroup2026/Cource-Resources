# <center>树莓派配置，Linux基础</center>

# <center>胡旭阳</center>

## 1.树莓派基本介绍

### 1>神魔是树莓派

#### *树莓派相当于一个微型计算机，被称为卡片式电脑，可以安装操作系统，并且接上显示屏鼠标键盘就可以进行更复杂的操作。*

##### 树莓派是一台“小电脑”，不是像STM32一样的单片机，他有操作系统（麻雀虽小，五脏俱全）CPU，内存，USB接口（接键盘鼠标），HDMI接口（接显示器）甚至还能连接网络

##### 树莓派是一个“微型服务器”——我们每天都在使用服务器刷短视频、玩网游，背后都是强大的服务器在支撑——功耗极低的服务器树莓派功耗极低，可以7x24小时不间断运行。我们可以在它上面搭建自己的个人网站、博客、游戏服务器，智能家居控制中心等等——人人都能上手的服务器一张银行卡大小的树莓派就能让想象变成可能

##### 树莓派是主控板，是“大脑”——GPIO引脚点灯，PWM，SPI，IIC等等——串口通信这将是你们要用到的！使用串口在树莓派和单片机之间进行通信——简单控制无需写大量初始化代码，使用python简单控制外设

![img](https://i-blog.csdnimg.cn/blog_migrate/85360f2a1f04831765a47c082996ebe6.png)

##### <u>对比着图和实物给小灯介绍各个模块</u>

### 2> 启动你的树莓派——系统烧录方法

Imager一键烧录

下载安装：https://www.raspberrypi.com/software/（imager地址）

![官网安装](https://i-blog.csdnimg.cn/direct/a945b2e57e914ae2b4e79f73089f18de.png#pic_center)

安装Imager后，打开树莓派软件，进行安装操作，依次修改图中三个选项。

![img](https://i-blog.csdnimg.cn/direct/67cd4c4be5b24cffaa83ccd6c6c17a88.png#pic_center)

*<u>（本次培训以树莓派4为例，按照自己实际版本选择）</u>*

依次raspi 4![image-20260406221313211](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260406221313211.png)

raspi os(x64)![image-20260406221350241](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260406221350241.png)

存储设备选择你的读卡器读到的TF卡**（记得格式化你的TF卡）**![image-20260406221545963](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260406221545963.png)



点击下一步![image-20260406221726691](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260406221726691.png)

点击编辑设置

![image-20260406221740411](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260406221740411.png)

在通用中按需设置用户名及WLAN

*通用设置注意事项*：

*主机名选项定义树莓派使用mDNS广播到网络的主机名。当您将树莓派连接到网络时，网络上的其他设备可以使用<hostname>.local或<hostname>.lan与您的树莓派进行通信。这里主机名无需改动*

*用户名和密码选项定义树莓派的管理员帐户的用户名和密码（自己设置即可，表示你以后需要如何登录进去，用户名不要出现中文）。*

*配置WiFi选项允许您输入无线网络的SSID（名称）和密码。就是你现在电脑上连接的网络*

***注意**，第一次不要使用公用wifi，最好使用自己的手机热点配置，因为以后登录时都是需要使用当前wifi，否则无法使用*

*WIFI国家选择：CN*

*语言设置选项允许您定义树莓派的时区和默认键盘布局。*

**在服务中一定要打开SSH**（后续需要使用ssh连接树莓派）![image-20260406221944628](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260406221944628.png)

设置完退出烧录进TF卡等待几分钟即可

### 然后接下来TF卡插入树莓派，连上显示屏尝试打开它吧awa

打开之后连上和你电脑一样的局域网，并在终端输入

```ifconfig```

wlan 的inet后面的ip地址记住，后面会用到

![image-20260409215806912](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260409215806912.png)

打开左上角，首选项。control centrl在Interfaces里打开vnc和ssh

![image-20260409215854177](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260409215854177.png)

![image-20260409215833673](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260409215833673.png)

或者命令行

```sudo raspi-config```

里Interfaces里打开vnc和ssh



## 2.Linux简介和终端操作

### 什么是Linux？？？一个操作系统而已。我们使用的Windows、MacOS，甚至于你手机上运行的系统都是操作系统。

**CLI和GUI—— 两种与电脑对话的方式**

**——图形用户界面（Graphical User Interface, GUI)你最熟悉的方式。通过点击图标、菜单、按钮来操作。**

**——命令行界面（Command-Line Interface，CLI）通过输入文本指令来操作计算机。**

![image-20260407213730182](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260407213730182.png)

<u>用wsl演示</u>

cd+目录 切换目录

*whoami显示当前用户名称*

*pwd：Print Working Directory。显示你当前所在的完整路径。*

*ls：List。列出当前目录下的文件和文件夹。*

*ls -l：以详细列表形式显示（能看到权限、所有者、大小、修改时间）。*

*ls -a：显示所有文件，包括隐藏文件（以 . 开头的文件）。*

mkdir my_folder：创建一个名为 my_folder 的目录。

touch my_file.txt：创建一个名为 my_file.txt 的空文件。

cp file1.txt file2.txt：复制 file1.txt 为 file2.txt。

mv file1.txt new_name.txt：移动/重命名 文件。

rm bad_file.txt：删除文件。

rm -r old_folder：递归删除目录及其内部所有内容。（使用要极其小心！可能把系统直接扬了……）

nano/vim 编辑文件内容

**等等等，命令符不用记，用到什么直接去搜**

![image-20260407214100018](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260407214100018.png)

![image-20260407215016969](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260407215016969.png)

## 3.ssh介绍

### 神魔是ssh？？？

SSH（Secure Shell）是一种安全通道协议，主要用来实现字符界面的远程登录、远程复制等功能。
SSH协议对通信双方的数据传输进行了加密处理，其中包括用户登录时输入的用户口令。因此SSH协议具有很好的安全性。

![image-20260407215641175](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260407215641175.png)

<u>让小灯尝试连接我的服务器</u>

ssh root@ip

密码At123456

并在我的服务器里面创建一个自己名字拼音的文件，在文件里写入HELLO AT!并保存退出

## 4.用vsc和mobaxterm连接树莓派

### 在VScode搜索remote-ssh并安装

![image-20260408131549570](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260408131549570.png)

### 点击这个电脑样式的小图标![image-20260408131624952](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260408131624952.png)进入

![image-20260408131648144](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260408131648144.png)

### 点击加号输入ssh usrname@ip

![image-20260408131726281](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260408131726281.png)

### 然后回车连接，选择linux并输入密码（自己设置的）

### 如果连接有任何问题点击设置查看config

![image-20260408131931556](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260408131931556.png)

### 选择第一个进去查看你的ip与用户名是否有错误且不能重复（重复删除多余的即可）

#### mobaxterm连接看[MobaXterm连接服务器_pycharm的add configuration-CSDN博客](https://blog.csdn.net/qq_37665301/article/details/116031615?ops_request_misc=elastic_search_misc&request_id=edf54ab013ee9b5cd03c62bd619e0e36&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~ElasticSearch~search_v2-8-116031615-null-null.142^v102^pc_search_result_base8&utm_term=mobaxterm连接&spm=1018.2226.3001.4187)

![image-20260409220737456](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260409220737456.png)

## 5.用realvnc连接树莓派并原神启动

<u>输入ip即可直接连接图形化界面</u>

![image-20260409215919486](C:\Users\79028\AppData\Roaming\Typora\typora-user-images\image-20260409215919486.png)

如果打开原神板子坏了自负哈
