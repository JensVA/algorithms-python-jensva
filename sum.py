def isDivisible(number, x, y):   #controleren of number deelbaar is door x of y
  if(number%x == 0 or number%y==0): return True
  return False

upperLimit = 10000
sum = 0
for i in range(1, upperLimit-1):
  if(isDivisible(i, 7, 9)): sum = sum + i

print(sum)
