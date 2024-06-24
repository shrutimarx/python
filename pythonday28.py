# print out the letters in a string one letter per line
# without a loop with recursion
# assume there is at least one letter

def print_letters(astr):
    # base case
    if len(astr) == 1:
        print(astr)
    else:
        print(astr[0])
        # recursive call get you closer to the base case
        print_letters(astr[1:]) # one to the end gets smaller
print_letters('jackets') # don't think of it as one letter at a time


##if len(astr) > 0:
##    print(astr[0])
##    print_letters(astr[1:])
##  still has a base case - opposite of if


# factorial 5! = 5*4*3*2*1
# factorial of 5! is 5 * 4! all the way to 2 * 1! (which we know is 1)

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)
print(fact(5))

# return a count of how many vowels are in a string
def vowels(astr):
    if len(astr) == 0:
        return 0
    else:
        if astr[0] in 'aeiou':
            return 1 + vowels(astr[1:])
        else:
            return vowels(astr[1:])
    
print(vowels('jackets'))

# in reverse!
def print_letters(astr):
    # base case
    if len(astr) == 1:
        print(astr)
    else:
        print_letters(astr[1:])
        # recursive call get you closer to the base case
        print(astr[0]) # one to the end gets smaller
print_letters('abc') # in reverse order

# building a data structure using recursion

# build a string of the digits from 0 up to the input param
# inclusive using recursion

def build_string(num):
    if num == 0:
        return '0' # make a string 0 concatenated onwards
    else:
        return build_string(num-1) + str(num) # if function call comes first,
    # so does the base case
print(build_string(5))


# build a dictonary mapping each even number up to the param
# to its square and each odd number up to the param to its cube

def build_dict(num):
    if num == 0:
        return {0:0}
    else:
        dic = build_dict(num-1)
        if num % 2 == 0:
            dic[num] = num ** 2
        else:
            dic[num] = num ** 3
    return dic
        # need to recursively build the rest of the dictionary

print(build_dict(3)) # {0:0,1:1,2:4,3:27}


    
    



