a = (1,2,'ajay',True) #list can be changed but tuple not list have [] and tuple have ()
print(type(a))

# for tuple of i data use (data,) because (data) considered as direct data only

b=(1,2,3,3,4,5,5,5,'ajay')

c=b.count(5) # count the datatype
print(c)

d=b.index(5) # give the index of first data that match 
print(d)

print(2 in b) # in - return boolean that given data is present or not

print(len(b)) # give length of the tuple