# zona de clase

class numeros_A_d:
    #constructor
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def dividir_numeros(self):
            return self.num1 / self.num2

# codigo principal

def main():
    ultimo_num1 = None
    ultimo_num2 = None
    
    while True:
        print("==========================")
        print("==== menu de division ====")
        print("==========================")
        print("1. ingresa dos numeros para hacer una division ➗")
        print("2. muestra ultima division guardada ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            num1 = int(input("ingra el numero 1 a dividir ➗ : "))
            num2 = int(input("ingresa el numero 2 a dividir ➗ : "))
            numero = numeros_A_d(num1,num2)
            division = numero.dividir_numeros()
            print(f"la division total de los dos numeros es ➗ :{division}")
            ultimo_num1 = num1
            ultimo_num2 = num2
            print("")

        elif opciom == "2":
            if ultimo_num1 is None or ultimo_num2 is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                numero = numeros_A_d(num1,num2)
                print("")
                print("buscando ultima division almacenada reciente 🔎")
                print(f"buscando ultimos numeros guardados num1:{num1}  y num2:{num2}")
                print(f"la ultima division guardada es  ➗ : {numero.dividir_numeros()} ")
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