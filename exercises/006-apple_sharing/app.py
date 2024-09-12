def apple_sharing(n,k):
  # Your code here
  r = k / n
  int_r = int(r)
  apples = k % n
  print("*******",apples)
  return int_r,apples
 

print(apple_sharing(6,50))
