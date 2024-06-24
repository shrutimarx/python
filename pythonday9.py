
word = "jackets"
# indexing always gives only one character or causes a runtime error
print(len(word))
print(word[6])# runtime error b/c no position 12 - greatest index possible is
# len word - 1
print(word[-1]) # wraps around

# slicing gives you 0 or more possible strings concatenated together (a substring)
print(word[2:100]) # goes from 2 to as many as possible
print(word[2:]) # slices from 2nd position to the end of str
print(word[:]) # prints everything
print(word[:5]) # from the beginning to the 5th index, but only really the 4th
print(word[::2]) # step size 2 from beginning to end
print(word[::-1]) # reverse string
print(word[6:2:-2])
print(word[-2:-5:-1])


# break and continue
## break immediately exits a loop
## continue goes back to the start of a loop

for num in range(100):
    print(num)
    if num > 4:
        break  #exit the loop
print("after loop")

# continue goes back to the start
for num in range(10):
    print(num)
    if num > 2 and num < 5:
        continue # go get another number - doesn't do num ** 2
    print(num ** 2)
    
# continue example
for num in range(-3, 3): # -3, -2, -1, 0, 1, 2 (doesn't get to 3)
    print(num)
    if num == 0:
        continue  # do not continue the code that follows this, get a new num
    print(10/num)

    
# keeping a running total
## continue to buy things at a store until i run out of money and want to buy
# of 5 things

money_spent = 0.0
for count in range(0,5):
    cost = float(input("cost of item: "))
    if money_spent + cost > 10.0:
        print("Too pricey")
        break
    money_spent += cost
print("You spent ${}".format(money_spent))    


# Nested loops

for num in range(3):
    for num2 in range(4):
        print(num2)
        break # does the inner loop for each of the outer number
    







    
