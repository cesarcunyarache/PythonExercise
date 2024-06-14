import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from prettytable import PrettyTable
from sympy import symbols, diff
import math

productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor']
cantidades = np.array([2, 15, 5, 8])
precios = np.array([3090, 90, 150, 450])

# Numpy: Cálculos Numéricos
ingresos_total = sum(cantidades * precios)
media_precios = np.mean(precios)

# Math: Cálculo exponencial de ingresos predichos
ingreso_inicial = ingresos_total
tasa_crecimiento = 0.03
ingresos_predichos = ingreso_inicial * math.exp(tasa_crecimiento * 5)

# Matplotlib: Visualización de Datos
plt.figure()
plt.plot(productos, cantidades, label='Cantidades Vendidas')
plt.legend()
plt.title('Cantidades Vendidas')
plt.xlabel('Productos')
plt.ylabel('Cantidad')
plt.show()


# PrettyTable: Genera tablas simples
table = PrettyTable()
table.field_names = ["Producto", "Cantidad", "Precio"]
for producto, cantidad, precio in zip(productos, cantidades, precios):
    table.add_row([producto, cantidad, precio])


# NetworkX: Manejo y Visualización de Grafos
G = nx.Graph()
for producto, cantidad, precio in zip(productos, cantidades, precios):
    if producto not in G.nodes:
        G.add_node(producto, cantidad_vendida=cantidad, ingreso_total=cantidad*precio)


plt.figure()
node_size = [G.nodes[n]['ingreso_total'] for n in G.nodes()]
nx.draw(G, with_labels=True, node_size=node_size, font_size=10)
plt.show()


# Sympy: Manipulación y Resolución de Expresiones Simbólicas
ventas = list(zip(productos, cantidades, precios))
P = symbols('P')
def demanda(a, b, P):
    return a - b * P

# Calcular las ventas totales para cada producto
ventas_totales = [(producto, cantidad, precio, cantidad * precio) for producto, cantidad, precio in ventas]

# Encontrar el producto con más ventas totales
producto_mas_vendido = max(ventas_totales, key=lambda venta: venta[3])

# Extraer los datos del producto más vendido
nombre_producto, cantidad_inicial, precio_inicial, _ = producto_mas_vendido

# Definir cantidad final y precio final para la elasticidad (pequeña variación)
cantidad_final = cantidad_inicial - 1
precio_final = precio_inicial + 1

# Calcular 'a' y 'b' para la demanda lineal
a = cantidad_inicial
b = (cantidad_final - cantidad_inicial) / (precio_inicial - precio_final)

# Calcular la elasticidad precio de la demanda
elasticidad = diff(demanda(a, b, P), P) * (P / demanda(a, b, P))

# Evaluar la elasticidad en el precio inicial
elasticidad_evaluada = elasticidad.subs(P, precio_inicial)

# Resultados
print(f"Ingresos Totales: {ingresos_total}")
print(f"Media de Precios: {media_precios}")
print(f"Ingresos Predichos en 5 días: {ingresos_predichos}")
print(f"Elasticidad Precio de la Demanda (producto más vendido): {elasticidad_evaluada}")

# Mostrar tabla de ventas
print(table)

