salary=int(input("please enter salary:"))
da= 52/100*salary
itc=5/100*salary
ma= 10/100*salary
hra=10/100*salary
va= 10/100*salary
pf=10/100*salary
gross_salary=salary+ da + hra + ma + itc + va
print("gross salary is:",gross_salary)
print("net_salary=",gross_salary-pf)
