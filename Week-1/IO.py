# input() function takes input from the user
name = input("Enter your name:")
print("Hello", name)
age = input("Enter your age:")
minimum_age = 5

# type conversion example
# use the int() function to convert age into an integer
age = int(age)
print(age > minimum_age)

error_line = int(name)
