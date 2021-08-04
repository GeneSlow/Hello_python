'''
#熟食店
sandwich_orders=['tuna','dumpling','bacon','egg']
finished_sandwiches=[]
while sandwich_orders:
   print('Imade you a '+sandwich_orders+'sandwich.')   ...又来了 总是类型不一样 但不是根本问题
    print('Imade you a '+sandwich_orders+'sandwich.')
    finished_sandwiches=sandwich_orders.pop()          ...必须把pop提前 这样才能一个一个变量的print
                                                          而且不能直接放到完成列表里面 要先赋给变量
print(finished_sandwiches)

#concatenate英 /kən'kætɪneɪt/ v. 连接，连结，使连锁
#TypeError: can only concatenate str (not "list") to str
#以上完全不对 列表怎么能直接用呢 提取变量啊

sandwich_orders=['tuna','dumpling','bacon','egg']
finished_sandwiches=[]
while sandwich_orders:
    finished=sandwich_orders.pop()
    print('I made you a '+finished+' sandwich.')
    finished_sandwiches.append(finished)
print(finished_sandwiches)
>>> I made you a egg sandwich.
    I made you a bacon sandwich.
    I made you a dumpling sandwich.
    I made you a tuna sandwich.
    ['egg', 'bacon', 'dumpling', 'tuna']

#五香烟熏牛肉
sandwich_orders=['tuna','dumpling','bacon','egg','pastrami','pastrami','pastrami']
finished_sandwiches=[]
if 'pastrami' in sandwich_orders:
    print('iam sorry we have no pastrami')
    while sandwich_orders:
        sandwich_orders.remove('pastrami')
        if "pastrami" not in sandwich_orders:
            finished_sandwiches=sandwich_orders
            print(finished_sandwiches)
            break
'''
#dream holiday
answer={}

active=True
while active:
    tips=('where would you like to go if you have a vacation?: ')
    tips+=('(if you wanna stop,pls input "quit")')
    name=input('please give me your name: ')
    if name =='quit':
        active=False
    else:
        question=input(tips)
#储存进字典的语法 字典名[键]=值
        if question =='quit':
            active=False
        else:
         answer[name]=question

#展示结果
for name,question in answer.items():
    print(name.title()+' would like to go '+question.upper()+' if the time is suitable.')
    print('And we will go toghter oneday!')
          
        
