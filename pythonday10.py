# advanced string slicing, string methods

# a method is simply a function that is called in a different way


print("cat".upper()) # upper is a method - input is before the dot. so that
# we know that the input is the correct data type for that method

print("cats are {}".format("cute")) # string method - returns a formatted
# string with curly braces replaced

print("C3PO".lower())
                    
print("C111123PO".replace("123", "X")) # replace is all occurences of 1

print("C111123PO".replace("Q", "X")) # no error, no replacement

print("C123PO111".find("C")) # finds the FIRST occurence

print("C123PO111".find("C2")) # returns negative 1 (if it can't find it) - can
# check in an if statement

name = "Chris"
if name.find("C") == -1:
    print("not in there")
else:
    print("fun TA")

# what is the difference .find and .index
print("cat".find("z")) #no error
# print("cat".index("z")) #runtime error

# what if you need to uppercase just the third and fourth characters
name = "spongebob"
name[2].upper()
name[3].upper()

# this won't work

##name[2] = name[2].upper
##name[3] = name[3].upper # strings are immutable - cannot be changed
##print(name)


# what I have to do is rebuild the str
name = name[0] + name[1] + name[2].upper() + name[3].upper() + name[4:]

print(name)


number_to_change = 5
name = name[0:5] + name[number_to_change].upper() + name[number_to_change+1:]



text = "CS1301 is fun"

print(text[3:6:2])
print(text[3:7] + text[2:3] * 2)
print(text.upper())  
print(text.upper().lower())  
print(text.isupper())  
print(text[2].isdigit())
print(text.replace(" ","$"))
print(text.replace("C","c").replace("c","X"))
print(text.find("z"))

print("cat"[5:7])
print("cat"[2:3] * 0)
print("dog"[-2:-1])
print("bear"[3:3])



# some methods return True or False

#.isalpha() is it a letter
#.isdigit() 
#.isupper()
#.islower()

print("1".isupper())

# change all the vowels in the str to capital X

sentence = "TAs are fun"

newstr = ""
for ch in sentence:
    if ch in "aeiouAEIOU":
        newstr += "X"
    else:
        newstr += ch
sentence = newstr
print(sentence)








