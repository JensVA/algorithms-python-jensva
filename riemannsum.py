def RightRiemannSum(a, b, aantal):
  deltaX = (b-a)/aantal       # breedte van een rechthoek
  x = a                       # x = huidige x-waarde rechthoek
  opp_totaal = 0.0
  for n in range(0, aantal):  # aantal keer herhalen
    opp_rechthoek = ((x+deltaX)**2 + 1) * deltaX  # f(x) = x² + 1 , (x+deltaX) is voor de Right Riemann sum
    x = x + deltaX            # volgende rechthoek
    opp_totaal = opp_totaal + opp_rechthoek
    n = n + 1
  return opp_totaal

def LeftRiemannSum(a, b, aantal):
  deltaX = (b-a)/aantal       # breedte van een rechthoek
  x = a                       # x = huidige x-waarde rechthoek
  opp_totaal = 0.0
  for n in range(0, aantal):  # aantal keer herhalen
    opp_rechthoek = (x**2 + 1) * deltaX  # f(x) = x² + 1
    x = x + deltaX            # volgende rechthoek
    opp_totaal = opp_totaal + opp_rechthoek
    n = n + 1
  return opp_totaal

def MiddleRiemannSum(a, b, aantal):
  deltaX = (b-a)/aantal       # breedte van een rechthoek
  x = a                       # x = huidige x-waarde rechthoek
  opp_totaal = 0.0
  for n in range(0, aantal):  # aantal keer herhalen
    opp_rechthoek = ((x+(deltaX/2))**2 + 1) * deltaX  # f(x) = x² + 1 , (x+(deltaX/2)) is voor de Middle Riemann sum
    x = x + deltaX            # volgende rechthoek
    opp_totaal = opp_totaal + opp_rechthoek
    n = n + 1
  return opp_totaal


# functie: f(x) = x² + 1
a = 0
b = 2
n = 5

print("functie: f(x) = x² + 1    Interval: [" + str(a) + ", " + str(b) + "]\tn = " + str(n))
print("Oppervlakte R: ", RightRiemannSum(a, b, n))
print("Oppervlakte L: ", LeftRiemannSum(a, b, n))
print("Oppervlakte M: ", MiddleRiemannSum(a, b, n))