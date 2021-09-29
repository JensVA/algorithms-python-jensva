class BinaryCounter:

  def __init__(self):
    self.__value = 0
    self.__led0 = 0
    self.__led1 = 0
    self.__led2 = 0
    self.__led3 = 0

  def __initLeds(self, newValue):
    if(newValue & 0b0001): self.__led0 = 1
    else: self.__led0 = 0
    if(newValue & 0b0010): self.__led1 = 1
    else: self.__led1 = 0
    if(newValue & 0b0100): self.__led2 = 1
    else: self.__led2 = 0
    if(newValue & 0b1000): self.__led3 = 1
    else: self.__led3 = 0

  def increment(self):
    if(self.__value < 15): self.__value = self.__value + 1
    self.__initLeds(self.__value)

  def decrement(self):
    if(self.__value > 0): self.__value = self.__value - 1
    self.__initLeds(self.__value)

  def setValue(self, value):
    if(self.__value >= 0 and self.__value <= 15): self.__value = value
    self.__initLeds(self.__value)

  def get_valueBin(self):
    return bin(self.__value)
  
  def get_valueHex(self):
    return hex(self.__value)

  def get_valueDec(self):
    return self.__value
  
  def get_ledStatus(self):
    return "led3: " + str(self.__led3) + ",  led2: " + str(self.__led2) + ",  led1: " + str(self.__led1) + ",  led0: " + str(self.__led0)


binaryValue = BinaryCounter()

binaryValue.setValue(6)
binaryValue.increment()

print("Decimal value: " + str(binaryValue.get_valueDec()))
print("Binary value: " + str(binaryValue.get_valueBin()))
print("Hexadecimal value: " + str(binaryValue.get_valueHex()))
print(binaryValue.get_ledStatus())
