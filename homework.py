
class dog:

    animal = "dog"

    def __init__(self,name,breed):
        
        self.name = name
        self.breed = breed

oreo = dog("oreo" , "husky")
puff = dog("puff" , "bulldog")

print("Dog detail")
print("species :" , oreo.animal)
print("Name :" , oreo.name)
print("Breed :" , oreo.breed)

print("Dog detail")
print("species :" , puff.animal)
print("Name :" , puff.name)
print("Breed :" , puff.breed)

print(dog.animal)