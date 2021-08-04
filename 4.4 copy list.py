my_favorite=['a','c','v']
friend_favorite=my_favorite[:]
print(my_favorite)
print(friend_favorite)
#副本 创建成功

my_favorite.append('u')
friend_favorite.append('o')
print(my_favorite)
print(friend_favorite)
# 分别添加新元素

#练习 4-11
for h in friend_favorite:
    print(h)
for j in my_favorite:
    print(j)
