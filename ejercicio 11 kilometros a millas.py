# zona calses
class convertir_kilometros:
    # construtor
    def __init__(self,kilometros):
        self.kilometros = kilometros

    def convertir_k_a_millas(self):
        return self.kilometros * 0.621371

# zona de código principal
def main():
    ultima_kilometros = None

    while True:
        print("============================")
        print("==== menu de kilometros ====")
        print("============================")
        print("1. convertir kilometros a millas 🛣️")
        print("2. mostrar ultimos kilometros convertidos ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            kilometros = float(input("ingresa la longitud del trapecio : "))
            convertir = convertir_kilometros(kilometros)
            millas = convertir.convertir_k_a_millas()
            print(f"las millas son: {millas:.2f}")
            ultima_kilometros = kilometros

        elif opciom == "2":
            if ultima_kilometros is None:
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
            else:
                convertir = convertir_kilometros(kilometros)
                print("buscando kilometros convertidos a millas 🔎")
                print(f"ultimos kilometros convertidos a millas 🛣️ : {kilometros}")
                print(f"ultima convercion de kilometros a millas 🛣️ : {convertir.convertir_k_a_millas():.2f} ")

        elif opciom == "3":
            print("programa finalizado 😴")
            break

        else:
            print("🚫 opcion invalida.")

# ejecucion 

if __name__ == "__main__":
    main()