# Complete the function to return the total cost in dollars and cents of (n) cupcakes
import math
def total_cost(d, c, n):

    doll_cupcake = d
    cents_cupcake = c
    total_cupcakes = n

    total_doll = doll_cupcake * total_cupcakes
    total_cents = cents_cupcake * total_cupcakes

    total_doll = math.floor(total_doll)
    total_cents = math.floor(total_cents)

    return total_doll, total_cents


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))
