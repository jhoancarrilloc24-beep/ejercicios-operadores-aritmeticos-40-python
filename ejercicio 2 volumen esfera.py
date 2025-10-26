# zona de clase

class esfera:
    # constructor de esfera
    def __init__(self,volumen,radio):
        self.volumen = volumen
        self.radio = radio

# declarar funcion

    def calcular_area(self):
        return (self.volumen * self.radio ** 2)

# zona codigo principal

def main():
    while True:
        print("")
        print("===== menu de esfera =====")
        print("1. calcular area de la esfera 🏐.")
        print("2. volver a realizar ♻️")
        print("3. salir.")

        opcion = input("elije una opcion: ")
        if opcion == "1" or opcion == "2":
            volumen = float(input("ingresa el volumen de la esfera 🏐:"))
            radio = float(input("ingresa el radio de la esfera 🏐:"))
            pelota = esfera(volumen,radio) # instancia
            print(f"el area de la esfera es 🏐: {pelota.calcular_area()}")
        elif opcion == "3":
            print("programa finalizado 😴")
            break
        else:
            print("🚫 opcion no valida")

# ejecucion:

if __name__ == "__main__":
    main()