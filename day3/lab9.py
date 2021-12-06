# take username and password from user and check it again for the three times whether the user has entered the right
# username and password.if yes then print a message"logged in Successfully", if not then print invalid credentials for
# consecutive 3 times and if the limit exceeds than print "Attempt finished".
a = input("enter a username")
b = input("enter a password")
for i in range(0,3):
    a1 = input("enter a username")
    b1 = input("enter a password")
    if a==a1 and b==b1:
        print("you are logged im successfully")
        break
    else:
        if(a!=a1 or b!=b1):
            print("invalid username or password")
else:
    print("attempt finished")

