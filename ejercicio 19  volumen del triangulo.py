# zona de clase

class triangulo:
    # constructor
    def __init__(self,base,altura,ancho):
        self.base = base
        self.altura = altura
        self.ancho = ancho

    def calcular_volumen(self):
        return ((self.base * self.altura) / 2 ) * self.ancho    


#codigo principal

def main():
    ultima_base = None
    ultima_altura = None
    ultimo_ancho = None
    
    while True:
        print("===========================")
        print("==== menu de triangulo ====")
        print("===========================")
        print("1. calcular volumen del triangulo 🔺")
        print("2. muestra ultima volumen del triangulo ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            base = int(input("ingra la base del triangulo 🔺: "))
            altura = int(input("ingresa la altura del triangulo 🔺 : "))
            ancho = int(input("ingresa el ancho del triangulo 🔺 : "))
            figura = triangulo(base,altura,ancho)
            volumen = figura.calcular_volumen()
            print(f"el volumen del triangulo es 🔺 : {volumen:.2f}")
            ultima_base = base
            ultima_altura = altura
            ultimo_ancho = ancho
            print("")

        elif opciom == "2":
            if ultima_base is None or ultima_altura is None or ultimo_ancho is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                figura = triangulo(base,altura,ancho)
                print("")
                print("buscando area del triangulo reciente 🔎")
                print(f"ultima base guardada del triangulo 🔺 :{base}")
                print(f"ultima altura guardada del triangulo 🔺 :{altura}")
                print(f"ultimo ancho guardado del triangulo 🔺 :{ancho}")
                print(f"el ultimo area del triangulo guardada es 🔺 : {figura.calcular_volumen():.2f} ")
                print("")

        elif opciom == "3":
            print("")
            print("programa finalizado 😴")
            break
        else:
            print("")
            print("🚫 opcion invalida.")
            print("")

# ejecucion 

if __name__ == "__main__":
    main()