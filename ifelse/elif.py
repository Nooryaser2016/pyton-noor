height = float(input("enter your height in cm:  "))
weight = float(input("enter your weight in kg:  "))
BMI = weight / (height/100)**2

if BMI <=18.4:
    print("u are underweight")
elif BMI <=24.9:
    print("you are healthy")
elif BMI <=29.9:
    print("you are healthy")
elif BMI <=39.9:
    print("you are healthy")
elif BMI <=34.9:
    print("you are healthy")
else:
    print("INVAILD VALUES")
