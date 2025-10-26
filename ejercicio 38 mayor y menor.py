# zona de clase

class Mayor:
    # constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def numero_mayor(self):
        if self.num1 > self.num2:
            return f"El mayor es: {self.num1}"
        elif self.num2 > self.num1:
            return f"El mayor es: {self.num2}"
        else:
            return "Ambos números son iguales."

# codigo principal

def main():
    ultimo_num1 = None
    ultimo_num2 = None
    ultimo_resultado = None

    while True:
        print("===============================")
        print("       MENÚ NÚMERO MAYOR 🔺")
        print("===============================")
        print("1. Determinar el número mayor 🔺")
        print("2. Mostrar resultado guardado ♻️")
        print("3. Salir")
        print("===============================")

        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == "1":
            num1 = float(input("Ingrese el primer número 🔺: "))
            num2 = float(input("Ingrese el segundo número 🔺: "))
            m = Mayor(num1, num2)
            resultado = m.numero_mayor()
            print(resultado)
            ultimo_num1 = num1
            ultimo_num2 = num2
            ultimo_resultado = resultado

        elif opcion == "2":
            if ultimo_num1 is None:
                print("⚠️ No hay resultados guardados. Use la opción 1 primero.")
            else:
                print(f"Últimos números: {ultimo_num1} y {ultimo_num2}")
                print(f"Resultado guardado: {ultimo_resultado}")

        elif opcion == "3":
            print("fin de Programa. 😴")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.\n")


# ejecutar el programa
if __name__ == "__main__":
    main()
