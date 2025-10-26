# zona clase

class Cociente:
    # constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular_cociente(self):
        # Evita división por cero
        if self.num2 == 0:
            return "❌ Error: No se puede dividir entre cero."
        else:
            return self.num1 / self.num2

# codigo principla

def main():
    ultimo_num1 = None
    ultimo_num2 = None
    ultimo_cociente = None

    while True:
        print("===============================")
        print("       MENÚ DE COCIENTE ➗")
        print("===============================")
        print("1. Calcular cociente 🔺")
        print("2. Mostrar resultado guardado ♻️")
        print("3. Salir")
        print("===============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num1 = int(input("Ingrese el primer número entero 🔺: "))
            num2 = int(input("Ingrese el segundo número entero 🔺: "))
            c = Cociente(num1, num2)
            resultado = c.calcular_cociente()
            print(f"El cociente es: {resultado}")
            ultimo_num1 = num1
            ultimo_num2 = num2
            ultimo_cociente = resultado

        elif opcion == "2":
            if ultimo_num1 is None:
                print("⚠️ No hay resultados guardados. Use la opción 1 primero.")
            else:
                print(f"Últimos números: {ultimo_num1} y {ultimo_num2}")
                print(f"Resultado guardado: {ultimo_cociente}")

        elif opcion == "3":
            print("fin de Programa. 😴")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.\n")


# ejecutar el programa
if __name__ == "__main__":
    main()
