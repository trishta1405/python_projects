import time
c1=time.localtime(time.time())
h=c1.tm_hour
m=c1.tm_min
s=c1.tm_sec
if h<=12:
    print(h,":",m,":",s,"am")
else:
    print(h,":",m,":",s,"pm")