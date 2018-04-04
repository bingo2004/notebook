


# 自动启动ss

shadowsocks.json文件放在/etc目录下

在/etc/rc.local中添加如下命令，注意在exit 0之前。

    sudo sslocal -c /etc/shadowsocks.json

# SSH连接远程服务器

##远程连接

    #!/bin/bash
    ssh -o StrictHostKeyChecking=no root@144.202.41.67

##上传本地到服务器

    scp /path/filename username@servername:/path/
    scp -r /path/local_dir username@servername:path/remote_dir
    
##从服务器下载到本地

    scp username@servername:/path/filename /path/
    scp -r username@servername:/path/remote_dir /path/local_dir
    
#tar压缩与解压缩

* -c 建立压缩文档
* -x 解压
* -z 有gzip属性
* -v 显示所有过程
* -f 最后一个，接文件档案名字

例如：

    tar -czf file.tar.gz *.jpg
    tar -xzf file.tar
    
#安装 Privoxy

    sudo apt-get install privoxy -y

###修改配置文件

    sudo cp /etc/privoxy/config /etc/privoxy/config.bak
    sudo vim /etc/privoxy/config

找到 listen-address 确保有这行代码 listen-address 127.0.0.1:8118
*如果失败，尝试去掉这一行，在办公室机器就是去掉这一行之后成功的

找到 forward-socks5 确保有这行代码(没有自己加) forward-socks5 / 127.0.0.1:1080 .
*注释掉这一行后，可以恢复非privoxy连接

###启动

    sudo service privoxy start
    sudo service privoxy status

###配置转发

    sudo vim ~/.bashrc

在最后添加如下代码：

    export http_proxy="http://127.0.0.1:8118"
    export https_proxy="http://127.0.0.1:8118"

###重载配置

    source ~/.bashrc
    
###测试

    wget http://www.google.com
    
--2018-04-01 11:23:21--  http://www.google.com/
正在连接 127.0.0.1:8118... 已连接。
已发出 Proxy 请求，正在等待回应... 200 OK
