# zona clase

class cubo:
    #constructor
    def __init__(self,longitud_lado):
        self.longitud_lado =longitud_lado
        
    def calcular_volumen(self):
        return self.longitud_lado ** 3
    
# zona codigo principal

def main():
    ultimo_lado = None
    
    while True:
        print("==========================")
        print("==== menu de cubo ====")
        print("==========================")
        print("1. calcular volumen ◻")
        print("2. mostrar ultimo volumen guardado ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            longitud_lado = int(input("ingresa el lado del cubo ◻ : "))
            figura = cubo(longitud_lado)
            volumen = figura.calcular_volumen()
            print(f"el volumen del cubo es ◻ : {volumen:.2f}")
            ultimo_lado = longitud_lado
            print("")

        elif opciom == "2":
            if ultimo_lado is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                figura = cubo(longitud_lado)
                print("")
                print("buscando centimetros convertidos 🔎")
                print(f"el lado guardado del cubo es ◻ :{longitud_lado}")
                print(f"el ultimo volumen del cubo guardado es ◻ : {figura.calcular_volumen():.2f} ")
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