def apple_sharing(n,k):
  # Your code here
  tuplas = round(k/n)
  moduleTupla = k % n

  return tuplas, moduleTupla
 

print(apple_sharing(6,50))
