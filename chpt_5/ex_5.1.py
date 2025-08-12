#iteration variable for input
num = 0
#variable for total
tot = 0.0
#infinite loop until 'done' is written to input
while True :
        #Prompt for a string from user
        sval = input('Enter a number: ')
        #stop loop when 'done' is input
        if sval == 'done':
                break
        #convert string to floating point integer
        try:
            fval = float(sval)
        #if converting string to floating point integer fails tell the user its an invalid input and restart the loop
        except:
               print('You gotta put a number in dawg')
               continue
        #print the number input by user 
        print(fval)
        #increase count by 1 for every successful user input to num variable
        num = num + 1
        #sum all floating input to tot variable
        tot = tot + fval

print('ALL DONE')
print(tot,num,tot/num)