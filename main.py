var_int = 70
var_float = 8.4
var_str = "No"
big_int35 = var_int * 3.5
var_float = var_float - 1
var_int/var_float and big_int35/var_float
var_str = var_str * 3 + "Yes" * 2
print(var_int, var_float, var_str, big_int35 )

k = int(input('Количесвто яблок: '))
n = int(input('Количесвто школьников: '))
everyshk_yablk = k // n
korzina = k % n
print("На каждого школьника столько яблок: ", everyshk_yablk, "В корзине останется: ", korzina )

x = int(input('Введите обьем шара, куб. ед.: '))
pi = 3.1415926
r = (pow((3*x), 1/3)/(4*pi))
print(r)

import math
x = int(input('Переменная x: '))
y = int(input('Переменная y: '))
f = abs(pow(x, y/x)-pow(y/x, 1.0/3)) + (y-x)
print (f)

min_in_day = 24 * 60
n = int(input('Столько минут прошло с начала суток: '))
min = n % min_in_day
hours = min // 60 
minutes = min % 60 
print ('Время:', hours, minutes)