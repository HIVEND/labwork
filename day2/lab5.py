# a school decided to replace the desks in three classrooms. Each desk sits two students.
# given the number of students in each class, print the smallest number of desks that can be purchased.
# the program should read three integers:the number of students in each of the three classes a ,b and c respectively
a = int(input("enter the number of students in first class?"))
b = int(input("enter the number of students in second class?"))
c = int(input("enter the number of students in third class?"))
sum = a//2+b//2+c//2+a%2 + b%2 + c%2
print(f" total number of desks we need:{sum} ")

