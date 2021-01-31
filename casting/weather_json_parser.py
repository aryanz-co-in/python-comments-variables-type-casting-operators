# Program to read file containing JSON object for weather

# Inorder to read and parse JSON, we need to use the json module from python
import json

weathers = []  # declaring empty list
weather_value = None # Will be using this variable to store the type casted value

print("Started Reading JSON file")
with open('weather.json') as f:  # Reading file
    for jsonObj in f:   # reading lines from the file
        weather = json.loads(jsonObj)   # parsing and storing the line
        weathers.append(weather)    # adding the line to the list

print("Printing each JSON Decoded Object")
for weather in weathers:    # Traversing through the list
    print(weather)
    print(f"Type of weather is: {type(weather['weather'])}")
    weather_value = int(weather["weather"]) # Type casting from string to int
    # print(weather["id"], weather["city"], weather["weather"], weather["unit"])


print(f"{weather_value}° C")
print(type(weather_value))


fahrenheit = (weather_value * 9/5) + 32

print(f"Fahrenheit {fahrenheit}")

