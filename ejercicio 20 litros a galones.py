# zona de clase

class convertir_litros:
    # constructor
    def __init__(self,litros):
        self.litros = litros

    def litros_a_galones(self):
        return self.litros * 0.264172   

#codigo principal

def main():
    ultimo_litro = None
    
    while True:
        print("========================")
        print("==== menu de litros ====")
        print("========================")
        print("1. canvertir litros a galones 🥛")
        print("2. muestra ultimo galon guardado ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            litros = int(input("ingra los litros 🥛 : "))
            agua = convertir_litros(litros)
            galones = agua.litros_a_galones()
            print(f"los galones son 🥛 : {galones:.2f}")
            ultimo_litro = litros
            print("")

        elif opciom == "2":
            if ultimo_litro is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                agua = convertir_litros(litros)
                print("")
                print("buscando ultimos galones almacenados reciente 🔎")
                print(f"buscando ultimos litros guardados 🥛 :{litros}")
                print(f"los ultimos galones guardados son 🥛 : {agua.litros_a_galones():.2f} ")
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