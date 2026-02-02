import time
c1=time.localtime(time.time())
m1=c1.tm_year
if m1 % 4==0 and m1 % 100 !=0 or m1 % 400 == 0:
    print(f"{c1} is a leap year")
else:
    print(f"{c1} is not a leap year")
