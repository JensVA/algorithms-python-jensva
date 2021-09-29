def isOdd(number):    #controleren of number oneven is
  if(number%2 != 0): return True
  return False

upperLimit = 4000000

number1 = 2
number2 = 1
number3 = 3

sum = 1    #we controleren alleen number3, daarom starten we met 1
while(number3 < upperLimit): #we controleren of number 3 niet over z'n limiet gaat
  if(isOdd(number3)): sum = sum + number3 
  number1 = number2   #na het controleren van 3 schuiven we 1 en 2 op en herberekenen we 3
  number2 = number3
  number3 = number1 + number2

print(sum)








