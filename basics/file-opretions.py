f = open("file.txt") # or open(filename, mode) example - open("file.txt", "r") is mode not mentioned - read default
data= f.read()
print(data)
f.close()


# writing in a file

f1 = open("file2.txt", "w")
st = "it will inserted in file"
f1.write(st)
f1.close()


# ===================== more functions

f3 = open("file.txt")
lines = f3.readlines()  # it will give a list with each line in that file
print(lines)            # if lines will not available the it will return empty ""
f3.close()

f4 = open("file.txt")
line = f4.readline() 
print(line)
line2 = f4.readline()
print(line2)
f4.close()

# =============== to avoid the file closing use this 

with open("file,txt") as f :
    print(f.write())


# for multiple use like this

with (
    open("file,txt") as f,
    open("file2,txt") as f2
):
    print("opretions can we done with multiple files")