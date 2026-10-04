def hello():
    print("hello this is running")

print(__name__) # if we are using this program from the same file then it will give __main__ but if we use this code outside from this file then it will giva that file name from which it is running

# use case -  if there is a code that we do not want that it run in other file then us it like this

if(__name__ == "__main__"):
    print("it will run only in original file")
    hello()
