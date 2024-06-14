import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función
f = x**2 + 3*x + 1
        # sp.sin(x) * sp.exp(-x/2)

# Calcular la derivada de la función
f_prime = sp.diff(f, x)

# Calcular la integral de la función
f_integral = sp.integrate(f, x)

# Convertir las funciones simbólicas a funciones numéricas para su evaluación
f_lambdified = sp.lambdify(x, f, 'numpy')
f_prime_lambdified = sp.lambdify(x, f_prime, 'numpy')
f_integral_lambdified = sp.lambdify(x, f_integral, 'numpy')

# Generar puntos x para la evaluación de las funciones
x_vals = np.linspace(0, 10, 400)

# Evaluar las funciones en los puntos x
f_vals = f_lambdified(x_vals)
f_prime_vals = f_prime_lambdified(x_vals)
f_integral_vals = f_integral_lambdified(x_vals)

# Crear el gráfico
plt.figure(figsize=(12, 8))

# Graficar la función original
plt.subplot(3, 1, 1)
plt.plot(x_vals, f_vals, label='f(x) = sin(x) * exp(-x/2)')
plt.title('Función Original')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Graficar la derivada de la función
plt.subplot(3, 1, 2)
plt.plot(x_vals, f_prime_vals, label="f'(x) = Derivada", color='green')
plt.title('Derivada de la Función')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.legend()

# Graficar la integral de la función
plt.subplot(3, 1, 3)
plt.plot(x_vals, f_integral_vals, label="∫f(x) dx = Integral", color='red')
plt.title('Integral de la Función')
plt.xlabel('x')
plt.ylabel('∫f(x) dx')
plt.legend()

# Ajustar el diseño y mostrar el gráfico
plt.tight_layout()
plt.show()

# Mostrar las expresiones de la derivada e integral
print("Función original:")
sp.pprint(f)

print("\nDerivada de la función:")
sp.pprint(f_prime)

print("\nIntegral de la función:")
sp.pprint(f_integral)
