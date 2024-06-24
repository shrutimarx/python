# csv

file = open('day23police.csv','r')
headers = file.readline() # str
datalines = file.readlines() # a list of str
file.close()
print(datalines[0].split(','))
count = 0
for line in datalines:
    pieces = line.split(',')
    offence = pieces[2]
    if 'bicycle' in offence.lower() or 'bike' in offence.lower():
        count += 1
print(count)

# how many murders occured in council district 9?

file = open('day23police.csv','r')
headers = file.readline() # str
datalines = file.readlines() # a list of str
file.close()
print(datalines[0].split(','))
count = 0
for line in datalines:
    pieces = line.split(',')
    offence = pieces[3]
    district = pieces[1]
    if 'assault' in offence.lower() and district == '9':
        count += 1
print(count)

# what council district had the most assaults?

file = open('day23police.csv','r')
headers = file.readline() # str
datalines = file.readlines() # a list of str
file.close()
print(datalines[0].split(','))
dic = {}
for line in datalines:
    pieces = line.split(',')
    offence = pieces[3]
    district = pieces[1]
    if district == "":
        continue
    if 'assault' in offence.lower():
        if district not in dic:
            dic[district] = 0
        else:
            dic[district] += 1
print(dic)

# changing a file

f = open('day20limerick.txt','r')
text = f.read()
f.close()
print(text)

text = text.replace('f','')
print(text)

f2 = open('day20limerick.txt','w')
f2.write(text) # writes it back the same way
f.close()





