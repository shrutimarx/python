print("hi")

#function should be versatile

def say_hello(name,age):
    print("Hello {} year old {}!".format(age,name))

say_hello("Pedro",22)
say_hello("Chris",20)
name = "Joe"
age = 6

say_hello(age,name)
#name is set to 6 and age is set to name - python only cares about position
#parameters - name and age. name gets the value of whatever the first thing is
#age gets set to the second thing.
#inside the function vs outside the function - not the same!

#functions that return a value
#in python a function call only returns one value

def square_area(side):
    return side ** 2

print(square_area(4.5) + square_area(10))
#didn't add print so nothing is printed. Return is good when you don't
#want a result printed. Rounding and such shouldn't be decided in the function

# functions can return any data type

def hyphenate(astr):
    return astr + "-" + astr

new_word = hyphenate("cat")

print(new_word)

new_word = hyphenate("cat")
new_new_word = hyphenate(new_word)
print(new_new_word)

#what if your try to use or print out a result from a function
#that doesn't include the return statement

def f1(astr):
    print(astr + "-" + astr)

new_word = f1("cat") # assign the returned value to new_word
print(new_word) #if you don't return something, python will return none

# compute avg of 3 grades where the first counts twice as much as other
def calc_average(t1, t2, t3):
    return (t1*2 + t2 + t3)/3
t1 = 10
t2 = 20
t3 = 30
average = calc_average(10, 20, 30)

print (average)









