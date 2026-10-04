# with map we can run a function on all elements in list

l = [1,2,3,4,5,6,7,8,9]

sqr = lambda a : a*a

new = map(sqr, l)

print(list(new))


# filter function used to filter out data from list using function

def even(a):
    if(a%2==0):
        return True
    return False

evenNumbers  = filter(even , l)
print(list(evenNumbers))



# reduce - it perform the function on first 2 numbers sequantialy  till there is only i data in list

from functools import reduce

def sum(a,b):
    return a+b

reduced = reduce(sum,l)

print(reduced)