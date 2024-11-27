#9.1 Write a program that reads the words in words.txt and stores them as keys in
#a dictionary. It doesn’t matter what the values are. Then you can use the in
#operator as a fast way to check whether a string is in the dictionary.

#file handle for words.txt
fh =  open("words.txt")
#empty dictionary to add to
d = dict()

#iterate through each line in the file to grab individual words
for line in fh:
    #remove whitespace
    line.strip()
    #seperate each word and line into a list
    words = line.split()
    #iterate through each word in words
    for word in words:
        #if the word is in the list add +1 to its value
        if word in d:
            d[word] = d[word] + 1
        #if the word is not in the list assign its value as 1
        else:
            d[word] = 1

print(d)
            
