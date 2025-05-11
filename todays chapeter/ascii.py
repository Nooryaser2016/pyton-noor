char=input("enter a character: ")
if len(char) == 1:
    ascii_value= ord(char)
    print(f"the ascii Value of '{char}'is{ascii_value}")
else:
 print("please enter only one character")