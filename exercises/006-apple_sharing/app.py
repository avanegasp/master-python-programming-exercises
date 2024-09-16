def apple_sharing(n,k):
  # Your code here
<<<<<<< HEAD
  r = k / n
  int_r = int(r)
  apples = k % n
  print("*******",apples)
  return int_r,apples
=======
  tuplas = round(k/n)
  moduleTupla = k % n

  return tuplas, moduleTupla
>>>>>>> 8a409af7fec795670a1b8294410799688762b8d0
 

print(apple_sharing(6,50))
