# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):

  string_num = str(num)
  int_string_num = string_num[::-1]

  return int(int_string_num)

   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(79))
print(swap_digits(30))
