i=1

while(i<6):
    print(i)
    i+=1

    # =============== for loop syntax is changed here

    for j in range(4) : # range function can be written as range(end)- range(0,end)                  
        print(j)        # original syntax 0 range(start, end, step) if interval not given - 1

# printing list using for
l = ['ajay', False, 3.14, 202]

for k in l :
    print(k)

    #============= advance-> for-else - very useful if we use break statement in for loop because on braek else will not run

l1= ['ajay', 1 ,3, 5, 7 ,90 ]

for m in l1:
    print(m)

else:
    print("this msg will print after the end of for loop")


    # break - exit the loop now
    #continue - skip this iteration

#================= new keyword- pass  , means do nothing

for m in l1 :
    pass         # it will work without  doing nothing and do not give error