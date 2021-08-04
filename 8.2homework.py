'''
#t-shirt
def make_shirt(sixe,font):
    #use to get size and style of Tshirt
    print('This is a '+sixe+' shirt with '+ font+'.')
make_shirt('xxl','zhuzhuxia')
make_shirt(font='zhuzhuxia',sixe='xxl')
================= RESTART: D:/MERCHINE LEARNING/8.2homework.py =================
This is a xxl shirt with zhuzhuxia.
This is a xxl shirt with zhuzhuxia.

#oversize Tshirt
def make_shirt(sixe,font='I love python.'):
    print('This is a '+sixe+' shirt with '+ font+'.')

make_shirt('xxl')
make_shirt(sixe='xl')
'''
#city
def descraible_city(name,location='China'):
    #know the location of one place
    print(name +' is in '+ location+'.')
descraible_city('Yantai')
descraible_city('Anhui')
descraible_city('Xian','Britain')
