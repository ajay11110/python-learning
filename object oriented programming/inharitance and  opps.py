# taking properties of a class to another 

class date:
    data = 1
    month = "jan"

    def show(self) :
        print(f"date is {self.data} {self.month} ")

class moment: # here we are using same data of date class
    data = 3
    month = "march"

    def show(self) :
        print(f"date is {self.data} {self.month} ")

a= date()
b= moment()

a.show()
b.show()

#=================== here is a problem in it , if we have to change something then  have to change everywhere so better approch

#============= inheritance


class pal:
    data = 1
    month = "jan" # ================ base class

    def show(self) :
        print(f"date is {self.data} {self.month} ")

class pal2(pal): # now we can use all things of pal in pal2
    data = 5    #=========== inheritade class


c= pal()
d= pal2()

c.show()
d.show()

#====================== multiple class can be passed
#====================== nested also passing class 1 -> class 2 -> class 3 ........


# in nested we can use only upper class and on run _init it will run only the class that is called but to use _init of parent class to use --

class data1:
    ajay = 1
    lan = "python"

    def __init__(self):
        print("it is data1")

    def show(self):
        print(f"value is {self.ajay} and lan is {self.lan}")

class data2(data1):
    ajay = 2

    def __init__(self):
        super().__init__() #================ it is important
        print("it is data2")


class data3(data2):
    ajay = 7

    def __init__(self):
        super().__init__()
        print("it is data3")


e= data1()
f= data2()
g= data3() # print init of all upper to it also


    