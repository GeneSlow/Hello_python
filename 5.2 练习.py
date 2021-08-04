'''
car='d'
print("is car=='d'?I predict Ture.")
print(car=="d")

print("\nis car=='f'?I predict False.")
print(car=="f")
#1
answer=1
print('\n')
a=str(answer==1)+' '
print(a*5)

answer=2
print('\n')
a=str(answer==1)+' '
print(a*5)

a=3+2
b=3+5
c=['9','8','5']
d=[1,2,5]
if a==b:
    print('yeh')
else:
    print('opps!')
 #第二种判断方法

print(a==b)
print(a<=b)
print(a>=b)

if a in c and a in d:
    print(a)
else:
    print(c)
#即将检查是否是int 和 str 的问题

>>>opps!
False
True
False
['9', '8', '5']
'''
a=3+2
b=3+5
c=[9,8,5]
d=[1,2,5]
print(a in c and a in d)
print(b in c or a in d)

'''
if a in c and a in d:
    print(a)
else:
    print(c)
>>>5
#哈哈哈哈 超级开心 自己解决自己的问题 就是字符串和整数是不相等的啊 千万注意表达
'''
print(a in c)
print(a not in c)
