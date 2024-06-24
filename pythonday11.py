
name = "Chris"
print(name[0].isalpha() and name[0].isdigit()) # False

print(type(name) == str) # True

def same_f_and_l(astr): # write a function that returns true if the first and
    # last letter of the param are the same and False otherwise.
    return astr[0] == astr[-1]
if same_f_and_l("Chris"):
    print("same!")

#.isalpha() # are the characters in the alphabet?

# escape sequences (not on Exam 1)

name = "Andr\ne" # there is an escape sequence in the middle of the string
# \n is the escape sequence for the new line character

print(name)

# these sequences (\n \t (tab) \\ (backslash) \" (quote) \' (one single quote)
# each count as one character when counting the length

name = "a\\b"
print(name)

print("cat\ndog\nbird")

# this string method produces a new datatype called a list
# super fun and useful

sentence = "Chris and Andre were late today"
print(sentence.split()) # splits into word onto white space (not just one space)

ssn = "234-21-6777"
print(ssn.split("-")) # delimiter is dividing the pieces (doesn't show up)
print(sentence.split("e"))

# the strip method removes white space from the beginning and end of a str

data = "    john smith    "

print(data.strip()) # from when you read data from files with lots of white space



