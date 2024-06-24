#rules for naming identifiers

"""
must contain only letters digits and _
cannot start with a digit
cannot be a reserved keyword
case sensitive

"""

name = "shruti"

print(name)

"""
recommendation: start all identifiers with a lowercase letter
and make your identifiers meaningful

"""

age = 29
print(age)

age = "twenty"

print(type(age))

# in python the type of an identifier is the type of the value
# stored in that memory location

"""
int
str
float
bool

"""

gpa = 3.9999
print(gpa)
has_glasses = False #orange:reserve python keyword)
print(type(has_glasses))

####
#arithmetic operators: + - / * ** %
#special whole number division operators // 
# pemdas rules apply

print ( 3+5      * 2)
print (5/3)
print (5%2)


### print statement varieties

name = "Chris"
age = 20

print(name,age) #comma adds space
print(name + str(age))

#print using the .format function (replaces each set up {} with the values
#in the formal parenthesis

print("{}{}" .format(name,name))
print("{}{}" .format(name,age))

def do_something():
    print("stuff")
    print("more stuff")

# a function includes a definition (def)
# and a block of code that executes when you call a function

do_something()

name = input("Enter your name: ")
print(name)









