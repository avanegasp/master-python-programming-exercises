# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):

  if num > 0:
      c = num % 10
      num = num // 10
      b = num % 10
      a = num // 10

  sum_three = a+b+c

  return sum_three
# Invoke the function with any three-digit number
print(digits_sum(123))
print(digits_sum(854))