file = input("enter name of the file to scan : ")
word = input("enter the word to find in this file : ")

f=open(file)
data= f.read()

if(word in data):
    print("yes, this word is present in this file")
else :
    print("no, this word is not present in this file")