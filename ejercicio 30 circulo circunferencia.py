import math

#zona clase

class circulo:
    # constructor
    def __init__(self,radio):
        self.radio = radio

    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

# zona de codigo principal

def main():
    ultimo_radio = None

    while True:
        print("")
        print("===========================")
        print("===== menu de circulo =====")
        print("===========================")
        print("1. calcular circunferencia del circulo 🏐.")
        print("2. mostrar datos guardados ♻️.")
        print("3. salir .")
        opciones = input("elija una opcion: ")
        
        if opciones == "1":
            print("")
            radio = int(input("ingresa el radio del circulo 🏐 : "))
            figura = circulo(radio)
            circunferencia = figura.calcular_circunferencia()
            print(f"la circunferencia del circulo es 🏐: {circunferencia}")
            print("")
            ultimo_radio = radio

        elif opciones == "2":
            if ultimo_radio is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                figura = circulo(radio)
                print("")
                print("buscando ultimos datos recientes del circulo 🏐 🔎")
                print(f"ultima radio guardado :{radio}")
                print(f"ultima circunferencia guardada {figura.calcular_circunferencia()} ")

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