# Nombre del estudiante: Cristian Rodriguez
# Grupo: 213022

# Matriz del inventario
inventario = [
    [201, "Cuadernos", 12, 20],
    [202, "Lapiceros", 30, 25],
    [203, "Carpetas", 5, 15],
    [204, "Marcadores", 18, 18],
    [205, "Resaltadores", 7, 14]
]

# Función para calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


print("===== LISTA DE PEDIDOS =====\n")

# Recorrido de la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock Actual:", stock_actual)
    print("Stock Mínimo:", stock_minimo)
    print("Cantidad a Pedir:", cantidad_pedir)
    print("----------------------------")
