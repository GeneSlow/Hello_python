#4.3动手试一试 打印数字1~20
a=[a for a in range(1,21)]
print(a)
#或者for n in range(1,21): print(n)
a=list(range(1,1000001))
print(min(a))
print(max(a))
print(sum(a))

a=[]
for values in range(1,20,2):
    a.append(values)
print(a)

