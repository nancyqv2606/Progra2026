"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 6400000
meta_norte = 700000

total_centro = sum(ventas_centro)
cantidad_centro = len(ventas_centro)
print(cantidad_centro)
promedio_centro = total_centro / cantidad_centro
print(promedio_centro)
