cars = 100 # car number
space_in_a_car = 4.0 #capacity of each car
drivers = 30 # who drive the car
passengers = 90 # who take the car
cars_not_driven = cars - drivers # car without drivers
cars_driven = drivers # cars drivers are driving
carpool_capacity = cars_driven * space_in_a_car # running cars can take how many people
average_passengers_per_car = passengers / cars_driven # each running cars can take how many people


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#Study drills
# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
# my explain: there is not a name 'car_pool_capacity before(line 1-8) but a name 'carpool_capacity'.
# 1. for about floating number, python is int for int and floating for floating
#