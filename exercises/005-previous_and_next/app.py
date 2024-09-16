# Complete the function to return the previous and next number of a given number
def previous_next(num):
  # Your code here
<<<<<<< HEAD
  num_1 = num - 1 
  num_2 = num + 1
  return num_1, num_2
=======
  num_tupla = num - 1

  return (num_tupla, num_tupla + 2)
>>>>>>> 8a409af7fec795670a1b8294410799688762b8d0


# Invoke the function with any integer as its argument
print(previous_next(179))
