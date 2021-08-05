'''
# Icecreamstand
#创建子类 赋予新的属性和方法
class Restaurant():

    def __init__(self,name,style):
        self.name=name
        self.style=style

    def describle_restaurant(self):
        print('The name of the restaurant is '+ self.name.title()+' .')

    def definition(self):
        print('The flavor of it is '+self.style+' .')


restaurant=Restaurant('new_moom','Chinese')
restaurant.definition()

class Icecream(Restaurant):

    def __init__(self,name,style):
        super().__init__(name,style)
        self.flavor=['herb','choclate']

    def display_flavors(self):
        print(self.flavor)

icecream=Icecream('moonnight','black')
icecream.display_flavors()

#Admini
from mending_attributes import User
  
class Admini(User):

    def __init__(self,first_name,last_name,login_attempts):
        super().__init__(first_name,last_name,login_attempts)
        self.privilleges=['can add pos','can delete post','can ban user']

    def show_privilleges(self):
        print('The privilleges including: \n')
        for h in self.privilleges:
            print('- '+ h +'\n')

admin=Admini('wng','jng',6)
admin.show_privilleges()


有个很奇怪的问题不能理解  一下为第一遍run的代码
>>>
The privilleges including: 

- can add pos

- can delete post

- can ban user

>>>    一下是第二遍运行的代码 问题在于 第一行后面总是多出来一个空行 啊啊啊 抓狂了 完全没有修改只是再次运行
The privilleges including: 


- can add pos

- can delete post

- can ban user

#privilleges
#将实例用作属性
from mending_attributes import User
  
class Privilleges():
    def __init__(self,privilleges):
        self.privilleges=['can add pos','can delete post','can ban user']

    def show_privilleges(self):
        print('The privilleges including: \n')
        for h in self.privilleges:
            print('- '+ h +'\n')
                             #.......将要作为属性的这一部分类先于上一级类安排好 之后再将类作为属性写进上一级代码里面
class Admini(User):

    def __init__(self,first_name,last_name,login_attempts):
        super().__init__(first_name,last_name,login_attempts)
        self.privillege=Privilleges()

#在主程序中这个用做属性的实例不会出现 但是会出现 上一级中相关的属性名称
admi=Admini('wang','jing',0)
admi.privillege.show_privilleges()

>>>Traceback (most recent call last):
  File "D:\MERCHINE LEARNING\9.3 son icecreamstand.py", line 112, in <module>
    admi=Admini('wang','jing',0)
  File "D:\MERCHINE LEARNING\9.3 son icecreamstand.py", line 99, in __init__
    self.privillege=Privilleges()
TypeError: __init__() missing 1 required positional argument: 'privilleges'

#看了很久才明白这个 为啥说没给'privilleges'的值 是因为 底下给的是一个列表 这就相当于默认值 不能在给出形参 'privilleges'
#所以报错了
'''
from mending_attributes import User
  
class Privilleges():
    def __init__(self):
        self.privilleges=['can add pos','can delete post','can ban user']

    def show_privilleges(self):
        print('The privilleges including: \n')
        for h in self.privilleges:
            print('- '+ h +'\n')
                             #.......将要作为属性的这一部分类先于上一级类安排好 之后再将类作为属性写进上一级代码里面
class Admini(User):

    def __init__(self,first_name,last_name,login_attempts):
        super().__init__(first_name,last_name,login_attempts)
        self.privillege=Privilleges()

admi=Admini('wang','jing',0)
admi.privillege.show_privilleges()

#upgrate battery
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
 
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
 
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
 
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
 
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery(): 
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):

        """初始化电瓶的属性""" 
        self.battery_size = battery_size
    
    def describe_battery(self): 
        """打印一条描述电瓶容量的消息""" 
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self): 
        """打印一条消息，指出电瓶的续航里程""" 
        if self.battery_size == 70: 
            range = 240 
        elif self.battery_size == 85: 
            range = 270 
 
        message = "This car can go approximately " + str(range) 
        message += " miles on a full charge." 
        print(message)

    def upgrate_battery(self):
        '''检查电瓶容量'''
        if self.battery_size !=85:
            self.battery_size=85
        
class ElectricCar(Car): 
    """Represent aspects of a car, specific to electric vehicles.""" 
    def __init__(self, make, model, year): 
        """ 电动汽车的独特之处 初始化父类的属性，再初始化电动汽车特有的属性""" 
        super().__init__(make, model, year) 
        self.battery = Battery()

e_car=ElectricCar('an','x86','2019')
e_car.battery.get_range()
'''对电瓶进行升级'''
e_car.battery.upgrate_battery()
e_car.battery.get_range()
