# zona clase

class conversion:
    #constructor
    def __init__(self,kilometros):
        self.kilometros = kilometros

    def convertir_a_millas(self):
        return self.kilometros * 0.621371    


# zona de codigo principal

def main():
    ultimo_kilometro = None

    while True:
        print("")
        print("==============================")
        print("===== menu de kilometoros =====")
        print("==============================")
        print("1. convertir kilometros a millas 🛣️.")
        print("2. mostrar datos guardados ♻️.")
        print("3. salir .")
        opciones = input("elija una opcion: ")
        
        if opciones == "1":
            print("")
            kilometro = int(input("ingresa los kilometros 🛣️ : "))
            camino = conversion(kilometro)
            millas = camino.convertir_a_millas()
            print(f"las millas son 🛣️: {millas}")
            print("")
            ultimo_kilometro = kilometro

        elif opciones == "2":
            if ultimo_kilometro is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                camino = conversion(kilometro)
                print("")
                print("buscando ultimos kilometros convertidos a millas guardados ⏱️ 🔎")
                print(f"ultimos kilometros guardados :{kilometro}")
                print(f"ultimas millas guardadas {camino.convertir_a_millas()} ")

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