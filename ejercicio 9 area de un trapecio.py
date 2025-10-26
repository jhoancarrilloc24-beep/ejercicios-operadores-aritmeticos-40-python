
# zona de clase
class Trapecio:
    # constructor
    def __init__(self, base, longitud_base, altura):
        self.base = float(base)
        self.longitud_base = float(longitud_base)
        self.altura = float(altura)

    # método para calcular el área
    def calcular_area(self):
        return ((self.base + self.longitud_base) * self.altura) / 2


# zona de código principal
def main():
    ultima_base = None
    ultima_longitud = None
    ultima_altura = None
    ultima_area = None

    while True:
        print("=======================================")
        print("     MENÚ: ÁREA DE UN TRAPECIO ")
        print("=======================================")
        print("1. Calcular área del trapecio 📏")
        print("2. Mostrar última operación de trapecio 📏")
        print("3. Salir")
        print("=======================================")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            base = int(input("Ingresa la base del trapecio 📏 : "))
            longitud_base = int(input("Ingresa la longitud (otra base) del trapecio 📏 : "))
            altura = int(input("Ingresa la altura del trapecio 📏 : "))

            trapecio = Trapecio(base, longitud_base, altura)
            area = trapecio.calcular_area()

            print(f"\n✅ El área del trapecio es: {area:.2f} unidades²\n")

            ultima_base = base
            ultima_longitud = longitud_base
            ultima_altura = altura
            ultima_area = area

        elif opcion == "2":
            if ultima_area is not None:
                print("\n📘 Último cálculo realizado:")
                print(f"Base: {ultima_base}")
                print(f"Otra base: {ultima_longitud}")
                print(f"Altura: {ultima_altura}")
                print(f"Área: {ultima_area:.2f} unidades²\n")
            else:
                print("\n⚠️ opcion no valida.\n")

        elif opcion == "3":
            print("Programa finalizado 😴")
            break
        else:
            print("\n❌ Opción no válida, intenta nuevamente.\n")


# ejecución de código
if __name__ == "__main__":
    main()
