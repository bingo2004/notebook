**Table of Content**

* [Linux]
* [1 自动启动ss](#自动启动ss)
* [2 SSH连接远程服务器](#SSH连接远程服务器)
* [3 tar压缩与解压缩](#tar压缩与解压缩)
* [4 安装Privoxy](#安装Privoxy)
* [5 linux 后台任务，运行，关闭，查看](#linux后台任务，运行，关闭，查看)
* [6 linux 多个文件中查找字符串](#linux多个文件中查找字符串)
* [7 fortune and fortune-zh](#fortune-and-fortune-zh)
* [8 vim](#vim)
      *  批量缩进
      *  批量粘贴
      *  基本替换
* [9 sendmail 的安装与配置](#sendmail的安装与配置)
* [10 后台任务和进程查看](#后台任务和进程查看)
* [11 rename](#rename)
*
* [Python]
* [1]
* [2 set基本使用](#set基本使用)
* [3 python 发送邮件（４种）](#python发送邮件（４种）)
* [4 time模块](#time模块)
* [5 python中的下划线](#5-python中的下划线)





## 自动启动ss

shadowsocks.json文件放在/etc目录下

在/etc/rc.local中添加如下命令，注意在exit 0之前。

    sudo sslocal -c /etc/shadowsocks.json

-------

## SSH连接远程服务器

<<<<<<< HEAD
### 远程连接

    #!/bin/bash
    ssh -o StrictHostKeyChecking=no root@144.202.41.67

### 上传本地到服务器

    scp /path/filename username@servername:/path/
    scp -r /path/local_dir username@servername:path/remote_dir
    
### 从服务器下载到本地

    scp username@servername:/path/filename /path/
    scp -r username@servername:/path/remote_dir /path/local_dir
    
------------

## tar压缩与解压缩

* -c 建立压缩文档
* -x 解压
* -z 有gzip属性
* -v 显示所有过程
* -f 最后一个，接文件档案名字

例如：

    tar -czf file.tar.gz *.jpg
    tar -xzf file.tar
    
------------

## 安装Privoxy

    sudo apt-get install privoxy -y

### 修改配置文件

    sudo cp /etc/privoxy/config /etc/privoxy/config.bak
    sudo vim /etc/privoxy/config

找到 listen-address 确保有这行代码 listen-address 127.0.0.1:8118
*如果失败，尝试去掉这一行，在办公室机器就是去掉这一行之后成功的

找到 forward-socks5 确保有这行代码(没有自己加) forward-socks5 / 127.0.0.1:1080 .
*注释掉这一行后，可以恢复非privoxy连接

### 启动

    sudo service privoxy start
    sudo service privoxy status

### 配置转发

    sudo vim ~/.bashrc

在最后添加如下代码：

    export http_proxy="http://127.0.0.1:8118"
    export https_proxy="http://127.0.0.1:8118"

### 重载配置

    source ~/.bashrc
    
### 测试

    wget http://www.google.com
    
--2018-04-01 11:23:21--  http://www.google.com/
正在连接 127.0.0.1:8118... 已连接。
已发出 Proxy 请求，正在等待回应... 200 OK

------------


## instance method VS class method VS static method


		class MyClass:
				def method(self):
						return 'instance method called', self

				@classmethod
				def classmethod(cls):
						return 'class method called', cls

				@staticmethod
				def staticmethod():
						return 'static method called'


[参考文献](https://realpython.com/instance-class-and-static-methods-demystified/)

-------------

## set基本使用

set类是在python的sets模块中，现在使用的python2.3中，不需要导入sets模块可以直接创建集合。

		>>>set('boy')
		>>>set(['y', 'b', 'o'])

集合添加、删除

集合的添加有两种常用方法，分别是add和update。
集合add方法：是把要传入的元素做为一个整个添加到集合中，例如：

		>>> a = set('boy')
		>>> a.add('python')
		>>> a
		set(['y', 'python', 'b', 'o'])

创建
第一种

		set1 = {"1", "2"}
		{'1', '2'}
		print(type(set1))

第二种

		list1 = ["1", "2", "2", "1"]
		set2 = set(list1)
		print(set2)
		{'1', '2'}
		<class 'set'>

集合update方法：是把要传入的元素拆分，做为个体传入到集合中，例如：

		>>> a = set('boy')
		>>> a.update('python')
		>>> a
		set(['b', 'h', 'o', 'n', 'p', 't', 'y'])

集合删除操作方法：remove

		set(['y', 'python', 'b', 'o'])
		>>> a.remove('python')
		>>> a
		set(['y', 'b', 'o'])

    >>> 清除素有内容
    s.clear()

    >>> 两个集合的差集
    s1 = {32, 12, 34}
    s2 = {12, 43, 23}
    >>> s1中存在，s2中不存在
    print(s1.difference(s2))
    >>> {32, 34}

    >>> 对称差集
    print(s1.symmetric_difference(s2))
    >>> {32, 34, 43, 23}
    >>> difference和symmetric_different会生成新一个结果，而different_update 和 symmetic_different_update会覆盖之前集合

    >>> 移除元素 如果元素不存在，不会报错 remove 如果元素不存在，会报错
    s1.discard(32)
    print(s1)
    >>> {34, 12}

    >>> 集合pop随机移除某个元素并且获取那个参数,集合pop没有参数
    re2 = s2.pop()
    print(re2)
    >>> 43
    s3 = {11, 22, 33}
    s4 = {44, 33, 22}

    >>> 交集
    print(s3.intersection(s4))
    >>> {33, 22}

    >>> 判断两个集合有没有交集,有返回true 无返回false
    print(s3)
    print(s4)
    print(s3.isdisjoint(s4))
    >>> False 怎么是false 这不是有交集吗

    >>> 并集
    print(s3.union(s4))
    >>> {33, 22, 11, 44}

    >>> update 批量更新
    li = [21, 4, 2, 312]
    s3.update(li)
    print(s3)
  >>> {33, 2, 4, 11, 21, 22, 312}

----------

## rename

将main1.c重命名为main.c

rename main1.c main.c main1.c

rename支持通配符

?  可替代单个字符
*  可替代多个字符
[charset]  可替代charset集中的任意单个字符

文件夹中有这些文件foo1, ..., foo9, foo10, ..., foo278

如果使用rename foo foo0 foo?，会把foo1到foo9的文件重命名为foo01到foo09，重命名的文件只是有4个字符长度名称的文件，文件名中的foo被替换为foo0。

如果使用rename foo foo0 foo??，foo01到foo99的所有文件都被重命名为foo001到foo099，只重命名5个字符长度名称的文件，文件名中的foo被替换为foo0。

如果使用rename foo foo0 foo*，foo001到foo278的所有文件都被重命名为foo0001到foo0278，所有以foo开头的文件都被重命名。

如果使用rename foo0 foo foo0[2]*，从foo0200到foo0278的所有文件都被重命名为foo200到foo278，文件名中的foo0被替换为foo。

rename支持正则表达式

字母的替换

		rename 's/AA/aa/' *  //把文件名中的AA替换成aa

修改文件的后缀

		rename 's//.html//.php/' *     //把.html 后缀的改成 .php后缀

批量添加文件后缀

		rename 's/$//.txt/' *     //把所有的文件名都以txt结尾

批量删除文件名

		rename 's//.txt//' *      //把所有以.txt结尾的文件名的.txt删掉

-------------

# linux 后台任务，运行，关闭，查看

fg、bg、jobs、&、nohup、ctrl+z、ctrl+c 命令

## &

加在一个命令的最后，可以把这个命令放到后台执行，如

    watch  -n 10 sh  test.sh  &  #每10s在后台执行一次test.sh脚本
## ctrl + z

可以将一个正在前台执行的命令放到后台，并且处于暂停状态。

## jobs

查看当前有多少在后台运行的命令

jobs -l选项可显示所有任务的PID，jobs的状态可以是running, stopped, Terminated。但是如果任务被终止了（kill），shell 从当前的shell环境已知的列表中删除任务的进程标识。

## fg

将后台中的命令调至前台继续运行。如果后台中有多个命令，可以用fg %jobnumber（是命令编号，不是进程号）将选中的命令调出。


## bg

将一个在后台暂停的命令，变成在后台继续执行。如果后台中有多个命令，可以用bg %jobnumber将选中的命令调出。

## kill

法子1：通过jobs命令查看job号（假设为num），然后执行kill %num
法子2：通过ps命令查看job的进程号（PID，假设为pid），然后执行kill pid
前台进程的终止：Ctrl+c

##  nohup

如果让程序始终在后台执行，即使关闭当前的终端也执行（之前的&做不到），这时候需要nohup。该命令可以在你退出帐户/关闭终端之后继续运行相应的进程。关闭中断后，在另一个终端jobs已经无法看到后台跑得程序了，此时利用ps（进程查看命令）

    ps -aux | grep "test.sh"  #a:显示所有程序 u:以用户为主的格式来显示 x:显示所有程序，不以终端机来区分

----------

# linux 多个文件中查找字符串

    find <directory> -type f -name "*.c" | xargs grep "<strings>"

<directory>是你要找的文件夹；如果是当前文件夹可以省略

-type f 意思是只找文件

-name "*.c"  表示只找C语言写的代码，从而避免去查binary；也可以不写，表示找所有文件

<strings>是你要找的某个字符串

----------

# fortune and fortune-zh

每日一首诗

    sudo apt-get install fortune(-zh)
    sudo apt-get purge fortune(-zh)

-------------

# vim 

## 批量缩进

    :3,33>

    3到33行缩进

## 直接粘贴的方式会导致代码丢失和缩进错乱等情况:

解决办法：
vim进入paste模式，命令如下：

    :set paste

进入paste模式之后，再按i进入插入模式，进行复制、粘贴就很正常了。 

命令模式下，输入

    :set nopaste

解除paste模式。

## 基本替换

		:s/str1/str2/ 替换当前行第一个str1为str2
		:s/str1/str2/g 替换当前行所有str1为str2
		:n,$s/str1/str2/ 替换第 n 行开始到最后一行中每一行的第一个str1为str2
		:n,$s/str1/str2/g 替换第 n 行开始到最后一行中每一行所有str1为str2


----------

# sendmail 的安装与配置

https://blog.csdn.net/xin_yu_xin/article/details/45115723

https://blog.csdn.net/xin_yu_xin/article/details/45115723


---------


# 后台任务和进程查看

我们可以让当前任务不再占用终端，去移动到后台了，去挂起或执行了，而仍然可以继续使用终端，继续来敲击命令。

## 先看进程ps –l

第一行的PID是进程id，那PPID则是父进程ID，第二列的S是status状态的意思。

## S，T,R

S：是指sleep睡眠状态，其实计算机的进程有很多时间都是在睡眠的，因为一般情况下，多任务执行是轮流分片执行的，大量的任务是不可能一起去执行的。因为硬件条件有限，一般的就是1个，两个，好些的是四个，8个cpu等等。那么几个根本不会同时执行多个任务

T：是挂起状态，挂起了就停止，在后台什么都不做，和睡眠状态不一样，挂起的话，即使时间片到了也不会被调度，就是什么都不做而干等着。只要不占据终端就能放到后台执行。

 注意：

 Vi编辑器是全屏幕的编辑器，一旦运行，就必须占用终端。

R：是运行状态（running）

其实还有一种状态Z，叫僵尸状态，使用ps –e（查看所有进程状态，而ps默认只看本终端的进程）

东西太多，我们使用管道命令，使用grep命令去查找带Z的行。

    dashuai@ubuntu:~$ ps -el | grep Z  

不过，人品不错，没有发现，其实一般情况下，一些程序员的程序写的不咋滴，就会出现一些僵尸进程出来，就是说一个程序本来已经结束了，但是他还占用着资源不释放！资源没有被回收。这样的进程就是僵尸进程。当然，比较常见的是STR这三个状态

补充：ps –f 完整的命令执行名称查看（full），可以显示完整的命令。

## 进一步看后台任务的例子 

比如sleep命令是睡眠命令，可以在后台运行，不会妨碍终端。

如果在命令后加一个符号&即可让命令在后台执行。

有一个专门查看后台任务的命令，jobs命令查看后台任务

    dashuai@ubuntu:~$ jobs  

发现每个后台任务都有编号（先后顺序编号），还有+和—，可以看作是优先级，+级别最高，什么都没有级别最低。这三个任务都已经完毕。
 

 fg把带+的任务调到前台来执行，我再重新弄几个后台任务

    dashuai@ubuntu:~$ jobs  
     [1]- Running                 sleep 1000&  
     [2]+ Running                 sleep 2000&  

Running是正在后台执行的意思。

fg（front）默认是把带+的任务调到前台，而fg加任务编号是将此任务调到前台来执行

bg（back）把暂停中的的后台任务，放到后台执行起来，同理默认是带+的任务带到后台执行！或者bg指定任务编号，来解除挂起状态。

终止某个当前的任务：一般可以用ctrl+c来终止。但是有些不行，比如vi就不能用ctrl+c来终止，当然也可以明确使用终止命令 kill 进程编号，通过发信号让进程终止

如果想要终止后台任务，也可以加上后台的编号，为了防止误会，加上%

kill %任务编号  终止后台某个正在执行的任务

-----------

# python 发送邮件（４种）

http://blog.51cto.com/lizhenliang/1875330

## 在vpn中，端口25不通,表现为smtplib.connect卡住

    stmp = smtplib.SMTP("smtp.163.com", 25)
    smtp.login('','')

    改为：

    stmp = smtplib.SMTP_SSL("smtp.163.com", 465)
    smtp.login('','')

https://segmentfault.com/q/1010000007661948
https://stackoverflow.com/questions/6979678/python-smtp-errno-10060

# time模块

time模块是包含各方面对时间操作的函数. 尽管这些常常有效但不是所有方法在任意平台中有效. time用struct_time表示时间

    import time
    time.struct_time(tm_year=2015, tm_mon=4, tm_mday=24, 
      tm_hour=14, tm_min=17, tm_sec=26, 
      tm_wday=4, tm_yday=114, tm_isdst=0)
    print time.localtime()
    print time.localtime().tm_year


    time.time(): 返回一个时间戳
    time.asctime([t]): 转换gmtime()和localtime()返回的元组或struct_time为string.
    time.clock(): 在第一次调用的时候, 返回程序运行的时间. 第二次之后返回与之前的间隔.
    time.ctime([secs]): 将时间戳转换为时间字符串, 如没有提供则返回当前的时间字符串,并与asctime(localtime())一样.
    time.gmtime([secs]): 将时间戳转化为, UTC 时区的struct_time.
    time.localtime([secs]): 类似gmtime()但会把他转换成本地时区.
    time.mktime(t): struct_time 转化为时间戳.
    time.sleep(secs): 线程推迟指定时间, 以秒为单位.
    time.strftime(format[,t]): 根据参数转换一个sturc_time或元组为字符串.
    time.strptime(string[, format]): 与strftime相反,返回一个struct_time.

--------

# 5 python中的下划线

**单个下划线(_)

1. 解释器中:交互解释器中最后一次执行语句的返回结果

2. 用作被丢弃的名称

3. ？

**单下划线前缀：

名称私有

**双下划线前缀：

python默认改写__spam为_classname__spam,其中classname是当前类名

**前后都带双下划线的名称：

python中的特殊方法名，惯例，确保python中的名称不会与用户自定义的名称冲突。

[参考](https://segmentfault.com/a/1190000002611411)
