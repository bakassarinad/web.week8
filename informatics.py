# Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.
import math
a =int (input())
b = int(input())
print(math.sqrt(a*a+b*b))

# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере. Пробелы, знаки препинания, заглавные и строчные буквы важны!
a = int(input())
print("The next number for the number " + str(a) + " is " + str(a+1)+".")
print("The previous number for the number " + str(a) + " is " + str (a-1)+".")
# N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?
a = int(input())
b = int(input())

print((b//a))

# N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок останется в корзинке?

a = int(input())
b = int(input())

print((b-(b//a*a)))

# Длина Московской кольцевой автомобильной дороги —109 километров. Байкер Вася стартует с нулевого километра МКАД и едет со скоростью v километров в час. На какой отметке он остановится через t часов?
v = int(input())
t = int(input())
print(v*t % 109)
# Условный оператор
# Даны два целых числа, каждое число записано в отдельной строке.
a = int (input())
b = int(input())
if a>b:
    print(a)
else:
    print(b)
# Требуется определить, является ли данный год високосным. (Напомним, что год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.)
a = int (input())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("YES")
else:
    print("NO")
#В условии одной из задач на этом сайте написано: “Если данное четырехзначное число является симметричным, выведите 1, иначе выведите любое другое целое число”. Для проверки задачи используются заранее подготовленные примеры и правильные ответ на них

#Школьнику кажется, что он решил эту задачу, но тестирующая система почему-то не принимает его решение. Школьник думает, что это происходит оттого, что он выводит не то любое другое число, которое записано в правильных ответах.

#Напишите программу, которая по ответу, записанному в тестирующей системе и по ответу школьника определяет, верно ли школьник решил задачу.
a = int (input())
b = int(input())
if a != 1 and b !=1 or a == 1 and b ==1:
    print("YES")
else:
    print("NO")
# В математике функция sign(x) (знак числа) определена так:
#sign(x) = 1,   если x > 0,
#sign(x) = -1, если x < 0,
#sign(x) = 0,   если x = 0.

#Для данного числа x выведите значение sign(x).
a = int (input())
if a > 0:
    print(1)
elif a < 0:
    print(-1)
else:
    print(0)
# Даны два целых числа, каждое записано в отдельной строке.
a = int(input())
b = int(input())
if a>b:
    print(1)
elif b>a:
    print(2)
else: 
    print(0)
# Циклы for
# Вводятся целые числа a и b. Гарантируется, что a не превосходит b
a = int(input())
b = int(input())
for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end = " ")
# Вводятся 4 числа: a, b, c и d. 
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b+1):
    if i % d == c:
         print(i, end=" ")
# Вводятся целые числа a и b. Гарантируется, что a не превосходит b.
import math
a = int(input())
b = int(input())
for i in range(a, b+1):
    if i == int(math.sqrt(i)) ** 2:
        print(i, end=" ")
# Найдите самый маленький натуральный делитель числа x, отличный от 1 (2 <= x <= 30000).
import math
a = int(input())
for i in range(2, a+1):
    if a % i == 0:
        print(i)
        break
# Выведите все натуральные делители числа x в порядке возрастания (включая 1 и само число).
import math
a = int(input())
for i in range(1, a+1):
    if a % i == 0:
        print(i, end=" ")
# Подсчитайте количество натуральных делителей числа x (включая 1 и само число; x2109).
import math
a = int(input())
sum = 0
for i in range(1, int(math.sqrt(a))):
    if a % i == 0:
        sum += 1
sum *=2
if a % math.sqrt(a) == 0:
    sum+=1

print(sum)
# Вычислите сумму данных 100 натуральных чисел.
import math
sum = 0
for i in range(0, 100):
    i = int(input())
    sum+=i
print(sum)
# Вычислите сумму данных N натуральных чисел.
import math
sum =0
a = int(input())
for i in range(0, a):
    i=int(input())
    sum+=i
print(sum)
# Вводится число N, а затем N чисел.
import math
sum = 0
a = int(input())
for i in range(0, a):
    i = int(input())
    if i == 0:
        sum+=1
print(sum)
# Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.
import math
i = 0
a = int(input())
while i < a:
    i+=1
    if i == (int(math.sqrt(i)) ** 2):
        print(i)
# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

i = 2
a = int(input())
while a % i != 0:
    i+=1
print(i)
# По данному числу N распечатайте все целые степени двойки, не превосходящие N, в порядке возрастания.

# Операцией возведения в степень пользоваться нельзя!
i = 1
a = int(input())
while i <= a:
    print(i, end=" ")
    i*=2
# Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
n = int(input())

i = 0
power = 0
two = 1


while(two < n):
    while(i <= power):
        two *= 2
        i += 1
    power += 1


if(two == n):
    print("YES")
else:
    print("NO")

# По данному натуральному числу N выведите такое наименьшее целое число k, что 2k≥N.

# Операцией возведения в степень пользоваться нельзя!
n = int(input())
i = 1
power = 0
while i < n:
    i*=2
    power+=1
print(power)
# Массивы
# Дан массив, состоящий из целых чисел. Нумерация элементов начинается с 0. Напишите программу, которая выведет элементы массива, номера которых четны (0, 2, 4...).
a = []
n = int(input())
a = [int(s) for s in input().split()]
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i])
# Дан массив, состоящий из целых чисел. Напишите программу, которая выводит те элементы массива, которые являются чётными числами.
a = []
n = int(input())
a = [int(s) for s in input().split()]
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i])
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитывает количество положительных чисел среди элементов массива.
a = []
sum = 0
n = int(input())
a = [int(s) for s in input().split()]
for i in range(len(a)):
    if a[i] > 0:
        sum+=1
print(sum)
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером).
a = []
sum = 0
n = int(input())
a = [int(s) for s in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        sum+=1
print(sum)
# Дан массив, состоящий из целых чисел. Напишите программу, которая определяет, есть ли в массиве пара соседних элементов с одинаковыми знаками.
a = []
answer = "NO"
n = int(input())
a = [int(s) for s in input().split()]
for i in range(1, len(a)):
    if (a[i] >= 0 and a[i-1] >= 0) or (a[i] < 0 and a[i-1] < 0):
       answer = "YES"
    
print (answer)
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
a = []
sum = 0
n = int(input())
a = [int(s) for s in input().split()]
for i in range(1, len(a)-1):
    if (a[i] > a[i-1]  and a[i] > a[i+1]):
       sum+=1
    
print (sum)
# Напишите программу, которая переставляет элементы массива в обратном порядке без использования дополнительного массива. Программа должна считать массив, поменять порядок его элементов, затем вывести результат (просто вывести элементы массива в обратном порядке – недостаточно!)

a = []
sum = 0
j = 0
n = int(input())
a = [int(s) for s in input().split()]
for i in range(len(a)//2):
        temp = a[i]
        a[i] = a[len(a)-i-1]
        
        a[len(a)-i-1] = temp
for i in range(len(a)):
    print(a[i])
# Функции
# Напишите функцию int min (int a, int b, int c, int d) (C/C++), static int min (int a, int b, int c, int d) (Java) function min (a,b,c,d: integer):integer (Pascal), находящую наименьшее из четырех данных чисел.
a, b, c, d = input().split()
def minDef(a, b, c, d):
    result = min(a, b, c, d)
    return result

print(minDef(a, b, c, d))
# Напишите функцию double power (double a, int n) (C/C++), function power (a:real; n:longint): real (Pascal), вычисляющую значение an.
n = input().split()
array = list(map(float, n))

def power(a, n):
    return a ** n


print(power(array[0], array[1]))
#Напишите функцию
#bool Xor (bool x, bool y) (C/C++),
# function _Xor (x, y:boolean): boolean (Pascal),
#def xor(x, y):(Python)
#реализующую функцию "Исключающее ИЛИ" двух логических переменных x и y. Функция Xor должна возвращать true, если ровно один из ее аргументов x или y, но не оба одновременно равны true.
a, b = input().split()

def  xor(x, y):
    if (x != y): 
        return True
    else:
        return False
if (xor(a, b)):
    print(1)
else:
    print(0)







 
