class employee :
    salary = 0
    lan= "python"

    def __init__(self):    # dunder method whioch is automatically called
        print("it will run without call")

raj = employee()
raj.name = "Raj"
print(raj.name, raj.lan, raj.salary)  


class employeedata :
    salary = 0
    lan= "python"

    def __init__(self , name, salary, lan): # acceptting and updating
        self.name = name
        self.salary = salary
        self.lan = lan
         

raj2 = employeedata("ajay", 0, "js") # we can pass atributes 
print(raj2.name, raj2.lan, raj2.salary)  

