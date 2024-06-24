#while loops work like if statements that keep going back up and checking
#the conditions again.

import time

"""
num = 1
while num < 5 or num % 2 == 1:
    print(num)
    num += 1

#for each loop loops for a particular number of times

for letter in "123456":
    print(letter) #made of individual letters - you can do something for
    #each piece; int is not iterable

name = input("Enter your name: ")
while name != "Melinda".lower():
    print("go away")
    name = input("Enter your name: ")
print("Hi melinda")


for value in [1, 2, 3]:
    print(value)
# what if you want the numbers from 1 to 25

for value in range(0, 25, 2):
    print(value + 1)
"""

for num in range(0,8,2):
    print(num)

temp = 89.9
while temp < 103:
    print("Your temp is ", temp)
    temp += 5
print("GO TO THE HOSPITAL NOWWW!!!")

count = 0

def how_many_vowels(sentence):
    for letter in sentence:
        if letter in "aeiouAEIOU":
            count += 1
    return count # after the loop

print(how_many_vowels("Hi y'all"))
print(how_many_vowels("Bye everyone!"))
