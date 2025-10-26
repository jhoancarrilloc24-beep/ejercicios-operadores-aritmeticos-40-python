# zona de clase

class numeros_A_r:
    #constructor
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def restar_numeros(self):
        return self.num1 - self.num2

# codigo principal

def main():
    ultimo_num1 = None
    ultimo_num2 = None
    
    while True:
        print("=======================")
        print("==== menu de resta ====")
        print("=======================")
        print("1. ingresa dos numeros para hacer una resta ➖")
        print("2. muestra ultima suma guardada ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            num1 = int(input("ingra el numero 1 a restar ➖ : "))
            num2 = int(input("ingresa el numero 2 a restar ➖ : "))
            numero = numeros_A_r(num1,num2)
            restar = numero.restar_numeros()
            print(f"la resta total de los dos numeros es ➖ :{restar}")
            ultimo_num1 = num1
            ultimo_num2 = num2
            print("")

        elif opciom == "2":
            if ultimo_num1 is None or ultimo_num2 is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                numero = numeros_A_r(num1,num2)
                print("")
                print("buscando ultima resta almacenada reciente 🔎")
                print(f"buscando ultimos numeros guardados num1:{num1}  y num2:{num2}")
                print(f"la ultima resta guardada es  ➖ : {numero.restar_numeros()} ")
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