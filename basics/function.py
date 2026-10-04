# function defination
def hello():
    print("hello python !")

hello() # function call

def hello2(name):
    print(f"hello python ! from {name}")

hello2("ajay") # function call

def hello3(name,ending = "task done"): # here task done is default value , it will use when no parameter is given
    print(f"hello python ! from {name}")
    print(ending)

hello3("ajay") # it will use the default value of ending
hello3("ajay", "done") # it will use the given value for ending