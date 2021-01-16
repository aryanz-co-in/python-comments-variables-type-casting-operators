#  Assign many values to Multiple Variables
#  Python allows you to assign values to multiple variables in one line:

veg1, veg2, veg3 = "Onion", "Carrot", "Potato"

print(f"veg1                    = {veg1}")
print(f"veg2                    = {veg2}")
print(f"veg3                    = {veg3}")

# One value to multiple variables

counter = index = position = 5
print("----------------------------------")
print(f"counter                 = {counter}")
print(f"index                   = {index}")
print(f"position                = {position}")


#  Unpacking list items to variables
#  Ensure the list item count and variable declared are of same length
#  i.e. Below list has 3 items in the list, then we need to ensure we create
#  3 variables to assign them.
fruits = ["Mango", "Banana", "Kiwi"]
fru1, fru2, fru3 = fruits
print("----------------------------------")
print(fruits)
print(f"fru1                    = {fru1}")
print(f"fru2                    = {fru2}")
print(f"fru3                    = {fru3}")



