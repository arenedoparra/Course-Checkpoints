
# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. 
class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

# Crea un objeto usando la clase.
usuario1 = Usuario("Ane", "12345")

# Imprimir los datos del usuario
print("nombre de usuario:", usuario1.nombre_usuario)
print("contraseña:", usuario1.contraseña)