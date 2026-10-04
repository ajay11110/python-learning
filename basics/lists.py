# it is like array but csn contain multiple datatypes in it.
# changeable and flexible

l = ['ajay','python',.7,3.17]
print(l)
print(l[1])

l.append("last word") # add element at last
print(l) #list will change

l2 =[1,3,5,674,3,23,4]
l2.sort()  #sort the numbers in increasing order
print(l2)

l2.reverse() #reverse the list
print(l2)

l2.insert(2,"data is inserted at index 2")
print(l2)

deleted= l2.pop(1) #delete the data at given index and return it
print(l2)
print(deleted)

l.remove("last word")  #delete the given data
print(l2)