'''
age=13
if age<10:
    price=0
elif age == 10:
    price=10
else:
    price=20
    
print('Hello,dear customer,your price of a ticket is '+'price'+'yuan.' )
>>> Hello,dear customer,your price of a ticket is priceyuan.
# 第一个问题在于冒号 第二个问提在与等号 用双等号

# 实验证明 ‘’无法直接把变量转换成字符串 还是需要用str
print('Hello,dear a, yourjjjj is '+str(price)+' yuan.')
'''
# 实验2 将price的值直接变成字符串
age=13
if age<10:
    price='0'
elif age == 10:
    price='10'
else:
    price='20'
print('Hello,dear a, yourjjjj is '+price+' yuan.')
# 结果表明 我们成功啦！
