# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  dec_num = divmod(num, 10)
  return dec_num


# Invoke the function with any integer
print(tens_digit(854345))
