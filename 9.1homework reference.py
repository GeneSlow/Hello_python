'''
#Restaurant
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):# definition of attributes
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describle_restaurant(self):        # definition of function of appraoch 
        print('The restaurant"s name is '+ self.restaurant_name+' .')
        print('The restautant"s flavor is '+ self.cuisine_type+'.')

    def open_restaurant(self):             # definition of function of appraoch 
        print('The restaurant is opening.')

restaurant=Restaurant('new_moon','taliand')

print(restaurant.restaurant_name) #目前不太能理解 这样调用的话不是非得知道通用
                                  #属性的具体命名吗???
restaurant.open_restaurant()
restaurant.describle_restaurant()
print('\n')
#describle_restaurant()           #暂时理解为方法必须  要基于变量
#就是说创建类的时候 通用属性和方法的名称是 是共识的
a=('niao ','niahao ')
print (a)

#3Restaurant
restaurant=Restaurant('new_moom','Tailand')
restaurant.describle_restaurant()
restaurant=Restaurant('Beijing','Chinese')
restaurant.describle_restaurant()
restaurant=Restaurant('huaqioa','usa')
restaurant.describle_restaurant()
'''
#User
class User():

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def describe_user(self):
        print('The user"s name is '+ self.first_name+' '+self.last_name+' .')

    def greet_user(self):
        print('Hello, '+self.first_name+' '+self.last_name+' .')

user=User('wang','jing')
print(user.first_name)
print(user.last_name)

user.describe_user ()
user.greet_user()

>>> wang
    jing
    The user"s name is wang jing .
    Hello, wang jing .
