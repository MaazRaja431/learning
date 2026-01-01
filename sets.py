
common_cars = {"toyota", "honda", "bmw", "audi"}
super_cars = {"ferrari", "lamborghini", "bmw", "audi"}

common = common_cars & super_cars
print("Common cars:", common)


different = common_cars ^ super_cars
print("Different cars:", different)


Universal_cars = common_cars | super_cars
print("Universal cars:", Universal_cars)


new_cars = {"bentley", "mercedes_benz", "mclaren"}
super_cars.update(new_cars)

print("Updated super cars:", super_cars)
