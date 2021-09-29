class Line:

  def __init__(self, X1, Y1, X2, Y2):
    self.__point1 = [X1, Y1]  
    self.__point2 = [X2, Y2]

  def get_length(self):
    # = sqrt((X2-X1)²+(Y2-Y1)²)
    # first = (X2-X1)²
    first = (self.__point2[0]-self.__point1[0])*(self.__point2[0]-self.__point1[0])
    # second = (Y2-Y1)²
    second = (self.__point2[1]-self.__point1[1])*(self.__point2[1]-self.__point1[1])
    return (first + second)**(1/2)
  
  def getLine(self):
    return "Point 1: [" + str(self.__point1[0]) + ", " + str(self.__point1[1]) + "]    Point 2: [" + str(self.__point2[0]) + ", " + str(self.__point2[1]) + "]"
  
line = Line(0, 0, 0, 8)

print(line.getLine())
print("Length: " + str(line.get_length()))