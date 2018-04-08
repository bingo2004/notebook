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

## 基本替换

		:s/str1/str2/ 替换当前行第一个str1为str2
		:s/str1/str2/g 替换当前行所有str1为str2
		:n,$s/str1/str2/ 替换第 n 行开始到最后一行中每一行的第一个str1为str2
		:n,$s/str1/str2/g 替换第 n 行开始到最后一行中每一行所有str1为str2


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
