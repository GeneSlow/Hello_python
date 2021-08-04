'''
#外星人的颜色
alien_colour=['green','yellow','red']
victim='red'

if victim in alien_colour[0]:
    print('Congradulations!You win 5 points.')

victim='red'
if victim in alien_colour[0]:
    print('Congradulations!You win 5 points.')
else:
    print()

victim='red'
if victim not in alien_colour[0]:
    print()

victim='red'
if victim in alien_colour[0]:
    print('Congradulations!You win 5 points cause you killed that alien.')
else:
    print('Congradulations!You win 10 points.')

if victim in alien_colour[0]:
    print('Congradulations!You win 5 points.')
elif victim in alien_colour[1]:
    print('Congradulations!You win 10 points.')
else:
    print('Congradulations!You win 15 points.')
#人生的不同阶段
age=2
if age<2:
    print('he is an infant')
elif 2<=age<4:
    print('he is a walking-learner')
elif 4<=age<13:
    print('he is a child')
'''
my_favotite=['apple','oranges','watermelon']
fruits='oranges'
if fruits in my_favotite:
    print('you really liake '+fruits+' !')
