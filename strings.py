string = "Denyse,Marie,Smith,21,London,UK"

print("1.", string.replace(","," "))

name = input("what is your name? ")
age = input("how old are you? ")

new_string = name + " is " + age + " years old"
print("2.",new_string)

print(f"the new string is {len(new_string)} charecters long")
print(new_string.upper())
print(new_string.find("alub"))