# Complete the function to return the previous and next number of a given number
def previous_next(num):
  # Your code here
  num_tupla = num - 1

  return (num_tupla, num_tupla + 2)


# Invoke the function with any integer as its argument
print(previous_next(179))
