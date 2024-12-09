#Write a program that reads a file and prints the letters in decreasing order of frequency.
#Your program should convert all the input to lower case and only count the letters
#a-z. Your program should not count spaces, digits, punctuation, or anything other
#than the letters a-z.

#import string module
import string
#ask user for file name
fname = input("Le name of file?:")

#try to open user input 
try: fhand = open(fname)
#close program if it doesnt work
except: 
    print("nope") 
    quit()
#empty list to iterate dictionary tuples into for sorting by value
lst = list()
#empty dictionary to iterate and count letters into
d = dict()
for line in fhand:
        #remove punctuation from line
        line = line.translate(line.maketrans(" "," ",string.punctuation))
        #remove numbers from line
        line = line.translate(line.maketrans(" "," ",string.digits))
        #lower case all words in line
        line.lower()
        #remove whitespace 
        line.rstrip()
        #split line into words seperated by whitespace
        words = line.split()
        #iterate through each word
        for word in words:
             #lowercase each word incase the previous .lower failed
             word = word.lower()
             #split each word into letters
             letter = word.split()
             #iterate through each letter and add it to a dictionary for counting
             for letter in word:
                 d[letter] = d.get(letter, 0) + 1

for key,val in d.items():
    #append key,value from d into lst as value, key for sorting by value
    lst.append((val,key))
    #sort in descending highest to lowest
    lst.sort(reverse=True)
#print sorted key,value from lst
for val,key in lst:
    print(key,val)        
        
         
        


    