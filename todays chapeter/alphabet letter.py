char=input("ENTER a character: ")
if len(char) == 1:
    if char.isalpha():
        print(char,"is an alphabet")
    else:
        print(char,"'is not alphabet")
else:
    print("please entetr only one character")