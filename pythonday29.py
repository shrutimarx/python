# recursion

def f1(phrases):
    if phrases == '':
        print('done!')
    else:
        print(phrases[0].lower())
        f1(phrases[1:])
        print(phrases[0].upper())
f1('ab')
# print(a) - a
# f1(b) 
# print(b)
# f1('')
# print('done!')
# print(B)
# print(A)

## Location of print statement matters - before and after function call
##
####def func():
######    if base case:
####        return something
####    else:
####        if:
##            return something
####        else:
##            return something
##

##def build_dic():
##    if base case:
##        return empty dictionary
##    else:
##        previous_dic = build_dic
##        change dic
##        return dic


# OBJECT ORIENTED PROGRAMMING
# alist = [1,2,3]
# 1) This list stores data and this list can do things. - .append(), .sort(), etc.

# create our own data type - can store data (attributes), that do things (methods)
# our scenario requires more specialised storage of data than just using default Python data type

# encapsulate our data into objects to separate them from other unrelated data

# create student - design blueprint (name is CALLED SELF)
# blueprint: student(name, hometown, major, courses (list)) - ALL ATTRIBUTES
# can: change major, register for class, etc.
# actual objects: priya - an instance of the class (an object), (Priya, Seattle, CS, []); (Alice, France, Physics, [])

# to get data from object, use dot notation
# priya.hometown
# alice.major
# to change - refer to blueprint (self.name to get blueprint's name)


print(type([1,2,3])) # class list

class Student: # captial letter
    pass
# how to create an object

##priya = str(data to be converted to a string) # constructor - creates a string object from what was placed there
# priya = Student("Priya", "Seattle", "CS")

# configure blueprint - special methods

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

    def register(self, course):
        self.courses.append(course)
        print('Registered for ' + course)



priya = Student("Priya", "Seattle", "CS")

# python doesn't know self
priya.major
priya.change_major('ISyE')

shruti = Student("Shruti", "10000", "CompE")

print(shruti)

print(shruti == priya) # FALSE
shayan1 = Student('Shayan', 'Pakistan', 'CS')
shayan2 = Student('Shayan', 'Pakistan', 'CS')

print(shayan1 == shayan2) # FALSE - do not share same memory before - NOW IT'S TRUE!!!!

shayan1 = Student('Shayan', 'Pakistan', 'CS')
shayan2 = shayan1
print(shayan1 == shayan2) # True

shruti.register('ISYE 2027')
print(shruti.courses)
print(shruti)
