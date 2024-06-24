# try and except, reading text files


try:
    print(blah)
    print(3/0)
except: # any runtime errors
    print('an error happened')
finally: # always happens - even if it says return in except
    print('done, close all windows') # if error in 'finally' then an error occurs

# the file must be stored in your current working directory


infile = open('day20limerick.txt', 'r')  # open the file for reading

# 3 ways to read a file
# 1: read the text into one very long str

mytext = infile.read() # reads all the file into one str
print(mytext)
infile.close()


infile = open('day20limerick.txt', 'r')
# 2nd way to read from a file

myline = infile.readline() # reads another line
infile.close()
print(myline) # skipped one line (/n) after the first line there is a /n


infile = open('day20limerick.txt', 'r')
# 3rd way - read all the lines into a list of str
line_list = infile.readlines()
infile.close
print(line_list)

# everytime you close the file and open it again
# the cursor goes back to the beginning

