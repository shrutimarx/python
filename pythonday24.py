import sys
print(sys.path)

import requests
def testRequests():
  res = requests.get("https://restcountries.com/v2/name/united")
  print("Success!")
testRequests()

# write three lists to a csv file called data.csv

headers = "name, role, salary\n"
names = ['Chris','Collin']
roles = ['Head TA', 'Regular TA']
salaries = [12.5,9.5]

##outfile = open('data.csv','w')
##outfile.write(headers)
##for index in len(names):
##    outfile.write(names[index] + ',' + roles[index] + ',' + '$' + str(salaries[index]) + '\n'
##    

# getting data from the web - data on the web is called a web API
# Application Programming Interface - provide data to other computers (not html which is for people)

url = 'https://pokeapi.co/api/v2/pokemon/3'
r = requests.get(url) # send a get request to this url - r stands for response
print(r) # prints out the status (if not found 404, if found 200)
print(r.text[:500])
print(type(r.text)) # just a str not a dictionary
# convert this str into a dictionary or list or other python data structure
data = r.json() # the .json function converts your str into the correct data structure
# json is a notation for storing data on the web
print(data.keys())
print(data['name'])
print(data['height'])
print(data['weight'])
