from classes import wheel, engine, body

class vehicle(wheel, engine, body):
    def __init__(self, horsepower, cylinders, color, w_size=18, num_doors=4):
        # make the engine of the vehicle
        self.engine = engine(horsepower, cylinders)

        # make the tires of the vehicle
        self.front_right_wheel = wheel(w_size)
        self.front_left_wheel = wheel(w_size)
        self.back_right_wheel = wheel(w_size)
        self.back_left_wheel = wheel(w_size)

        # make the body of the vehicle
        self.body = body(color, num_doors)
    
    def drive(self, num_miles):
        print(f"You just drove {num_miles}")
        self.engine.mileage += num_miles
        self.engine.trip_counter += num_miles
    
    def repair(self):
        print(f"Thanks for your repair!")
        self.engine.change_oil()
        self.engine.max_mileage += 100

    def check_mileage(self):
        mileage = self.engine.mileage
        print(f"Your car has {mileage} miles")

camry = vehicle(180, 4, "Silver")
santa_fe = vehicle(280, 4, "Blue", w_size=20)

# check the mileage of our new cars
camry.check_mileage()
santa_fe.check_mileage()

# drive them both a little bit
camry.drive(160)
santa_fe.drive(10)

# check the mileage of our cars after the drive
camry.check_mileage()
santa_fe.check_mileage()

