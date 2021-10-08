from sum import isDivisible, calculateSum

def test_isDivisible():
  assert(isDivisible(8, 4, 2) == True)
  assert(isDivisible(8, 3, 2) == True)
  assert(isDivisible(8, 2, 3) == True)
  assert(isDivisible(8, 3, 3) == False)

def test_calculateSum():
  assert(calculateSum(20, 7, 9) == 48)  # 7+9+14+18 = 48
  assert(calculateSum(10, 2, 3) == 23)  # 2+3+4+6+8 = 23
  assert(calculateSum(100, 25, 15) == 390)  # 15+25+30+45+50+60+75+90 = 390
  