''
#members of having lunch
#关于有默认值的属性
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):# definition of attributes
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describle_restaurant(self):        # definition of function of appraoch 
        print('The restaurant"s name is '+ self.restaurant_name+' .')
        print('The restautant"s flavor is '+ self.cuisine_type+'.')

    def open_restaurant(self):             # definition of function of appraoch 
        print('The restaurant is opening.')

    def red_num_served(self):
        print('The number of customers is: '+ str(self.number_served))

    def set_number_served(self,number):
        self.number_served=number

    def increment_number_served(self,increment):
        self.number_served=self.number_served+increment
        

restaurant=Restaurant('new_moon','taliand')#调用默认值 必须是有完整属性的实例 所以其他属性不能是空白 能够构成实例
#restaurant.red_num_served()
'''
#修改属性方法1:
restaurant.number_served=12
restaurant.red_num_served ()

#fixing the attributes 2
restaurant.set_number_served(12)
restaurant.increment_number_served(13)
restaurant.red_num_served()

restaurant.increment_number_served(13)
restaurant.red_num_served()
'''
#login times
class User():

    def __init__(self,first_name,last_name,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=login_attempts

    def describe_user(self):
        print('The user"s name is '+ self.first_name+' '+self.last_name+' .')

    def greet_user(self):
        print('Hello, '+self.first_name+' '+self.last_name+' .')

    def increment_login_attempts(self):
        increment=1
        self.login_attempts += increment
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts='0'
        print(self.login_attempts)
        
user=User('wang','jing',2)
user.increment_login_attempts()
user.reset_login_attempts()
