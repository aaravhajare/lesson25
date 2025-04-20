
class parrot:

    species = "bird"

    def __init__(self,name,age):

        self.name = name
        self.age = age

blu = parrot("blu" , 10)
yell = parrot("hi" , 12)

print("Hi i am from" , blu.species , "species")
print("hi i am from " , yell.species , "species")

print("Hi i am " , blu.name , "I am " , blu.age , " year old")
print("Hi i am " , yell.name , "I am " , yell.age , " year old")
