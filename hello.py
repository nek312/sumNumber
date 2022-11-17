from cmath import sqrt
from re import S
from sys import flags
from unicodedata import digit
import math

print ('Задача 1.1 запрашивает с клавиатуры три целых числа, и выводит на экран произведение данных чисел')
print (' ')
a = input('Enter num1: ')
b = input('Enter num2: ')
c = input('Enter num3: ')

print (int(a)*int(b)*int(c))


print (' ')

print ('Задача 1.2 запрашивает с клавиатуры три целых числа, и выводит на экран сумму данных чисел в прямом и обратном порядке. Например, сумма равна 123, в обратном порядке 321.')
print (' ')

a = input('Enter num1: ')
b = input('Enter num2: ')
c = input('Enter num3: ')
m = int(a)+int(b)+int(c)
print (m)

z =  str(m)
z2 = z[::-1]
print ('Наоборот:', z2)
print (' ')


print (' Задача 2.1 найти периметр прямоугольного треугольника по двум катетам a, b.')
print (' ')
a = input('Enter a: ')
b = input('Enter b: ')
c = int(a)*int(a) + int(b)*int(b)
sqrt = math.sqrt(c)
print('Третья сторона равна с =',int(sqrt))
p = int(sqrt)+int(a)+int(b)
print('Периметр равен a+b+c=',p)
print (' ')


print ('Задача 2.2 найти ребро куба, площадь полной поверхности которого равна S')
print (' ')
a = input('Enter S: ')
h = int(a)/6
sqrt = math.sqrt(h)
print('Площадь равна S=',a)
print('Ребро равно h=', int(sqrt))


print (' ')

print ('Задача 3.1 найти наименьшую цифру в натуральном двухзначном числе')
print (' ')
x = input('Enter num: ')
z = int(x)/10
z2 = int(x)%10
if int(z) > z2:
  print (int(z), '>', z2)
if int (z2) > z:
 print (int(z), '<', z2)
elif int(z) == z2:
  print (int(z), '=', (z2) )


print (' ')

print ('Задача 3.2 кратна ли трем сумма цифр двухзначного числа')
print (' ')
x = input('Enter num: ')
z = int(x)/10
z2 = int(x)%10
z3 = int(z) + int(z2) 

if int(z3) % 3 == 0:
  z4 = int(z3) / 3
  print('Да делится ответ:', z4)
else:
  print(' не делится')


print (' ')

print ('Задача 3.3 кратна ли числу А. Cумма цифр двухзначного числа')
print (' ')
x = input('Enter num: ')
y = input('Enter число А: ')
z = int(x)/10
z2 = int(x)%10
z3 = int(z) + int(z2) 
z4 = int(z3) / int(y)

if int(z3) % int(y) == 0:
  print('Да делится ответ:', int(z4))
else:
  print(z3, ' не делится на',y)


print (' ')
print ('Задача 3.4 какая из цифр трехзначного числа больше: первая или последняя.')
print (' ')
x = input('Enter num: ')
z = int(x)/100
z3 = int(int(x)/10)%10
z2 = int(x)%10

if int(z) > z2:
  print (int(z), '>', z2,)
if int (z2) > z:
 print (int(z), '<', z2)
elif int(z) == z2:
  print(int(z),'=',z2)

print (' ')
print (' Все ли цифры трехзначного числа одинаковые')
x = input('Enter num: ')
z = int(x)/100
z3 = int(int(x)/10)%10
z2 = int(x)%10

if int(z) == z2 == z3:
  print (int(z), '=', (z3), '=', (z2) )
else:
  print('Они неравны')

x = input('Enter: ')

if True != x.isdigit():
  print('lol')
elif len(x) != 6:
  print('lol')

first_3 = x[:3]
second_3 = x[3:]

First = int(first_3)
Second = int(second_3)

sum3 = First % 10
sum2 = int(First / 10) % 10
sum1 = int(First / 100)

sum3_s = Second % 10
sum2_s = int(Second/ 10) % 10
sum1_s = int(Second / 100)

sumFirst = sum1 + sum2 + sum3
sumSecond = sum1_s + sum2_s + sum3_s
print(sumFirst, sumSecond)


