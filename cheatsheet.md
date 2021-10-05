# Cheatsheet Python

A cheatsheet made by Jens Vanhove for `Python` based on `C#`

```C#
// First codeblock will be C# 
```

```python
# Second codeblock will be Python
```

## Decisions

### If Statements

```C#
if (number > 8 || number < -3)
{
  Console.WriteLine("Good");
}
```

```python
if (number > 8 or number < -3):
  print("Good")
```

---

### If-else Statements

```C#
if (score < 70 && score >= 0)
{
  Console.WriteLine("Work a little harder");
}
else
{
  Console.WriteLine("Good job!");
}
```

```python
if (score < 70 and score >= 0):
  print("Work a little harder")
else:
  print("Good job!")
```

---

### If-elseif-else Statements

```C#
if (score >= 90)
{
  Console.WriteLine("Good Job!");
}
else if (score >= 30)
{
  Console.WriteLine("Work a little harder.");
}
else
{
  Console.WriteLine("Rip.");
}
```

```python
if (score >= 90):
    print("Good Job!")
elif (score >= 30):
    print("Work a little harder.")
else:
    print("Rip.")
```

## Loop Statements

### For loop

```C#
for (int i = 0; i < 10; i+=2)
{
  Console.WriteLine(i + ": Hello");
}
```

```python
for i in range(0,10,2):
  print(str(i) + ": Hello")
```

---

### While loop

```C#
while (count < 10)
{
  Console.WriteLine("Count still less than 10");
}
```

```python
while count < 10:
  print("Count still less than 10")
```

---

### Do while loop

```C#
do
{
  Console.Write("Do something before checking:");
} while (count > 15);
```

```python
# Do while loops do not exist in Python, however...you can emulate them.
while True:
    print("Do something before checking:")
    if count > 15:
        break
```

## Data structures

### Array/List

```C#
int[] empty_array = new int[10];
int[] filled_array = { 10, 11, 12, 13 };
empty_array[3] = 5;    //Assigning a value
number = filled_array[1];  //number = 11
Console.WriteLine(empty_array.Length());  //Prints the length
```

```python
filled_array = [10, 11, 12, 13]
filled_array.append(14)   #Adding an element to the list
print(len(filled_array))  #Prints the length
```

---

### Iteration over a List/Array

```C#
int[] filled_array = { 10, 11, 12, 13 };
foreach (var number in filled_array)
{
  Console.WriteLine(number);
}
```

```python
filled_array = [10, 11, 12, 13]
for number in filled_array:
  print(number)
```

## Functions

### Creating a function

```C#
static void SayHello()
{
  Console.WriteLine("Hello there.");
}
```

```python
def SayHello():
  print("Hello there.")
```

## Classes

### Creating Classes

```C#
namespace YourChoice
{
  class Point
  {
    //Class declaration
  }
}
```

```python
class Point:
  #Class declaration
```

---

### Class Methods

```C#
public void Move(double toX, double toY) {
  x = toX;
  y = toY;
}
```

```python
def Move(self, double toX, double toY):
  self.__x = toX
  self.__y = toY
```

---

### Default Constructor

```C#
public Point()  
{
  x = 0;
  y = 0;
}
```

```python
def __init__(self):
  self.__name = "Unnamed"
```

---

### Constructor Overloading

```C#
public Point(name) {
  this.name = name;
}
```

```python
def __init__(self, name):
  self.__name = name
```

---

### Declaring attributes

```C#
private double x = 0;
private double y = 0;
```

```python
# In python, you don't need to declare attributes before using them.
# To assign or access attributes, use: self.__<name_of_attribute>
# __ is the same as private in C#, it's not accessable outside of the scope of the class.
```

---

### Creating Objects

```C#
Point point = new Point();
```

```python
point = Point()
```

### Calling methods

```C#
point.Move(8.4, 9.5);
```

```python
point.Move(8.4, 9.5)
```
