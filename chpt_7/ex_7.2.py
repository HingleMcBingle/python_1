#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.

#ask user to input file name
fname = input("Enter file name: ")
#sum of all numbers extracted from file
numb_s = 0
#count for the amount of lines extracted from each loop iteration
count = 0
#variable to open filename input by user
fh = open(fname)
#for loop to iterate through file to find X-DSPAM-Confidence: lines and only take the number from the string
for line in fh:
    #if the line doesn't start with "X-DSPAM-Confidence:" restart loop 
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #count each iteration of loop to extract how many lines are printed
    count = count + 1
    #find index position of ":" and store that position in snumb variable
    snumb = line.find(":")
    #use the index position of ":" to store everything after it in the string into fnumb variable
    fnumb = line[snumb+1:]
    #sum floating point number extracted from each iteration in loop and store into numb_s variable
    numb_s = numb_s + float(fnumb) 
    
    #print(fnumb)
# print the average dividing numb_s by count
print("Average spam confidence:",numb_s / count)
#print("Done")
