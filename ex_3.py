hrs =  input("How Many Hours Worked?")
hrs = float(hrs)
if hrs > 40 :
        hrs_plus = (hrs - 40)
rate =  input("Whats the Hourly Rate?")
rate = float(rate)
rate_plus = (rate * 1.5)
print( (hrs * rate))
if hrs_plus > 0:
      print(hrs_plus * rate_plus + hrs * rate)