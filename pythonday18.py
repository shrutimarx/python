
adic = {}
bdic = adic
adic['c'] = 'cash' 
print(bdic)

alist = [1,2,3,[4,5]] # pointer to [4,5] - storing the memory location
blist = alist # alist and blist share memory
blist.append(7)
print(alist)

clist = alist[:] # it's a copy (doesn't share memory) - SHALLOW copy

### weird thing
alist[3].append(9)
print(alist)
print(blist)
print(clist) # includes the 9 [1,2,3, address] - points to same [4,5]

tas = {'Naomi':(18,4.0), 'Chris':(12,3.9), 'Collin':(26,4.0)}

lookup = ['Naomi', 'Collin']

# What is the average GPA of a TA in the lookup list
total = 0.0
for name in lookup:
    total += tas[name][1]
print(total/len(lookup))
total = 0.0
for name in lookup:
    age,gpa = tas[name]
    total += gpa
print(total/len(lookup))

# create a list of tas that have a gpa > 3.75

tas = {'Naomi':(18,4.0), 'Chris':(12,3.9), 'Collin':(26,4.0)}
high_gpas = []
for name in tas:
    age,gpa = tas[name]
    if gpa > 3.75:
        high_gpas.append(name)
print(high_gpas)

# change the dictionary - add the TAs favorite color to the dictionary in
# the lookup list

tas = {'Naomi':(18,4.0), 'Chris':(12,3.9), 'Collin':(26,4.0)}
lookup = [('Naomi', 'pink'),('Collin', 'dark green')]

for name,color in lookup:
    tas[name] = tas[name] + (color,) # MUST HAVE COMMA
print(tas)

# dictionary tracing practice
# expressions table

print(len({1:2,2:3,1:4})) # TWO replaces 1:2 - 1:4
print(len({print('hi'):5, print('bye'):7})) # value of print is None

print({1:4, 2:4})




    



