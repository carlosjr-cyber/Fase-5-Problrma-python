# Nombre  del estudiante: Carlos Alberto Córdoba Mosquera
# Grupo: 213022_192
# Programa: Ingenieria de sistemas
# Código Fuente: autoría propia
# Evaluación Final Fase 5

# ----------------------------
# RESTAURANTE LA CIRIACA
# "La Ciriaca" es un restaurante donde se pueden encontrar comidas tipicas chocoanas. El restaurante tiene una promoción especial para los platos fuertes: si el precio base de un plato fuerte es mayor a $20,000, se aplica un descuento del 15%, esto con el fin de que los clientes puedan disfrutar de sus platos fuertes a un precio más accesible.

# # --------------------------
# Matriz: [Nombre, Categoría, Precio Base]
menu_restaurante = [
    ["Patacon con queso", "Entrante", 12000],
    ["Sopa de queso", "Entrante", 8500],
    ["arroz atollado", "Plato Fuerte", 35000],
    ["bocachico sudado", "Plato Fuerte", 22500],
    ["cocadas", "Postre", 10000],
    ["Helado de badea", "Postre", 6000]
]

# Parámetros de la promoción
categoria_objetivo = "Plato Fuerte"
umbral_precio = 20000
descuento = 0.15  # 15%

# --------------------------
# MÓDULO 2: Función para calcular precio final
# --------------------------
def calcular_precio_final(categoria, precio_base):
    """
    Calcula el precio final aplicando la promoción si corresponde.
    """
    # Lógica de negocio
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        precio_final = precio_base * (1 - descuento)
    else:
        precio_final = precio_base
    
    return round(precio_final, 2)  # Redondear a 2 decimales para moneda

# --------------------------
# MÓDULO 3: Mostrar resultados
# --------------------------
print("=== RESUMEN DE PRECIOS - MENÚ DEL RESTAURANTE ===")
print(f"Promoción: 15% de descuento en '{categoria_objetivo}' con precio mayor a {umbral_precio}\n")

# Recorremos la matriz y calculamos para cada producto
for producto in menu_restaurante:
    nombre, categoria, precio_base = producto
    precio_final = calcular_precio_final(categoria, precio_base)
    
    # Salida formateada
    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio Base: ${precio_base:,}")
    print(f"Precio Final: ${precio_final:,}")
    print("-" * 50)