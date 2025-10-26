# zona clase
class Descuento:
    #constructor
    def __init__(self, precio):
        self.precio = precio

    def calcular_descuento(self):
        return self.precio * 0.10

# codigo principal

def main():
    ultimo_precio = None
    ultimo_descuento = None

    while True:
        print("===============================")
        print("       MENÚ DE DESCUENTO 💰")
        print("===============================")
        print("1. Calcular 10% de descuento 💸")
        print("2. Mostrar resultado guardado ♻️")
        print("3. Salir")
        print("===============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            precio = float(input("Ingrese el precio del artículo: "))
            d = Descuento(precio)
            descuento = d.calcular_descuento()
            print(f"El 10% de descuento es: {descuento:.2f}")
            ultimo_precio = precio
            ultimo_descuento = descuento

        elif opcion == "2":
            if ultimo_precio is None:
                print("⚠️ No hay datos guardados. Use la opción 1 primero.")
            else:
                print(f"Último precio ingresado: {ultimo_precio}")
                print(f"Descuento guardado: {ultimo_descuento:.2f}")

        elif opcion == "3":
            print("Programa finalizado. 😴")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.\n")


# ejecutar el programa
if __name__ == "__main__":
    main()
