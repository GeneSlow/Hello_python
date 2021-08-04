'''
#sandwich
def food(*integrets):
    for integret in integrets:
        print('the list including:'+ '\n-'+integret)

food('rainbow','flours')
>>>                       ......表达1
    the list including:
        -rainbow
    the list including:
    -flours

#sandwich
def food(*integrets):
    print('the list including:')
    for integret in integrets:
        print('\n-'+integret)

food('rainbow','flours
>>>                    ........表达2
    the list including:

    -rainbow

    -flours
#这样表达更好

# 用户简介
def user_profile(last,first,**person_infor):
    dic={}
    dic['first_name']=first
    dic['last_name']=last
    for key,value in person_infor.items():
        dic[key]=value
    return dic
#一下两种都可以:
#dicts=user_profile('wang','jing',height='163',weight='120')
#print(dicts)                          .............................1
#print(user_profile('wang','jing',height='163',weight='120')).......2

user_profile('wang','jing',height='163',weight='120') ......这里键值对的实参的表达是用的等号
print(user_profile)]
#这个表示方法是错的 但是为啥错 我也讲不清楚 难受呀
总的来说 函数本来就是给变量调用的 之前直接用可能是定义中有print
=================== RESTART: D:/MERCHINE LEARNING/8.5.py ==================
<function user_profile at 0x00000155C6ED3940>
'''
#汽车
def make_car(manufacturer,type,**car_features):
    dic={}
    dic['manufacturer']=manufacturer
    dic['type']=type
    for key,value in car_features.items():
        dic[key]=value
    return dic
#car=make_car('BMW','suv','color'='red','assemble'='tyre')表达错误后年的键不要加引号
                                             #说不清为哈 难受
car=make_car('BMW','suv',color='red',assemble='tyre')
print(car)

