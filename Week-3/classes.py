class wheel:
    def __init__(self, diameter, wtype="all-weather"):
        self.size = diameter
        self.type = wtype

class engine:
    def __init__(self, horsepower, n_cylinders):
        self.horsepower = horsepower
        self.n_cylinders = n_cylinders

        self.is_healthy = True 
        self.need_oil_change = False 
        self.trip_counter = 0 
        self.mileage = 0
        self.max_mileage = 150000
    
    def check_health(self):
        if self.mileage > self.max_mileage:
            self.is_healthy = False 
            print("Our engine is breaking")

        if self.trip_counter >= 3000:
            self.is_healthy = False
            self.need_oil_change = True
            if self.trip_counter >= 15000:
                self.mileage = self.max_mileage
                print("I'm dead cause you were lazy")
            elif self.trip_counter >= 6000:
                print("I'm going to die if you don't change my oil")
            else:
                print("Change your oil!")

    def change_oil(self):
        print("Thanks for changing your oil")
        self.trip_counter = 0
        self.need_oil_change = False
        self.is_healthy = True 
        
class body:
    def __init__(self, color, num_doors=4):
        self.num_doors = num_doors
        self.color = color
        
        if self.num_doors == 0:
            self.trunk_size = "tiny"
        elif self.num_doors == 2:
            self.trunk_size = "small"
        elif self.num_doors == 4:
            self.trunk_size = "med"
        elif self.num_doors >= 5:
            self.trunk_size = "large"

    

