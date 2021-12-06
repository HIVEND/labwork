# find BMI of a person where take mass and height as input from the user
mass = int(input("enter the mass:"))
height = int(input("enter the height:"))
BMI = mass/(height**2)
print(f"BMI of a person is {BMI} kg/m\u00b2")