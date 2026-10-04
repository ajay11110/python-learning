try:
    a= int(input("enter a number : "))
    print(a)

except Exception  as e: # if above block give any error then this will run and forward program will also run
    print(e)

except ValueError as v:  # if want to find special error
    print(v)
    print("please enter number only")


print("thank you")



# +================== more advance

try:
    a= int(input("enter a number : "))
    print(a)

except Exception  as e: # if above block give any error then this will run and forward program will also run
    print(e)

else:
    print("thank you")   # it will run only when try will success

#=============== finally it will always run for both cases 
# best use in function if we return in both cases even then finally will run

try:
    a= int(input("enter a number : "))
    print(a)

except Exception  as e: 
    print(e)

finally:
    print("thank you")   # it will always run 








