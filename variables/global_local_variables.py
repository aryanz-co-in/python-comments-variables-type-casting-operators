# Global and Local variables


index = 2  # Global variable - used through out the entire code


def print_fruit():
    fruits = ["Apple", "Banana", "Orange"]  # Local variable - Used within the function
    if index < len(fruits):
        print(fruits[index])


print(f"Index = {index}")
print_fruit()
