# zona clase

class Promedio:
    #constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular_promedio(self):
        return (self.num1 + self.num2) / 2

# codigo principal

def main():
    ultimo_num1 = None
    ultimo_num2 = None
    ultimo_promedio = None

    while True:
        print("===============================")
        print("       MENÚ DE PROMEDIO 📊")
        print("===============================")
        print("1. Calcular promedio de dos números")
        print("2. Mostrar resultado guardado")
        print("3. Salir")
        print("===============================")

        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            p = Promedio(num1, num2)
            promedio = p.calcular_promedio()
            print(f"El promedio es: {promedio:.2f}")
            ultimo_num1 = num1
            ultimo_num2 = num2
            ultimo_promedio = promedio

        elif opcion == "2":
            if ultimo_num1 is None:
                print("⚠️ No hay resultados guardados. Use la opción 1 primero.")
            else:
                print(f"Últimos números: {ultimo_num1} y {ultimo_num2}")
                print(f"Promedio guardado: {ultimo_promedio:.2f}")

        elif opcion == "3":
            print("👋 Programa finalizado.")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.\n")


# ejecutar el programa
if __name__ == "__main__":
    main()
