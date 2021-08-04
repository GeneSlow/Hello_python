'''  #关于标志和break#
prompt=('nishiyizhizhu')
prompt+=('\nnihsaihsiyizhizhu')

active=True
while active:
    mess=input(prompt)

#   if mess ==quit:      ...1  ....×
    if mess =='quit':    ...2  ....√
        active=False
#       beak             ...3  ....√
    else:
        print(mess+'\n')
#反复失败 和书上的对比发现 欸 又是类型问题 quit× ;  'quit'√
'''
