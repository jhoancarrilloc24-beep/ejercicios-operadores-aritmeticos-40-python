import math

# zona de clase

class numeros_A_r:
    #constructor
    def __init__(self,num1):
        self.num1 = num1

    def raizx2_numeros(self):
        return math.sqrt(self.num1)

# codigo principal

def main():
    ultimo_num1 = None
    
    while True:
        print("=======================")
        print("==== menu de raiz*2 ====")
        print("=======================")
        print("1. hacer una raiz al cuadrado ")
        print("2. muestra ultima multiplicacion al cuadrado guardada ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            num1 = int(input("ingra el numero: "))
            numero = numeros_A_r(num1)
            raizx2 = numero.raizx2_numeros()
            print(f"resultado de raiz*2 es  :{raizx2}")
            ultimo_num1 = num1
            print("")

        elif opciom == "2":
            if ultimo_num1 is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                numero = numeros_A_r(num1)
                print("")
                print("buscando ultima raiz al cuadrado almacenada reciente 🔎")
                print(f"buscando ultimo numero guardado num:{num1}")
                print(f"la ultima raizx2 guardada es: {numero.raizx2_numeros()}")
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