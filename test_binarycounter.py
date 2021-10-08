from binarycounter import BinaryCounter

def test_setValue():
  binary = BinaryCounter()
  binary.setValue(-9)
  assert(binary.get_valueDec() == 0)
  binary.setValue(8)
  assert(binary.get_valueDec() == 8)

def test_increment():
  binary = BinaryCounter()
  binary.setValue(5)
  binary.increment()
  assert(binary.get_valueDec() == 6)
  binary.setValue(15)
  binary.increment()
  assert(binary.get_valueDec() == 0)

def test_decrement():
  binary = BinaryCounter()
  binary.setValue(5)
  binary.decrement()
  assert(binary.get_valueDec() == 4)
  binary.setValue(0)
  binary.decrement()
  assert(binary.get_valueDec() == 15)

def test_getValueBin():
  binary = BinaryCounter()
  assert(str(binary.get_valueBin()) == '0b0')
  binary.setValue(5)
  assert(str(binary.get_valueBin()) == '0b101')
  binary.setValue(15)
  assert(str(binary.get_valueBin()) == '0b1111')
  binary.setValue(1)
  assert(str(binary.get_valueBin()) == '0b1')

def test_getValueHex():
  binary = BinaryCounter()
  assert(str(binary.get_valueHex()) == '0x0')
  binary.setValue(5)
  assert(str(binary.get_valueHex()) == '0x5')
  binary.setValue(15)
  assert(str(binary.get_valueHex()) == '0xf')
  binary.setValue(1)
  assert(str(binary.get_valueHex()) == '0x1')

def test_getValueDec():
  binary = BinaryCounter()
  assert(binary.get_valueDec() == 0)
  binary.setValue(5)
  assert(binary.get_valueDec() == 5)
  binary.setValue(15)
  assert(binary.get_valueDec() == 15)
  binary.setValue(1)
  assert(binary.get_valueDec() == 1)