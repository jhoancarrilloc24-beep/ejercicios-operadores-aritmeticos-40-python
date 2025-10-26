# zona clase

class cuadrado:
    # constructor 
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return self.lado ** 2
    
# codigo principal    
    
def main():
    ultimo_lado = None

    while True:
        print("==========================")
        print("==== menu de cuadrado ====")
        print("==========================")
        print("1. calcular volumen del cuadrado ◻")
        print("2. mostrar ultimo volumen del cuadrado ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            lado = int(input("ingresa el numero del lado : "))
            figura = cuadrado(lado)
            area = figura.calcular_area()
            print(f"el volumen es: {area:.2f}")
            ultimo_lado = lado

        elif opciom == "2":
            if ultimo_lado is None:
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
            else:
                figura = cuadrado(lado)
                print("buscando volumen del cuadrado 🔎")
                print(f"ultimo lado ingresado del cuadrado ◻ : {lado}")
                print(f"ultimo volumen guardado del cuadrado ◻ : {figura.calcular_area():.2f} ")

        elif opciom == "3":
            print("programa finalizado 😴")
            break

        else:
            print("🚫 opcion invalida.")

# ejecucion 

if __name__ == "__main__":
    main()