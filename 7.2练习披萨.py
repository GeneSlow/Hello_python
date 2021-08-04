
'''
#pizza
pizza=('please show me the ingredient:')
pizza+=('\nWhen you finished please input quit.')
x=''              #....................一定要先定义元素以进入循环

if sl=='quit':
    break
else:
    for sl:
        print('Ok,we will add it!')

for sele in sl:
    if sele =='quit':
        break
    else:
        print('Ok,we will add it!')
        
 #尝试一次输入所有配料 然后挨个输出   失败
 
while sl=='quit':
    break
else:
    for sle in sl:
        print('Ok,we will add '+sle+'!')

while x != 'quit':
    x=input(pizza)
    if x!='quit':
        print('Ok,we will add it!')
        
#自己写的时候 才发现if 和 while 用的是同一个判断条件 但是 x 的值
#        已经发生变化   
# is similar with if the variable should be defined advanced
>>> please show me the ingredient:
    When you finished please input quit.mushrooms
    Ok,we will add it!
    please show me the ingredient:
    When you finished please input quit.eggs
    Ok,we will add it!
    please show me the ingredient:
    When you finished please input quit.quit

#电影票
quesion=('how old are you?')
age=''
while age=='':
    age=input(quesion)
    if age <3:
        print('Its free for you')
    elif 3<=age<12:
        print('the price is 10')
    elif age>= 12:
        print('the price is 15')

>>>how old are you?12
    Traceback (most recent call last):
      File "D:/MERCHINE LEARNING/7.2 练习 披萨.py", line 50, in <module>
        if age <3:
    TypeError: '<' not supported between instances of 'str' and 'int'

quesion=('how old are you?')
age=''
while age=='':
    age=input(quesion)
    age=int(age)             # .............turn age to integer
    if age <3:
        print('Its free for you')
    elif 3<=age<12:
        print('the price is 10')
    elif age>= 12:
        print('the price is 15')

#三个出口
quesion=('how old are you?')
active= True
while active:
    age=input(quesion)
    if age!= 'quit':
        age=int(age)
        if age <3:
            print('Its free for you')
        elif 3<=age<12:
            print('the price is 10')
        elif age>= 12:
            print('the price is 15')
    elif age=="quit":
# 1       break
# 2       active=False
# 3       print('Stop here')
# 真的可以这么搞 通过制表符区分结构 nice  
'''
#无限循环
senense=('u a beauiful,是吗')
senense+=(' \n( 请输入"是")')
s=input(senense)
while s=='是':
    print('you are definitely A beautiful pig')
    
   
