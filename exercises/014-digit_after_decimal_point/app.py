# Complete the function to return the first digit to the right of the decimal point
def first_digit(num):
  first_dec = int((num * 10) % 10)
  return first_dec


# Invoke the function with a positive real number. ex. 34.33
print(first_digit(6.24))
