# zona de clase

class rectangulo:
    # constructor de esfera
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho

# declarar funcion

    def calcular_area(self):
        return self.longitud * self.ancho

# zona codigo principal

def main():
    while True:
        print("")
        print("===== menu de rectangulo =====")
        print("1. calcular area de la rectangulo ⏹️.")
        print("2. volver a realizar ♻️")
        print("3. salir.")

        opcion = input("elije una opcion: ")
        if opcion == "1" or opcion == "2":
            longitud = float(input("ingresa el volumen de la rectangulo ⏹️ :"))
            ancho = float(input("ingresa el radio de la rectangulo ⏹️ :"))
            figura = rectangulo(longitud,ancho)
            print(f"el area del rectangulo es ⏹️ : {figura.calcular_area()} unidades cuadradas.")
        elif opcion == "3":
            print("programa finalizado 😴")
            break
        else:
            print("🚫 opcion no valida")

if __name__ == "__main__":
    main()