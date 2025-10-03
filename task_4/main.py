import math
x = float(input('Переменная x: '))
y = float(input('Переменная y: '))
z = float(input('Переменная z: '))
b = math.sqrt (10 * (x**1/3) + x**(y+2))*(math.asin(z)**2 - abs(x - y))
print (b)
