# csv files

file = open('day22alice.txt','a')
file.write('\nThe END!!')
file.close() # need to close the file

file = open('day22alice.txt','r').read()
print(file)

# csv values, comma separated values

file = open('day22crime.csv','r')
headers = file.readline() # read the first line
data = file.readlines()
file.close()

print(data) # a list of str 

# what is the average crime rate for these cities

total = 0.0

for line in data:
    line = line.strip() # strips off \n
    pieces = line.split(',') # splits by comma
    print(pieces)
    total += float(pieces[-1])
print(total/len(data))

# what is the average crime rate for a city with a name that starts w 's'
total = 0
scount = 0
for line in data:
    line = line.strip() # strips off \n
    pieces = line.split(',') # splits by comma
    name = pieces[2]
    rating = float(pieces[3])
    if name[0] in 's' or 'S':
        scount += 1
        total += rating
print(total/scount)

dic = {}
for line in data:
    line = line.strip() # strips off \n
    pieces = line.split(',') # splits by comma
    name = pieces[2]
    rating = float(pieces[3])
    dic[name] = rating
print(dic)

# create a list of city names for all the cities with ratings >= 4297.05
high_crime_list = []
for line in data:
    line = line.strip() # strips off \n
    pieces = line.split(',') # splits by comma
    name = pieces[2]
    rating = float(pieces[3])
    if rating > 4297.05:
        high_crime_list.append(name)
print(high_crime_list)

        
        







    
