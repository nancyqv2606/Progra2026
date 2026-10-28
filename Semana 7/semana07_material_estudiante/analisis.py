from sedes import emprendimientos

print("Emprendimientos registradas:", len(emprendimientos))
print("Primer emprendimientos: ", emprendimientos[0]["nombre"])
print("Primer emprendimiento VENTAS", emprendimientos[0]["ventas"])

print("\nANALISIS SEMANAL DE EMPRENDIMIENTOS")


for empre in emprendimientos:
    total sum(empre['ventas'])
    porcentaje = total / empre['meta'] * 100

    if porcentaje >= 100:
        estado = "meta alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "requiere atencion!"

    print(
        f"{empre["nombre"]} | Total: ${total:,.2f} | f"Cumplimiento: {porcentaje:.2f}% | {estado}")
    )