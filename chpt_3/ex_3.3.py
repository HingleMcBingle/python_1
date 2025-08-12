inp = input("Input a score between 0.0 and 1.0\n")
inp = float (inp)
try:
    if inp >= 0 and inp < 1 :
        if inp >= 0.9 :
            print("A")
        elif inp >= 0.8 :
            print("B")
        elif inp >= 0.7 :
            print("C")
        elif inp >= 0.6 :
            print("D")
        elif inp < 0.6 :
            print("F")
except: 
    print("Please Enter value Between 0.0 and 1.0")


