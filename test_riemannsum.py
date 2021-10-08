from riemannsum import RightRiemannSum, LeftRiemannSum, MiddleRiemannSum

#source to calculate all the RiemannSum answers: https://www.emathhelp.net/calculators/calculus-2/riemann-sum-calculator/
#round() has been used to change for ex. 3.39999999999 to 3.4 (basically the same answer)

def test_rightRiemann():
  assert(round(RightRiemannSum(0, 2, 4), 2) == 5.75)
  assert(round(RightRiemannSum(0, 10, 50), 2) == 353.4)
  assert(round(RightRiemannSum(-5, 7, 24), 2) == 174.5)

def test_leftRiemann():
  assert(round(LeftRiemannSum(0, 2, 4), 2) == 3.75)
  assert(round(LeftRiemannSum(0, 10, 50), 2) == 333.4)
  assert(round(LeftRiemannSum(-5, 7, 24), 2) == 162.5)

def test_middleRiemann():
  assert(round(MiddleRiemannSum(0, 2, 4), 3) == 4.625)
  assert(round(MiddleRiemannSum(0, 10, 50), 2) == 343.3)
  assert(round(MiddleRiemannSum(-5, 7, 24), 2) == 167.75)