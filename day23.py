def file_stuff(in_file,out_file):
    file = open(in_file,'r')
    text = file.read()
    file.close()
    text = text.replace(',','')
    text = text.replace('!','')
    text = text.replace("'","")
    output = ''
    text.split()
    for word in text.split():
        output += word + '\n'
    file = open(out_file,'w')
    
    file.write(output)
    file.close()
    
    
print(file_stuff('day23_poem.txt','day23_words.txt'))
    
    
