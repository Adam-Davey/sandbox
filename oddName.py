"""Adam Davey"""
name = str(input("what is your name?:"))

while len(name) == "":
        print("invalid name")
name = str(input("what is your name?:"))




print(name[::2])