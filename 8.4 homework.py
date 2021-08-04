'''
#magicians
def show_magician(name):
    for a in name:
        print(a)

magicians_name=['iris','jack','jimmy']
show_magician(magicians_name)
'''
#excellent magicians

        
def make_great(name):
    y=[]
    while name:
        a="Great"+name.pop()
        y.append(a)
        name=y
    
def show_magician(name):
    print(name)        

magicians_name=['iris','jack','jimmy']
make_great(magicians_name)
show_magician(magicians_name)
