# python 发送邮件（４种）

http://blog.51cto.com/lizhenliang/1875330

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
