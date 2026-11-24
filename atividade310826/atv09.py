from math import pi
height = float(input("Enter the height: "))
ray = float(input("Enter the ray: "))

volume = (pi * (ray * ray) * height) / 3
print(f"The volume is: {volume:.2f}")
