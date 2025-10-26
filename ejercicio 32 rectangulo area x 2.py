# zona de clase

class rectangulo:
    # constructor de esfera
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

# zona de codigo principal

def main():
    ultima_longitud = None
    ultimo_ancho = None

    while True:
        print("")
        print("==============================")
        print("===== menu de rectangulo =====")
        print("==============================")
        print("1. calcular area del rectangulo ⏹️.")
        print("2. mostrar datos guardados ♻️.")
        print("3. salir .")
        opciones = input("elija una opcion: ")
        
        if opciones == "1":
            print("")
            longitud = int(input("ingresa la longitud del rectangulo ⏹️ : "))
            ancho = int(input("ingresa el ancho del rectangulo ⏹️ : "))
            figura = rectangulo(longitud,ancho)
            area = figura.calcular_area()
            print(f"el area del rectangulo es ⏹️ : {area}")
            print("")
            ultima_longitud = longitud
            ultimo_ancho = ancho

        elif opciones == "2":
            if ultima_longitud is None or ultimo_ancho is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                figura = rectangulo(longitud,ancho)
                print("")
                print("buscando ultimo calculo de area guardado ⏱️ 🔎")
                print(f"ultima longitud guardada :{longitud}")
                print(f"ultimo ancho guardado :{ancho}")
                print(f"ultimos minutos convertidos {figura.calcular_area()} ")

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