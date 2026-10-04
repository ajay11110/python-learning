# nhi sanajh aaya but

# if we want to do some opretions then use it

class data:
   salary = 10000000
   increament = 20

   @property
   def afterIncreament(self):
      return (self.salary + (self.salary * self.increament)/100)
   
a=data()
print(F"salary after increament is {a.afterIncreament}") # able to use like varriable as i use @property