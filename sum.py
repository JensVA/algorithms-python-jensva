def isDivisible(number, x, y):   #controleren of number deelbaar is door x of y
  if(number%x == 0 or number%y==0): return True
  return False

def calculateSum(limit, number1, number2):
  upperLimit = limit
  sum = 0
  for i in range(1, upperLimit-1):
    if(isDivisible(i, number1, number2)): sum = sum + i
  return sum

print(calculateSum(10000, 7, 9))
