def take_input():
    number = int(input("Enter your number: "))
    if number < 0:
        print("Number is negative.")
        return
    else:
         print("Number is positive.")
take_input() # recursive call

take_input()