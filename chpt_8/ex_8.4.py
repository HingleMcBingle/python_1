#Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

#prompt user for file name
fname = input("Enter file name: ")
#open file in variable
fh = open(fname)
#empty list to iterate words into 
lst = list()
#for loop to pull lines and seperate words into lst
for line in fh:
    #split line from string into individual word list
    words = line.split()
    #conditional to only add words to lst if words arent already in lst
    if words not in lst:
        #add words to lst
        lst.extend(words)
        #sort lst 
        lst.sort()
print(lst)
