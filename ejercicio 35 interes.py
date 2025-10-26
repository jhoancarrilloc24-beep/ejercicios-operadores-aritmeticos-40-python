# zona clase

class Interes:
    #constructor
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def calcular_interes(self):
        return self.cantidad * 0.05

#codigo principal

def main():
    ultima_cantidad = None
    ultimo_interes = None

    while True:
        print("===============================")
        print("       MENÚ DE INTERÉS 💵")
        print("===============================")
        print("1. Calcular 5% de interés 💸")
        print("2. Mostrar resultado guardado ♻️")
        print("3. Salir")
        print("===============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad de dinero: "))
            i = Interes(cantidad)
            interes = i.calcular_interes()
            print(f"El 5% de interés es: {interes:.2f}")
            ultima_cantidad = cantidad
            ultimo_interes = interes

        elif opcion == "2":
            if ultima_cantidad is None:
                print("⚠️ No hay datos guardados. Use la opción 1 primero.")
            else:
                print(f"Última cantidad ingresada: {ultima_cantidad}")
                print(f"Interés guardado: {ultimo_interes:.2f}")

        elif opcion == "3":
            print("fin del Programa. 😴")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.\n")


# ejecutar el programa
if __name__ == "__main__":
    main()
