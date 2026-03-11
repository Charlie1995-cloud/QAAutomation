import  sys


# używaj taba nie ; oraz w ten sposób możesz wypisać wersję python.
if 5 < 2:
    print(sys.version)

#Możesz wypisać potrzebne rzeczy w jednej lini pod warunkiem użycia ; pomiędzy
print("Hello"); print("How are you?"); print("Bye bye!")

#W princie możesz używać "" jak i '' - oba zadziałają
print("This will work!")
print('This will also work!')

#print() konczy zawsze z nowa linia ale dodanie , end=" " nie przechodzi do kolejnej lini
print("Hello World!", end=" ")
print("I will print on the same line.")

#Variables
x = 5 # x is of type int
y = "John" # y is of type str
print(x) 
print(y)

#specify the data type of a variable
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#nazwy dostępne
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#wile wartości do wielu zmiennych
x, y, z = "Orange", "Banana", "Cherry"

#jedną wartości na wiele zmiennych
x = y = z = "Orange"

#print x,y,z w jednej komendzie
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

print(x + y + z)

#dodawanie zmiennych int w princie do siebie
x = 5
y = 10
print(x + y)

#Zmienne globalne i localne i wewnątrz finkcji
x = "awesome" #global

def myfunc():
  x = "fantastic"  #local
  print("Python is " + x)

myfunc()

print("Python is " + x)

#aby zmienić zmienna globalną localnie wewnątrz funckji 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)