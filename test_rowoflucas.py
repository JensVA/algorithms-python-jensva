from rowoflucas import sumRowOfLucas, isOdd

def test_isOdd():
  number1 = 13
  assert(isOdd(number1) == True)
  number2 = 12
  assert(isOdd(number2) == False)

def test_sumRowOfLucas():
  assert(sumRowOfLucas(11) == 11)   # 2 1 3 4 7|11 18 ...= 1+3+7 = 11
  assert(sumRowOfLucas(60) == 98)   # 2 1 3 4 7 11 18 29 47|76 ... = 1+3+7+11+29+47 = 98