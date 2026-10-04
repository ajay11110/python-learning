class data:
    day = 23
    month = 12

    def show(self):
        print(f"day is {self.day}")

    @classmethod   #it will prevent to chnage and will use original class atribute
    def show2(cls):
        print(f"month is {cls.month}")

a = data()
a.day   = 25 
a.month = 2 
a.show()  # able to change
a.show2()  # unable to change
