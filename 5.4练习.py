#练习 5.4
'''
names=['kuier','tyue','huaer','wj','admin']

for name in names:
    print('Hello, '+ name )

for name in names:
    if name=='admin':
        print('Hello,admin,nishizhu ma ' )
    else:
        print('wa you are not admin. thats awsome!')

names=[]
if names:
    for name in names:
        print('Hello,admin,nishizhu ma ' )
else:
    print('we need more users')

current_users=['kuier','tyue','huaer','wj','admin']
new_users=['kuier','Tyue','nihao']
for a in new_users:
    if a.lower() in current_users:
        print('you need to change a name')
    else:
        print(a+' is ok')

current_users=['kuier','tyue','huaer','wj','admin']
new_users=['kuier','Tyue','nihao']
for a in new_users:
    if a in current_users:
        print('you need to change a name')
    else:
        print(a+' is ok')
'''
# 序数
num=['1','2','3','4','5','6','7','8','9']
for a in num:
    if a=='1':
        print(a+'st')
    elif a=='2':
        print(a+'nd')
    elif a=='3':
        print(a+'rd')
    else:
        print(a+'th')
