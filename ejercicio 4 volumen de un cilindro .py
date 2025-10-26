import math


class Cilindro:
    """Clase que representa un cilindro (base = radio)."""

    def __init__(self, base, altura):
        # Convertimos aquí a float para evitar TypeError al usar **
        self.base = float(base)
        self.altura = float(altura)

    def calcular_area(self):
        """Área de la base (π * r^2)."""
        return math.pi * (self.base ** 2)

    def calcular_volumen(self):
        """Volumen del cilindro (π * r^2 * h)."""
        return math.pi * (self.base ** 2) * self.altura


def main():
    ultima_base = None
    ultima_altura = None

    while True:
        print("============================")
        print("===== MENÚ DE CILINDRO =====")
        print("============================")
        print("1. Calcular área del cilindro 🗞️")
        print("2. Calcular volumen del cilindro ⚙️")
        print("3. Volver a hacer ♻️ (usa la última base/altura ingresada)")
        print("4. Salir 😴")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            base = input("Ingresa el radio/base del cilindro 🗞️: ").strip()
            altura = input("Ingresa la altura del cilindro 🗞️: ").strip()
            try:
                figura = Cilindro(base, altura)
            except ValueError:
                print("🚫 Valores no válidos. Usa números (ej: 2.5).")
                continue
            ultima_base = figura.base
            ultima_altura = figura.altura
            print(f"El área del cilindro es 🗞️: {figura.calcular_area():.2f}")

        elif opcion == "2":
            base = input("Ingresa el radio/base del cilindro 🗞️: ").strip()
            altura = input("Ingresa la altura del cilindro 🗞️: ").strip()
            try:
                figura = Cilindro(base, altura)
            except ValueError:
                print("🚫 Valores no válidos. Usa números (ej: 2.5).")
                continue
            ultima_base = figura.base
            ultima_altura = figura.altura
            print(f"El volumen del cilindro es ⚙️: {figura.calcular_volumen():.2f}")

        elif opcion == "3":
            if ultima_base is None or ultima_altura is None:
                print("No hay valores previos. Primero ingresa base y altura con la opción 1 o 2.")
                continue

            figura = Cilindro(ultima_base, ultima_altura)
            print("♻️ Reutilizando la última base y altura ingresadas:")
            print(f" - radio/base = {ultima_base}")
            print(f" - altura     = {ultima_altura}")
            # Preguntamos qué calcular ahora
            sub = input("¿Quieres calcular 1) Área o 2) Volumen? Elige 1 o 2: ").strip()
            if sub == "1":
                print(f"El área del cilindro es 🗞️: {figura.calcular_area():.2f}")
            elif sub == "2":
                print(f"El volumen del cilindro es ⚙️: {figura.calcular_volumen():.2f}")
            else:
                print("Opción no válida dentro de 'volver a hacer'. Volviendo al menú...")

        elif opcion == "4":
            print("programa finalizado 😴 ")
            break

        else:
            print("🚫 Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
