import numpy as np
B = 20      
H = 0.3      
n = 0.03    
S = 0.0003   
def flujo_manning(B, H, n, S):
    return (1/n) * ((B * H)**(5/3) / (B + 2*H)**(2/3)) * S**(1/2)

Q = flujo_manning(B, H, n, S)
print(f"Flujo Q: {Q:.4f} ")

def derivada_n(B, H, n, S):
    return -flujo_manning(B, H, n, S) / n

def derivada_S(B, H, n, S):
    return flujo_manning(B, H, n, S) / (2 * S)

delta_n = 0.1 * n
delta_S = 0.1 * S

error_rel_n = abs(derivada_n(B, H, n, S)) * (delta_n / n)
error_rel_S = abs(derivada_S(B, H, n, S)) * (delta_S / S)

print(f"Error relativo por n: {error_rel_n:.4f}")
print(f"Error relativo por S: {error_rel_S:.4f}")

if error_rel_n < error_rel_S:
    print("La pendiente S tiene mayor sensibilidad en la predicción del flujo.")
else:
    print("El coeficiente de rugosidad n tiene mayor sensibilidad en la predicción del flujo.")
