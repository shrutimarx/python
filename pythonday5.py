#if you don't tell the function what to return it will return None which is
#type NoneType

print(None)
print(type(None))

def circ_area(radius):
    area = 3.1415189 * radius ** 2
    return area

circ_area(5)
result = circ_area(5)
print(round(result,2))

#### boolean expressions evaluate to True or False

print(3 > 5)

# the equality comparison is done using ==

print(3 == 3)

print(3.0 == 3)

print("cat?" < "cat!")

#you can combine these using and or not

print(3 < 5 and 3 > 2)
print(3 < 5 or 3 < 1)

#precedence (< <= etc) get evaluated
#anything in parenthesis 
#then not then and then or
#lastly the assignment operator if one is used
value = 3 > 5 and not 2 < 7 or 9 > 1
print(value)

print(3 < 2+1)


# write a statement that prints True if num is between 4 and 7 inclusive

num = 5
print(num >= 4 and num <= 7)
print(4 <= num <= 7)


age = 23

if age >= 18:
    print("go vote")
else:
    print("no voting for you")
print("done")


if age >= 17:
    print("you can go to college")
elif age >= 14:
    print("you can go to high school")
else:
    print("no school for you!")

## num += 1 adds one to whatever was stored in the variable num -= subtracts one







