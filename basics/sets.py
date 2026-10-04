# sets are same as maths sets

empty=set() #method to make empty set

s={1,2,3,4, "ajay"} 

#elements do not repeat in set and do not maintain order
s1 ={1,2,3,4,4,4,5,6} # 4 will considerred only 1 time 
print(s1)

s.add(1234) #like append
print(s)

print(len(s)) #print length

s.remove(1) #remove given item
print(s)

s.pop() # remove any rendom number

s3 = {1,22,3,3,4,54,56,5}
s3.clear() # make set empty
print(s3)

s4=s1.union(s) #make union
print(s4)

s5=s1.intersection(s) #make union
print(s5)
