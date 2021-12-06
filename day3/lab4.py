# given three integers, print the smallest one.(all integers should be user input)
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if a<=b and a<=c:
    print("first number is the smallest")
elif b<=a and b<=c:
    print("second number is the smallest")
else:
    print("third number is the smallest")
