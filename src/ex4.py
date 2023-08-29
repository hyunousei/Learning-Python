# define cars
cars = 100

# define spaces in a car
spaces_in_car = 4.0

# define number of drivers
drivers = 30

# define number of passengers
passengers = 90

# this will calculate number of cars not driven
cars_not_driven = cars - drivers

# this will calculate number of driven cars
cars_driven = drivers

# calculate how many seat we had per car (excluded drivers)
carpool_capacity = cars_driven * spaces_in_car

# calculate how many passengers we need at least per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")