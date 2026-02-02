import time
c1=time.localtime(time.time())
h=c1.tm_hour
m=c1.tm_min
s=c1.tm_sec
print(h,":",m,":",s)
if h<=12:
    print("good morning")
elif 12<h<=7:
    print("good afternoon")
else:
    print("good evening")
