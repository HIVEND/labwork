# WAP which accepts marks of four subjects and display total marks, percentage and grade
a = int(input("enter the marks of first subject "))
b = int(input("enter the marks of second subject "))
c = int(input("enter the marks of third subject "))
d = int(input("enter the marks of fourth subject "))
t = a+b+c+d
T = (t/4)
print("total percentage is {} %" .format(T))
if T >= 70:
    print("student scored distinction")
elif T >=60 or T <70:
    print("student scored first division")
elif T >=40 or T <60:
    print("student scored pass marks ")
elif T < 40:
    print("student is fail ")
else:
    print("student didn't attempt the exam ")

