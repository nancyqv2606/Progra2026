"""Micrireto: el portero del café."""

energia = int(input("Cuanta energía tienes de 0-100? :"))
trae_cafe = input("¿traes café? (si/no): ").lower().strip() == "si"
mensaje = "Completa las reglas del portero"

# 1. Si energia < 30 y no trae café -> no entra
if energia < 30 and not (trae_cafe):
    mensaje = "No puedes entrar. menos del 30 y sin café, chao!."
#2. Si energia >= 30 o trae café-> Pasa
elif energia >= 30 or trae_cafe:
    mensaje = "Puede pasar! "
#3 Si es diferente -> portero confundido
else:
    mensaje = "Acceso denegado, revisa las respuestas."
    
print(mensaje)


print("Energia: ", energia)
print("Trae café: ", trae_cafe)

mensaje = "Completa las reglas del portero."

#< 30 energia y no traigo cafe

# TODOS: USA AND PARA DETECTAR ENERGÌA BAJA SIN CAFÉ.
# TODOS: USA OR