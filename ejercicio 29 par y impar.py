# zona clase
class ParImpar:
    #contructor
    def __init__(self, numero):
        self.numero = numero

    def determinar(self):
        if self.numero % 2 == 0:
            return "El número es par."
        else:
            return "El número es impar."


# código principal
def main():
    ultimo_numero = None  # ✅ inicializamos la variable aquí

    while True:
        print("==============================")
        print("      MENU PAR O IMPAR 🧮")
        print("==============================")
        print("1. Determinar si un número es par o impar")
        print("2. Mostrar resultados guardados")
        print("3. Salir")
        print("==============================")

        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == "1":
            numero = int(input("Ingrese un número: "))
            resultado = ParImpar(numero)
            print(resultado.determinar())
            ultimo_numero = numero  # ✅ guardamos el número ingresado

        elif opcion == "2":
            if ultimo_numero is None:
                print("⚠️ No hay datos guardados aún. Seleccione la opción 1 primero.")
            else:
                print(f"Último número ingresado: {ultimo_numero}")
                resultado = ParImpar(ultimo_numero)
                print(f"Resultado: {resultado.determinar()}")

        elif opcion == "3":
            print("Programa finalizado. 😴")
            break

        else:
            print("⚠️ Opción no válida. Intente de nuevo.\n")


# ejecutar el programa
if __name__ == "__main__":
    main()
