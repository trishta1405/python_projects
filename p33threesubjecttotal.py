marks_in_maths=int(input("enter marks of maths:"))
marks_in_ss=int(input("enter marks of ss:"))
marks_in_science=int(input("enter marks of science:"))
total_marks=marks_in_maths+marks_in_ss+marks_in_science
print("total marks are-",total_marks)
if total_marks<50:
    print("grade C")
elif 50<total_marks<100:
    print("grade B")
else:
    print("grade A")