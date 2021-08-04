'''
def person(firstname,lastlame):
    persons={'first':'firstname','last':'lastlame'}
    return persons
person('w','j')

# 上面的代码 运行不报错 但是没有内容 是因为最基本的print没有
#之前定义的代码的作用就内涵 print 所以没有意识到问题,要输出一定要打印一下哦

def person(firstname,lastlame):
    persons={'first':firstname,'last':lastlame}
    return persons
print(person('w','j'))
'''
#print and reture 是并列的命令类型 当给函数的定义
#没有print 的时侯 必然有其他命令代替 来告诉函数她要做什么
