file = input("enter name of the file to scan : ")
word = input("enter the word to change in this file : ")
changed =  input("enter the word by which you want to change : ")

f=open(file)
data= f.read()
f2= open(file, "w")

if(word in data):
    print("yes, this word is present in this file")
    changeddata = data.replace(word, changed)
    f2.write(changeddata)
    print("changed successfully")

else :
    print("no, this word is not present in this file")

    f.close()
    f2.close()