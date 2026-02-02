import time
c1=time.localtime(time.time())
d=c1.tm_mday
m=c1.tm_mon
y=c1.tm_year
print(d,"/",m,"/",y)