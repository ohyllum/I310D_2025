# calculate the volume of a sphere
def calculate_volume_of_sphere(radius):
    vol = (4/3) * 3.14 * radius * radius * radius
    return vol

radius = calculate_volume_of_sphere(30)
radius2 = calculate_volume_of_sphere(40)
print(radius, radius2)