# zona de clases

class triangulo:
    # constructor de triangulo
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# zona de codigo principal

def main():
    ultima_base = None
    ultima_altura = None

    while True:
        print("")
        print("===== menu de triangulo =====")
        print("1. calcular area de triangulob 📐.")
        print("2. mostrar datos guardados ♻️.")
        print("3. salir .")
        opciones = input("elija una opcion: ")
        
        if opciones == "1":
            print("")
            base = int(input("porfavor ingresa la base del triangulo 📐: "))
            altura = int(input("porfavor ingresa la altura del triangulo 📐: "))
            figura = triangulo(base,altura) # instancia
            print(f"el area del triangulo es 📐: {figura.calcular_area()}")
            print("")
            ultima_base = base
            ultima_altura = altura

        elif opciones == "2":
            if ultima_base is None or ultima_altura is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                figura = triangulo(base,altura)
                print("")
                print("buscando ultimos datos recientes del triangulo📐 🔎")
                print(f"ultima base guardada :{base}")
                print(f"ultima altura guardada :{altura}")
                print(f"ultima area del triangulo guardada 📐 : {figura.calcular_area()} ")

        elif opciones == "3":
            print("")
            print("proceso terminado 😴")
            break
        else:
            print("")
            print("🚫 opcion no valida")
            print("")

# ejecucion

if __name__ == "__main__":
    main()
