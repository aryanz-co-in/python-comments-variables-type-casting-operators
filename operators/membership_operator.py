#  Membership operators
# "in" and "not in"

# Mostly used to check if an item is available in the list/collection of items.

# in

fruits = ["Apple", "Banana", "Watermelon", "Grapes", "Blue berry", "Pineapple"]
apple = "Apple"


if apple in fruits:
    print(f"{apple} is available in fruits list : \n{fruits}")
else:
    print(f"{apple} is NOT available in fruits list : \n{fruits}")

print("\n")


# not in

vegetables = ("Onion", "Potato", "Eggplant", "Drum stick")
tomato = "Tomato"


if tomato not in vegetables:
    print(f"{tomato} is NOT available in vegetable tuple : \n{vegetables}")
else:
    print(f"{tomato} is available in vegetable tuple : \n{vegetables}")


