"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""
dias =["Lunes", "Martes", "Miercoles", "jueves", "viernes"]
ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro) # Total de ventas semanal
cantidad_centro = len(ventas_centro) # Catidad de días registrados

promedio_centro = total_centro / cantidad_centro # Promedio ventas diario
menor_centro = min(ventas_centro)
mayor_centro = max(ventas_centro)
dia_mayor = dias[Ventas_centro.index(mayor_centro)]
print(dia_mayor, mayor_centro)

porcentaje_centro = total_centro * 100 / meta_centro

print(total_centro)
print(porcentaje_centro)

total_norte = sum(ventas_norte) # Total de ventas semanal
cantidad_norte = len(ventas_norte) # Catidad de días registrados

promedio_norte = total_norte / cantidad_norte # Promedio ventas diario
menor_norte = min(ventas_norte)
mayor_centro = max(ventas_norte)

porcentaje_norte = total_norte * 100 / meta_norte

if total_centro > meta_centro:
    estado_centro = "meta superada"
elif total_centro  ==  meta_centro:
    estado_centro  = "meta alcanzada exactamente"
else:
    estadao_centro = "meta NO alcanzada"
    
if total_norte > meta_norte:
    estado_norte = "meta superada"
elif total_norte == meta_norte:
    estado_norte  = "meta alcanzada exactamente"
else:
    estadao_centro = "meta NO alcanzada"   
    
#todo: comparo los totales y rangos.
if total_centro > total_norte:
        tienda_mayor_ventas = 'tienda del centro'
elif total_norte > total_centro:
        tienda_mayor_ventas = 'tienda del Norte'
else:
        tienda_mayor_venta = 'Ambas tiendas tienen el mismo total'
        
print('COMPARACIÓN SEMANAL DE TIENDAS')
print("-" * 70)
print(f"Centro | total: ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} | cumplimiento {porcentaje_centro:.0f}%")
print(f"Centro logro: {estado_centro}\n")
print(f"Norte  | total: ₡{total_norte:,.2f} | meta ₡{meta_norte:,.2f} | cumplimiento {porcentaje_norte:.0f}%")
print(f"Norte logro: {estado_norte}\n")

print("Tienda con mayor ventas:", tienda_mayor_venta)
        

