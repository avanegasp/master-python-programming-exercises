# Complete the function to return the tens digit and the units digit of any interger
def two_digits(number):
  # Your code here
  split_num = str(number)

  digits = tuple(int(digit) for digit in split_num)
  return digits
   

# Invoke the function with any two digit integer as its argument
print(two_digits(79))
