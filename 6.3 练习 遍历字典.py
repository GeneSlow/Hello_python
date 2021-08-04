#vocabulary
voca={'variables':'jiesi ','list':'store'}
'''#这要print根据键的不同添加一系列打印操作 但是偷懒 就写一个作eg
print('variables :'+voca['variables'])

for key,value in voca.items ():
    print(key,':',value,'\n')........1 打印格式1
    print(key+':'+value).............2 打印格式2
#不能直接用 '：' 表达识别不出来 必须加引号转化为字符串
>>> variables : jiesi ...............1
    variables:jiesi   ...............2
    list : store      ...............1
    list:store        ...............2
# 假设键值对 A B ，遍历方式是 A→print 1→print 2→B→print 1→print 2
# 我的错误理解是 A→print 1→B→print 1...

for key,value in voca.items ():
    print(key,':',value,'\n')
print(key+':'+value) 
>>>variables : jiesi  

list : store 

list:store

#很明显 不在for内的print 不会逐项打印 而是顺着计算过程把循环的最后一组键值对打印出来
并且是用的自己的方式
# 一下是我预测的结果 哈哈 完全不合理 没能明白原理 加油

>>>> variables : jiesi  

list : store 

variables:jiesi
list:store

for key,value in voca.items ():
    print(key,':',value) #用，组织的格式
    print(key+':'+value) #用 + 组织的格式
    print('key:'+'value')#......>>>key:value 错的离谱哈 加了引号就非含值变量
    print('key:'+key)    #正确的用法
    print('value:'+value+'\n')

>>> variables : jiesi 
    variables:jiesi 
    key:value
    key:variables
    value:jiesi 

    list : store
    list:store
    key:value
    key:list
    value:store

voca['cars']='bihai'
for key,value in voca.items ():
    print('key:'+key)    #正确的用法
    print('value:'+value+'\n')
'''
#河流  对于values 和 keys 的考察
river={'nile':'egypt','huanghe':'china','mixixibi':'USA'}
'''
for key,value in river.items():
    print('the ',key ,'runs through', value,'.')

for name in river.values():
    print(name)
for rivers in river.keys():
    print(rivers)
'''    
# 调查 检查是否包含在字典中
favo_languages={'nihao':'dhdi','huahu':'hdu8','jiu':'hdhu'}
list=['yew','hdhu','gd']
for a in list:
    if a in favo_languages.values():
        print('thanks for coming!'+a.title())
    else:
        print('Please involved in our exprement.')


