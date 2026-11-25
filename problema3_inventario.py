# ==============================================================================
# UNAD - Fundamentos de Programación (213022)
# Fase 5 - Evaluación Final POA
# Problema 3: Control de inventario y reabastecimiento
# Estudiante: Elys María Ramos Trujillo
# ==============================================================================

# Matriz inicial: [Código del artículo, Nombre del artículo, Stock actual, Stock mínimo requerido]
INVENTARIO = [
    ["ART-001", "Caja corrugada sencilla", 120, 150],
    ["ART-002", "Cinta de embalaje 48mm", 45, 30],
    ["ART-003", "Plancha de cartón CB", 80, 80],
    ["ART-004", "Esquinero protector", 25, 60],
    ["ART-005", "Film estirable industrial", 12, 20],
    ["ART-006", "Etiqueta adhesiva térmica", 200, 100],
]


def calcular_cantidad_a_pedir(stock_actual: int, stock_minimo: int) -> int:
    """Calcula la cantidad exacta a pedir para reabastecer un artículo.

    Args:
        stock_actual: Unidades disponibles actualmente.
        stock_minimo: Unidades mínimas requeridas en inventario.

    Returns:
        Cantidad a pedir: stock_minimo - stock_actual si stock_actual < stock_minimo;
        de lo contrario, 0.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def generar_reporte_reabastecimiento(matriz_inventario: list) -> None:
    """Muestra el nombre de cada artículo y la cantidad exacta a solicitar."""
    print("\n--- REPORTE DE REABASTECIMIENTO DE INVENTARIO ---")
    for articulo in matriz_inventario:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"Artículo: {nombre} | Cantidad a pedir: {cantidad_pedir}")


if __name__ == "__main__":
    generar_reporte_reabastecimiento(INVENTARIO)