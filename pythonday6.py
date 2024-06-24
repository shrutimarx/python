num = 8
if num > 5:
    num = 3
    if num == 15:
        print("15")
    else:
        print("not 15")
else:
    print("not less than 15")

# shortcut operators
# just a short way to express a variable's value changing
num = 5
num += 1 # num becomes 6
num += 2
num -= 1
num *= 2 

# shortcut operators are += *= -= /= //= %=

num %= 5
print(num)

# shortcut operators could work with str too
name = "Naomi"
name += "s"
print(name)

# remmeber that a conditional expression results in a bool
bool_value = (3 + 5 > 6 * 2)
score = 75
iswinning = score > 100
print(iswinning)
if iswinning:
    print("Yay")
else:
    print("keep going")

# functions that return a bool
#write a function that returns True if the school is "Georgia Tech" and
#the GPA is greater than 2.0, or the school is UGA and the gpa is greater than 3.99"
#any other school choice is not smart


def is_smart(school,gpa):
    if school == "Georgia Tech" and gpa >= 2.0:
        return True
    elif school == "UGA" and gpa >= 3.99:
        return True
    else: #don't need an else
        return False
print(is_smart("Georgia Tech",3.5))
print(is_smart("UGA",1.0))
      
# the in and not in operation
# is is a conditional operator bc it results in True or False

print("a" in "apple")
print("a" not in "cat")
# will not work with int or float :(

# tracing practice

is_cat = True
is_dog = False
age = 2
if is_cat:
    if age > 1:
        print("vet")
    else:
        print("young")
if not is_dog:
    if age < 3 and is_cat:
        print("wow")
    else:
        print("b")









    
