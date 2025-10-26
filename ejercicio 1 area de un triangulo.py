# zona de clases

class triangulo:
    # constructor de triangulo
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    # declarar funcion 
    def calcular_area(self):
        return (self.base * self.altura) / 2

# zona de codigo principal

def main():
    while True:
        print("")
        print("===== menu de triangulo =====")
        print("1. calcular area de triangulob 📐.")
        print("2. volver a intentar ♻️.")
        print("3. salir .")
        opciones = input("elija una opcion: ")
        
        if opciones == "1" or opciones == "2":
            base = float(input("ingresa la base del triangulo 📐: "))
            altura = float(input("ingresa la altura del triangulo 📐: "))
            figura = triangulo(base,altura) # instancia
            print(f"el area del triangulo es 📐: {figura.calcular_area()}")
        elif opciones == "3":
            print("proceso terminado 😴")
            break
        else:
            print("🚫 opcion no valida")

# ejecucion

if __name__ == "__main__":
    main()



