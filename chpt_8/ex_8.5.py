#8.5 Open the file mbox-short.txt and read it line by line. 
#When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line
#(i.e. the entire address of the person who sent the message). Then print out a count at the end.

#ask user yo input filename
fname = input("Enter file name: ")

#if the length of the user input is less than 1, fname variable will default to the filename mbox-short.txt
if len(fname) < 1:
    fname = "mbox-short.txt"

#open mbox-short.txt into fh variable 
fh = open(fname)

#empty counter for loop will update for each from email
count = 0

#iterate through each line in the file to find from emails
for line in fh:
    #only grab lines that start with "From "
    if line.startswith("From "):

        #increase count by 1 for each iteration
        count = count + 1

        #split line into list sepeating by spaces
        fline = line.split()

        #print index 1 of the list 
        print(fline[1])
    else:
        continue

print("There were", count, "lines in the file with From as the first word")
