import requests

# API - a way to share data on the web
# json formatting

# who is heavier bulbasaur or charmander

baseurl = "http://pokeapi.co/api/v2/"
parturl = "pokemon/charmander/"
r = requests.get(baseurl + parturl)
print(r) # prints status code - stands for response
print(baseurl+parturl)
print(r.text[0:500])
data = r.json() # convert str to appropriate data type - dictionary
print(data.keys())
print(data['weight'])

parturl = "pokemon/charizard/"
r = requests.get(baseurl + parturl)
print(r) # prints status code - stands for response
print(baseurl+parturl)
print(r.text[0:500])
data = r.json() # convert str to appropriate data type - dictionary
print(data.keys())
print(data['weight'])

# what if the website works but is html not json

r = requests.get('http://www.gatech.edu') # send a request to that website to get a response
print(type(r)) # response object
#page = r.json()
#print(page) # doesn't work
print(r.text[:1000]) # gives html

baseurl = 'https://swapi.dev/api/'
parturl = '/people/1' # no 0 value
r = requests.get(baseurl + parturl)
data = r.json()
print(data)
print(data.keys())
name = print(data['name'])
newurl = data['homeworld']
r2 = requests.get(newurl)
print(r2)
data2 = r2.json()
print(data2.keys())
planet = data2['name']
print(planet)

# create a dictionary that maps each star wars character to their planet
dic = {}
for i in range(1,6):
    baseurl = 'https://swapi.dev/api/'
    parturl = '/people/' + str(i) # no 0 value
    r = requests.get(baseurl + parturl)
    data = r.json()
    name = print(data['name'])
    newurl = data['homeworld']
    r2 = requests.get(newurl)
    data2 = r2.json()
    planet = data2['name']
    dic[name] = planet
print(dic)


url = "https://anapioficeandfire.com/api"

r = requests.get(url)
data = r.json()
r2 = requests.get(data['houses'])
data2 = r2.json()
print(data2)
dic = {}
for dictionary in data2:
    print(dictionary['swornMembers'])
    
    
    
    

