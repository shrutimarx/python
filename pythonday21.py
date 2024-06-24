# write a function called sum_up that opens a file passed in as a
# param and returns the sum of all the numbers in the file

def sum_up(filename):
    # cannot do an if statement
    try:
        infile = open(filename,"r")
        text = infile.read()
        infile.close()  # with reading it's bad style not to close the file
        print(hi)
        total = 0
        # print(text)
        pieces = text.split()  # splits on all whitespace
        # print(pieces)
        for num in pieces:
            total += int(num)
        return total
    except Exception as error:
        return error
    except FileNotFoundError:
        print('File Not Found!')

print(sum_up('day21numbers.txt'))

##infile.read()
##infile.realine()
##infile.readlines() - everything is a string on the web

# there is only one way to write to a file - .write() method

outfile = open('iHateSHRUTI','w')
outfile.write("sid says hi\n")
outfile.write('hi')
outfile.close() # NEED TO CLOSE THE FILE
# python will create the file if it doesn't exist & will replace its contents
# if it doesn't exist

# create a file containing all the letters of the alphabet one per line
# call the file letters.txt
import string
letterfile = open('letters.txt','w')
for letter in string.ascii_lowercase:
    letterfile.write(letter + "\n")
letterfile.close()

# given dictionary d write the keys that have odd values to a file called odds.txt
# one per line
d = {1:43, 2:55, 3:21, 5:96, 7:1, 8:41}

oddfile = open('odds.txt','w')
for key,value in d.items():
    if value % 2 == 1:
        oddfile.write(str(key) + '\n')
    


oddfile.close()
















