name = "ajay" # strings can not be changed 

nameslice = name[1:3] # method of slicing - starting from 1 and taking till 3 , not 3 (1 and 2)
print(nameslice)

names2= name[:3] # empty space will be taken as 0 in starting
names3 = name[1:]# empty space will be taken as -1 in ending

#===================================================

# to use any varriable in string use f string

Name='ajay'
print(f"hello the name was {Name} ans it is f string")

#===================================================

# slice with skiping 
ajay = "itisarawdatatouseincode"
ajay2=ajay[1:5:2] # here 2 is denoting that on which repaetation letter will apear
print(ajay2)



# functions of strings

#len
ajay3 = "ajay"
print(len(ajay3))

#endswith
end = ajay3.endswith('ay')
print(end)

#startswith
start = ajay3.startswith('aj')
print(start)

#capitalize - capitalize first letter of sentence
cap = ajay3.capitalize()
print(cap)


text = " hello python "

# upper()
# Use: convert text to CAPITAL letters
print(text.upper())      
# OUTPUT:  HELLO PYTHON 


# lower()
# Use: convert text to small letters
print(text.lower())      
# OUTPUT:  hello python 


# capitalize()
# Use: first letter capital
print(text.capitalize()) 
# OUTPUT:  hello python 


# title()
# Use: first letter of every word capital
print(text.title())      
# OUTPUT:  Hello Python 


# strip()
# Use: remove extra spaces
print(text.strip())      
# OUTPUT: hello python


# replace()
# Use: replace old text with new text
print(text.replace("python", "java"))
# OUTPUT:  hello java 


# split()
# Use: convert string into list
print(text.split())      
# OUTPUT: ['hello', 'python']


# join()
# Use: join list into string
words = ["I", "Love", "Python"]
print(" ".join(words))
# OUTPUT: I Love Python


# find()
# Use: find position/index
print(text.find("python"))
# OUTPUT: 7


# count()
# Use: count character/word
print(text.count("o"))
# OUTPUT: 2



# isdigit()
# Use: check only numbers
num = "12345"
print(num.isdigit())
# OUTPUT: True


# isalpha()
# Use: check only alphabets
word = "Python"
print(word.isalpha())
# OUTPUT: True


# isalnum()
# Use: check alphabets + numbers
mix = "Python123"
print(mix.isalnum())
# OUTPUT: True



# reverse string
# Use: reverse text
print(text[::-1])
# OUTPUT:  nohtyp olleh 


# in keyword
# Use: check word exists or not
print("python" in text)
# OUTPUT: True


# not in keyword
# Use: check word not exists
print("java" not in text)
# OUTPUT: True