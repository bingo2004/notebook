#服务器上NginX部署flask应用

这部分内容网上讲解的很多，很多人的博客中都有介绍，但是在参考的过程中也遇到了很多问题。终于在参考了一些前人的经验成功部署，给自己做一个记录。

主要参考文章：

+ [Serving Flask with Nginx](https://vladikk.com/2013/09/12/serving-flask-with-nginx-on-ubuntu/)
+ [阿里云部署Flask+WSGI+Nginx详解](https://www.cnblogs.com/Ray-liang/p/4173923.html)
+ [Flask+uwsgi+Nginx部署应用](https://www.jianshu.com/p/84978157c785)


本文涉及到的内容包括：Nginx、uWSGI、flask框架

##前提

```
   sudo apt-get install pip
   sudo pip install virtualenv
   virturalenv venv
   source venv/bin/active
   pip install flask
   pip install uwsgi
```

##Nginx安装

Ubuntu中apt-get安装Nginx，首先添加repositories

`sudo add-apt-repository ppa:nginx/stable`

注：如果 “add-apt-repository” 命令不存在，需要首先安装 “software-properties-common” 包: sudo apt-get install software-properties-common

更新升级包：

`sudo apt-get update && sudo apt-get upgrade`

安装并启动 Nginx:

```
sudo apt-get install nginx
sudo /etc/init.d/nginx start
```


##uWSGI安装

```
sudo apt-get install build-essential python python-dev
pip install uwsgi
```

##配置

flask框架里面利用manager.py启动文件，下面是manager.py

```
#!/usr/bin/env python
import os

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app
from flask.ext.script import Manager, Shell

# 通过配置创建 app 
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def deploy():
    """Run deployment tasks."""
    pass


if __name__ == '__main__':
    manager.run()
```



##配置Nginx

删除默认设置
`sudo rm /etc/nginx/sites-enabled/default`

在/etc/nginx/conf目录中添加config_nginx.conf
```

server {
	listen 80;
	server_name localhost;
	
	location / {
		include uwsgi_params;
		uwsgi_pass	127.0.0.1:8001;
		uwsgi_param	UWSGI_PYHOME /home/bingo/git/flasky/venv
		uwsgi_param	UWSGI_CHDIR /home/bingo/git/flasky
		uwsgi_param	UWSGI_SCRIPT manager:app;
	}
}
```

#配置uWSGI
config_uwsgi.ini文件：

```
[uwsgi]
socket = 127.0.0.1:8001 
chdir = /home/bingo/git/flasky
master = True
home = /home/bingo/git/flasky/venv
wsgi-file = manager.py
callable = app
processes = 4
threads = 2
buffer-size = 32768
stats = 127.0.0.1:9191
```

#安装配置supervisor

使用supervisor引导uWSGI。安装：

`sudo apt-get install supervisor`

supervisor的全局配置文件在/etc/supervisor/supervisor.conf中，一般不改动，新建一个文件flask_supervisor.conf放在/etc/supervisor/conf.d目录下:

```
[program:blog] 
# 启动命令入口 
command=/home/bingo/git/flasky/venv/bin/uwsgi /home/bingo/git/flasky/config_uwsgi.ini            
# 命令程序所在目录 
directory=/home/bingo/git/flasky
#运行命令的用户名 
user=bingo
autostart=true
autorestart=true
#日志地址 
stdout_logfile=/home/bingo/git/flasky/logs/uwsgi_supervisor.log
```
启动supervisor服务：sudo service supervisor start

