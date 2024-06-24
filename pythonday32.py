# Farmer and Animal Method

# Lecture 32 - Object Oriented Programming (OOP) Chapter 15, 21, 16
#
"""
What we did last time:
Combining two classes


What we are doing today
# objects are references (aliases and clones revisited)
# practice oop for exam
# default parameters vs. always assigned to a specific value

"""
# Let's look at the Farmer and Animal methods from last lecture's miniquiz
class Farmer:
  def __init__(self,n):
    self.name = n
    self.animal_list = []
  def __str__(self):
    return "Farmer {} has {} animals total".format(self.name, len(self.animal_list))
  def add_stock(self,animal):
    self.animal_list.append(animal)
  def num_cows(self):
    count = 0
    for animal in self.animal_list:
      if animal.animal_type == "cow":
        count += 1
    return count

  def count_animals(self):
    return len(self.animal_list)
    
class Animal:
  def __init__(self,t,f):
    self.animal_type = t # t is a str
    self.farmer_owner = f # f is a Farmer object

  def __str__(self):
    return "This animal is a {}".format(self.animal_type)



# what if we have an Animal object? How do we know which Farmer
# this animal belongs to?

##bessy = Animal('cow')
##bessy2 = Animal('cow') # clone
##bessy3 = b
mcdaniel = Farmer('Old McDaniel')
##mcdaniel.add_stock(bessy)
bossy = Animal('cow',mcdaniel) # mcdaniel is not a string - it's a Farmer object
mcdaniel.add_stock(bossy)

# i have to look through all the farmers' animal_lists

# write a loop that prints "Found her home" if bessy belongs to farmer
# McDaniel

for each_animal in mcdaniel.animal_list:
##    if each_animal == bessy: # are these aliases? Yes
        print('Found her home')
        
# write a snippet of code that prints found her home if bossy belongs to
# farmer mcdaniel

if bossy.farmer_owner == mcdaniel:
    print('found her home!')

# add a method to the Farmer class that returns the number of animals
# in the stock list - call this method count_animals
print(mcdaniel.count_animals())







