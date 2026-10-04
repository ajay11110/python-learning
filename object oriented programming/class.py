# blueprint for objects

class employee :
    salary = 0
    lan= "python"

raj = employee()
raj.name = "Raj"
print(raj.name, raj.lan, raj.salary)  # here salary and lan are class atributes and name is objec/instance atribute

maya = employee()
maya.name = "maya"
maya.lan = "javascript" # instance atributes take spreference over class atributes
print(maya.name, maya.lan, maya.salary)



# we can also define the function in a class

class data:
    dataNo = 24
    batch = "arftgc"

    def getdata(self):  # we have to give an atribute without it there will be an error
        print(f"data number is {self.dataNo} and batch if {self.batch}")

     # if we do not want pass pass the object to the function the use @staticmethod
    @staticmethod
    def greet():
        print("hello user")

data2 = data()

data2.getdata() # it will converted into data.getdata(data2) thats why self atribute was given in function