from classes import wheel, engine, body
#from classes import *

tire = wheel(18)
print(tire.size)

camry_eng = engine(180, 4)
print(camry_eng.horsepower)
print(f"my car's engine has: {camry_eng.n_cylinders} cylinders")

camry_body = body("silver")
print(camry_body.trunk_size)