# Complete the function to return the amount of days it will take to cover a route
import math 

def car_route(n,m):

  km_day = n
  length_km = m

  days = length_km/km_day

  days = math.floor(days)


  return days


# Invoke the function with two integers
print(car_route(20, 40))
