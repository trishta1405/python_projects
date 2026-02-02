import time
c1=time.localtime(time.time())
h=c1.tm_hour
m=c1.tm_min
s=c1.tm_sec
if h==0:
    h=12
elif h>12:
    h=h-12
print(f"{h}:{m}:{s}")
