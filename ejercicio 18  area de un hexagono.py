import math

#zona clase

class hexagono:
    # contructor
    def __init__(self,lado):
        self.lado = lado

    def calcular_area(self):
        return (3 * math.sqrt(3) / 2) * (self.lado ** 2)

#codigo principal

def main():
    ultima_lado = None
    
    while True:
        print("==========================")
        print("==== menu de hexagono ====")
        print("==========================")
        print("1. calcular area del hexagono 💎")
        print("2. muestra ultima area de hexagono ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            lado = int(input("ingresa el lado del hexagono 💎 : "))
            figura = hexagono(lado)
            area = figura.calcular_area()
            print(f"la area del hexagono es 💎 : {area:.2f}")
            ultima_lado = lado
            print("")

        elif opciom == "2":
            if ultima_lado is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                figura = hexagono(lado)
                print("")
                print("buscando area del hexagono reciente 🔎")
                print(f"ultimo lado guardado del hexagono 💎 :{lado}")
                print(f"ultima area de hexagono guardada 💎 : {figura.calcular_area():.2f} ")
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