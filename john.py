#Ask user to input their name
#If name is not "John", add name to incorrect names list otherwise break loop
#Print incorrect names list

incorrect_names = []

while True:
    name = input("Please enter your name: ").title()
    if name != "John":
        incorrect_names.append(name)
    else:
        break 
    
print(f"Incorrect names: {incorrect_names}")