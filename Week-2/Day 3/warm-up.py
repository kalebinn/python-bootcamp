import math

def cyl_volume(h,r):
    volume = math.pi * (r**2) * h
    return volume

print(cyl_volume(1, 1))

def cone_volume(h,r):
    volume = (h/3) * math.pi * (r**2)
    return volume

print(cone_volume(1,1))
print(f"1/3 pi = {math.pi/3}")