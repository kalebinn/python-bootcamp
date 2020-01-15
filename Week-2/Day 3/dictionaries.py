# Example of a dictionary
my_personal_info = {
    "name" : "Kelvin",
    "DOB" : "01/15/2020",
    "School" : "CCNY",
    "GPA" : 0.5
} 

# Checking if a key exists in a dictionary
if "name" in my_personal_info:
    #print(my_personal_info["name"])
    pass
else:
    #print("its not in the dictionary")
    pass

# print out all the keys in the dictionary:
for key in my_personal_info:
    #print(key)
    pass

# print out all the values in the dictionary (without the key):
for value in my_personal_info.values():
    print(value)



