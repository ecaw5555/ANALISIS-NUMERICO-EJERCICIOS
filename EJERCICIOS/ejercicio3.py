import numpy as np
import math

def f(x):
    return np.log(x)
f0 = f(1)  
f1 = 1     
f2 = -1    
f3 = 2     
f4 = -6    

x = 2.5
x_base = 1
h = x - x_base
taylor_1 = f0 + f1*h
taylor_2 = taylor_1 + (f2 * h**2) / math.factorial(2)
taylor_3 = taylor_2 + (f3 * h**3) / math.factorial(3)
taylor_4 = taylor_3 + (f4 * h**4) / math.factorial(4)

valor_real = f(2.5)
def error_relativo_porcentual(valor_real, valor_aprox):
    return abs((valor_real - valor_aprox) / valor_real) * 100

error_1 = error_relativo_porcentual(valor_real, taylor_1)
error_2 = error_relativo_porcentual(valor_real, taylor_2)
error_3 = error_relativo_porcentual(valor_real, taylor_3)
error_4 = error_relativo_porcentual(valor_real, taylor_4)

print(f"Aproximación primer orden: {taylor_1}, Error: {error_1}%")
print(f"Aproximación segundo orden: {taylor_2}, Error: {error_2}%")
print(f"Aproximación tercer orden: {taylor_3}, Error: {error_3}%")
print(f"Aproximación cuarto orden: {taylor_4}, Error: {error_4}%")
print(f"Valor real: {valor_real}")
