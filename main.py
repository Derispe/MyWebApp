import math
A = int(input())
B = int(input())
C = int(input())
x1 = 0
x2 = 0
discriminant = B**2-4*A*C
if discriminant > 0 :
    x1 =-((B+math.sqrt(discriminant))/(2*A))
    x2 =-((B-math.sqrt(discriminant))/(2*A))
    print("Корни квадратного уравнения: \n", "Первый корень = ", round(x1), "\n", "Второй корень = ", round(x2))
if discriminant == 0 :
    x1 = -( B/(2*A))
    print('Корни квадратного уравнения: \n', "Первый корень = ", round(x1), "\n", "Второй корень = ", round(x1))
if discriminant < 0 :
    print('Корней не существует')