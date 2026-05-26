# it is like json that store values in key-value pairs

a= {
 
 "ajay":123,
 "ajay2":1234
}

empty={} #empty dictionary

print(a, type(a))

# it do not follow indexing but know the key
#can be changed
#keys should be different
print(a["ajay2"]) #return the value of givrn key and error if key is not available


print(a.items()) # print key-value pairs
print(a.keys()) # print keys pairs
print(a.values()) # print values pairs

a.update({"ajay" : 100, "ajay3":101}) #update the data, if key available- update ,  if not make it
print(a)

print(a.get("ajay")) #returns value if available else None



# to know more

# ==========================================
# PYTHON DICTIONARY METHODS - FULL EXAMPLE
# ==========================================


# ------------------------------------------
# CREATE DICTIONARY
# ------------------------------------------

student = {
    "name": "Ajay",
    "age": 20,
    "course": "Python"
}

print("Original Dictionary:")
print(student)


# ==========================================
# ACCESSING VALUES
# ==========================================

# Access using key
print("\nName:")
print(student["name"])

# Safe access using get()
print("\nCourse using get():")
print(student.get("course"))

# get() with default value
print("\nCity using get() with default:")
print(student.get("city", "Not Found"))


# ==========================================
# ADDING NEW ITEMS
# ==========================================

# Add new key-value pair
student["marks"] = 95

print("\nAfter Adding Marks:")
print(student)


# ==========================================
# UPDATING VALUES
# ==========================================

# Change existing value
student["age"] = 21

print("\nAfter Updating Age:")
print(student)

# update() method
student.update({
    "city": "Jaipur",
    "phone": 1234567890
})

print("\nAfter update():")
print(student)


# ==========================================
# REMOVE ITEMS
# ==========================================

# pop() removes item and returns value
removed_age = student.pop("age")

print("\nRemoved Age:")
print(removed_age)

print("\nDictionary After pop():")
print(student)

# popitem() removes last inserted item
last_item = student.popitem()

print("\nRemoved Last Item:")
print(last_item)

print("\nDictionary After popitem():")
print(student)


# ==========================================
# DICTIONARY METHODS
# ==========================================

# keys() -> returns all keys
print("\nKeys:")
print(student.keys())

# values() -> returns all values
print("\nValues:")
print(student.values())

# items() -> returns key-value pairs
print("\nItems:")
print(student.items())


# ==========================================
# CHECK IF KEY EXISTS
# ==========================================

if "name" in student:
    print("\n'name' key exists")


# ==========================================
# LOOPING THROUGH DICTIONARY
# ==========================================

# Loop through keys
print("\nLoop Through Keys:")

for key in student:
    print(key)

# Loop through values
print("\nLoop Through Values:")

for value in student.values():
    print(value)

# Loop through key-value pairs
print("\nLoop Through Items:")

for key, value in student.items():
    print(key, ":", value)


# ==========================================
# COPY DICTIONARY
# ==========================================

new_student = student.copy()

print("\nCopied Dictionary:")
print(new_student)


# ==========================================
# SET DEFAULT VALUE
# ==========================================

# Adds key only if not present
student.setdefault("country", "India")

print("\nAfter setdefault():")
print(student)


# ==========================================
# FROMKEYS METHOD
# ==========================================

# Create dictionary using list of keys
keys = ["a", "b", "c"]

new_dict = dict.fromkeys(keys, 0)

print("\nDictionary Using fromkeys():")
print(new_dict)


# ==========================================
# NESTED DICTIONARY
# ==========================================

students = {

    1: {
        "name": "Ajay",
        "age": 20
    },

    2: {
        "name": "Rahul",
        "age": 21
    }
}

print("\nNested Dictionary:")
print(students)

# Access nested dictionary value
print("\nAccess Nested Value:")
print(students[1]["name"])


# ==========================================
# DICTIONARY COMPREHENSION
# ==========================================

# Create squares dictionary
square = {
    x: x * x
    for x in range(5)
}

print("\nDictionary Comprehension:")
print(square)


# ==========================================
# CLEAR DICTIONARY
# ==========================================

temp_dict = {
    "a": 1,
    "b": 2
}

print("\nBefore clear():")
print(temp_dict)

# Remove everything
temp_dict.clear()

print("\nAfter clear():")
print(temp_dict)


# ==========================================
# DELETE USING del
# ==========================================

sample = {
    "x": 10,
    "y": 20
}

print("\nBefore del:")
print(sample)

# Delete specific key
del sample["x"]

print("\nAfter del:")
print(sample)


# ==========================================
# LENGTH OF DICTIONARY
# ==========================================

print("\nLength of student dictionary:")
print(len(student))


# ==========================================
# FINAL OUTPUT
# ==========================================

print("\nFinal Student Dictionary:")
print(student)
