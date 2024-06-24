# student class

class Student:
    # every method inside of a class needs to also pass in the name of the blueprint, so we can change it
    def __init__(self, name, hometown, major):  # initialise 
        self.name = name # the first value that i put in has to be name
        self.hometown = hometown
        self.major = major
        self.courses = []
        
    def change_major(self, new_major):
        self.major = new_major
        print('Welcome to {}.'.format(new_major))
        
    def __str__(self):
        return "{}: a {} student taking {} courses.".format(self.name, self.major, len(self.courses))
    
    def __eq__(self, other):
        if self.name == other.name and self.hometown == other.hometown:
            return True
        else:
            return False
        # doesn't have to make sense!

    def register(self, course):
        self.courses.append(course)
        print('Registered for ' + course)

    def __lt__(self, other):
        return self.hometown < other.hometown
    # data type of hometown is str - str class has lt method defined
    def __ge__(self, other):
        return self.hometown >= other.hometown

# outside class don't say self - self is Alice

alice = Student("Alice", "Decataur", "Physics")
collin = Student("Collin", "Demorest", "CM")
print(type(alice)) # instance of class
alice.change_major('CS')
print(alice)

# the __eq__ is called when the == sign is used self(left), other(right)

print(alice < collin) # what makes alice less than collin?
# __lt__ __gt__ __le__ __ge__ __ne__

# __lt__ is most important (USED FOR SORTING)

ta_list = [collin, alice] # contain objects
ta_list.sort()
for ta in ta_list:
    print(ta) # calls the __str__ from Student class

collin.register("CS4400")
print(collin)

blist = [collin, alice, 'cat', [1,2,3]]

for item in blist:
    print(item) # calls the right data type


# Aliases and clones as related to objects

new_alice = alice
print(new_alice) # same memory location

new_alice.register("CS4400")
print(alice) # anything i do to new_alice also happens to alice


ta_list = [collin, alice]

# if no __eq__
print(collin == alice) # FALSE python looks for an eq method, if none, it checks to
# see if they are in the same memory location - CHECKS ALIAS
print(alice == new_alice)

alice = new_new_alice = Student("Alice", "Decatur", "CS")
new_new_alice = Student("Alice", "Decatur", "CS")
ta_list = [collin, alice]
print(alice == new_new_alice) # if no __eq__, False; with __eq__ True

print(ta_list[1] == alice) # is this an alias?



