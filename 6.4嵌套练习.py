#dictionnary in list
#人  宠物的信息打印
'''
people1={'height':'tall','weight':'hesvey'}
people2={'height':'medium','weight':'light'}

people=[people1,people2]

for peo in people:
    print(peo)

Downtown={'Attributes':'dog','master':'WJ'}
Grey={'Attributes':'cat','master':'WW'}
#pets=['Downtown','Grey']    #又把变量处理成了字符串
pets=[Downtown,Grey]
for pet in pets:
    print(pet)
    
#喜欢的地方
#把列表放进字典里面
fav_place={'gene':'iceislend','iris':['nihon,tokyo,china'],'Nicho':['sichuan,xizang']}
for name,place in fav_place.items():
    print('Name:'+name.title())
    #print(place+'\n')  ...2....运行错误  + 一定要注意拼接运算符两侧的元素类型一样
    #print(place)       ...1.....没问题 
    print(str(place)+'\n')......3

>>> Name:Gene
    iceislend
    Name:Iris
    ['nihon,tokyo,china']
    Name:Nicho
    ['sichuan,xizang']            .........1

>>> Name:Gene
    iceislend

    Name:Iris
    Traceback (most recent call last):
      File "D:/MERCHINE LEARNING/6.4嵌套练习.py", line 24, in <module>
        print(place+'\n')
    TypeError: can only concatenate list (not "str") to list       ..........2

>>> Name:Gene
    iceislend

    Name:Iris
    ['nihon,tokyo,china']

    Name:Nicho
    ['sichuan,xizang']           ...........3

#喜欢数字
dic={'huahua':[5,9],'hshs':[69,9],'ggug':[7,88]}
print(dic['huahua'])
print(dic)

>>> [5, 9]
    {'huahua': [5, 9], 'hshs': [69, 9], 'ggug': [7, 88]}
'''
