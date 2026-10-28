"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_norte = sum(ventas_norte) # Total de ventas semanal
cantidad_norte = len(ventas_norte) # Catidad de días registrados

promedio_norte = total_norte / cantidad_norte # Promedio ventas diario
menor_norte = min(ventas_norte)
mayor_centro = max(ventas_norte)

porcentaje_norte = total_norte * 100 / meta_norte
print(total_norte)
print(porcentaje_norte)