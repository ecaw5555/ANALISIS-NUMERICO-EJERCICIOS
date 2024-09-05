import numpy as np
sigma = 5.67e-8 
A = 0.15  
e = 0.90  
T = 650 
delta_T = 20 
H = e * sigma * A * (T ** 4)
H_650_plus = e * sigma * A * ((T + delta_T) ** 4)
H_650_minus = e * sigma * A * ((T - delta_T) ** 4)

error_relative_plus = abs((H_650_plus - H) / H) * 100
error_relative_minus = abs((H_650_minus - H) / H) * 100

print(f"H (T=650 K) = {H:.2f} W")
print(f"Error relativo con T=650+20 K: {error_relative_plus:.2f}%")
print(f"Error relativo con T=650-20 K: {error_relative_minus:.2f}%")

delta_T_new = 40  # K
H_650_plus_new = e * sigma * A * ((T + delta_T_new) ** 4)
H_650_minus_new = e * sigma * A * ((T - delta_T_new) ** 4)

error_relative_plus_new = abs((H_650_plus_new - H) / H) * 100
error_relative_minus_new = abs((H_650_minus_new - H) / H) * 100

print(f"Error relativo con T=650+40 K: {error_relative_plus_new:.2f}%")
print(f"Error relativo con T=650-40 K: {error_relative_minus_new:.2f}%")
