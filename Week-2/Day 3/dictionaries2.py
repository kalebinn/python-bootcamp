def find_avg_year(years):
    sum = 0
    for year in years:
        sum += year
    return int(sum/len(years))

def find_avg_year_short(years):
    return int(sum(years)/len(years))


list_of_cars = ["toyota", "ford", "BMW", "audi", "benz"]
list_of_models = ["Camry", "F150", "i8", "A4", "S550"]

car = {
    "make" : list_of_cars,
    "model" : list_of_models,
    "years" : [2010, 2017, 2020, 2006, 2020]
}

for key in car:
    #print(key)
    pass

car_years = car["years"]
#print(car_years)
# small challenge: Find the average years the cars were produced
# trunate it to an integer
# try using a function. 
avg_year = find_avg_year(car_years)
#print(f"The average year of all the cars is: {avg_year}")

car_colors = ["red", "blue", "black", "blue", "silver"]
car["color"] = car_colors

for key in car:
    #print(key)
    pass

for value in car.values():
    #print(value)
    pass

# small excercise:
# try to add the stock numbers into the dictionary
# say you have 3 cameries, 5 fords, 6 BMWs, 1 Audi, and 3 Benz
car["Num in stock"] = [3, 5, 6, 1, 3]

for key in car:
    #print(key)
    pass

# print all the values stored in this dictionary
for value in car.values():
    #print(value)
    pass

# tiny excercise: Tell me how many cars we have in stock by accessing
# the "num in stock" key from the dictionary
inventory = car['Num in stock']
print(f"we have {sum(inventory)} in stock!")
# print(f"we have {sum(car['Num in stock'])} in stock!")

#print(f"We have {inventory} cars in stock!")
#car["dealers"] = ["Amy", "Bob", "Charlie", "Dylan", "Elephant"]

for key in car:
    pass
    #print(key)

#print("Firing all the dealers ... ")
#car.pop("dealers")
#for key in car:
#    print(key)
#car["dealers"].clear()
print(car)
print("\n we're going to close our dealership")
car.clear() # erase the contents of the dicionary
print(car)
del car # delete the whole dictionary
# print(car) 

