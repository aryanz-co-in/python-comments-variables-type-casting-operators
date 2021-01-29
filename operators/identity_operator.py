#  Identity operator
# "is" and "is not"


living_room_temperature = 23
kitchen_room_temperature = 23

#  is
if living_room_temperature is kitchen_room_temperature:
    print("Temperature is same")
else:
    print("Temperature is NOT same")

living_room_temperature = 18

#  is
if living_room_temperature is kitchen_room_temperature:
    print("Temperature is same")
else:
    print("Temperature is NOT same")

#  is not
if living_room_temperature is not kitchen_room_temperature:
    print("Temperature is NOT same")
else:
    print("Temperature is same")

#  The id of the value must be same
#  It does not compare the value, but it checks if has same id.
name1 = "John"
name2 = name1.lower()
#  name2 = "John"

if name1 is name2:
    print(f"{id(name1)} is {id(name2)}")
else:
    print(f"{id(name1)} is NOT {id(name2)}")

