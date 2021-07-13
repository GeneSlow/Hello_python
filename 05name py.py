Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name='gene snow'
>>> print(name.title())
Gene Snow
>>> '''将字符串 gene snow 储存在变量name中
       title()是方法 方法在python可对数据执行的操作
       (.)是为了让python对变量 name 执行 方法title()指定的操作
       title()的括号是每个方法 bracket pair后面需要的额外的限制信息
       函数title dont need the other message,so it is a blank bracket
'''
'将字符串 gene snow 储存在变量name中\n       title()是方法 方法在python可对数据执行的操作\n       (.)是为了让python对变量 name 执行 方法title()指定的操作\n       title()的括号是每个方法 bracket pair后面需要的额外的限制信息\n       函数title dont need the other message,so it is a blank bracket\n'
>>> 
>>> print(name.upper())
GENE SNOW
>>> print(name.lower())
gene snow
>>> #拼接信息
>>> first_name='gene'
>>> last_name='snow'
>>> full_name=first_name+' '+last_name
>>> print('hello'+full_name+"!")
hellogene snow!
>>> print('hello,'+full_name+'!')
hello,gene snow!
>>> print('Hello,'+full_name.title()+'!')
Hello,Gene Snow!
>>> #增加一个full_name的变量 简化python 的语言
>>> message='Hello,'+full_name.title()+'!'
>>> print(message)
Hello,Gene Snow!
>>> #将信息储存在变量 message 中 进一步简化python 语句
