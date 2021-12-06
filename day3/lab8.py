# given a n-digit number.find the sum of its digits.
a = int(input("enter the number"))
total = 0
while a>0:
    digits=a%10
    total=total+digits
    a = a//10
print("the sum of digits of the number entered is",total)
