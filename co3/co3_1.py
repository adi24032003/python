import datetime
import math
import random


now = datetime.datetime.now()
print("Current date and time:", now)


number = 9
print("Square root of", number, "is", math.sqrt(number))
print("Pi value:", math.pi)


print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice:", random.choice(["red", "green", "blue"]))
