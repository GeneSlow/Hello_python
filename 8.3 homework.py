'''
#城市名

def city_country(sity,kountry):
    print(sity +','+kountry)
city_country('XI','china')

#album
def make_album(singer,album,price=''):
    if price:
        dic={'singer_name':singer,'album_name':album,'price_':price}
    else:
        dic={'singer_name':singer,'album_name':album}
    return dic
#album=make_album('huahua','niyoahuaozhe')

#>>>{'singer_name': 'huahua', 'album_name': 'niyoahuaozhe'}

album=make_album('huahua','niyoahuaozhe',30)
print(album)

>>>{'singer_name': 'huahua', 'album_name': 'niyoahuaozhe', 'price_': 30}
'''
#用户的专辑
def make_album(singer,album,price=''):
    if price:
        dic={'singer_name':singer,'album_name':album,'price_':price}
    else:
        dic={'singer_name':singer,'album_name':album}
    return dic

while True:
    print('Show me your favorite singer and album')
    print('(If you wanna stop ple press "q")')
    singer=input('Singer:')
    if singer=='q':
        break
    album=input('Album:')
    if album=='q':
        break
print(make_album(singer,album))
