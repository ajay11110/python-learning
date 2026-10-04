# to change global varriale

a= 13 # it is global

def show():
    a =10  # it is local , can not change value of global
    print(a)

print(a)
show()

def show2():
    global a
    a = 10   # it will change now

show2()

print(a) # now a is changed