list1=[11, 44, 500, 22, 99, 77]
list2=[]
list3=[]
for i in range(len(list1)):
    if i % 2 == 0:
        list2.append(list1[i])
    else:
        list3.append(list1[i])
print(list2)
print(list3)

