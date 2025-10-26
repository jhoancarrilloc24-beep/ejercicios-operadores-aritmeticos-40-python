import math

# ========================================
# CLASE CIRCULO
# ========================================
class Circulo:
    # Constructor
    def __init__(self, radio):
        self.radio = float(radio)

    # Método para calcular el área
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

# ========================================
# FUNCIÓN PRINCIPAL
# ========================================
def main():
    ultima_radio = None
    
    while True:
        print("===========================")
        print("===== MENU DE CIRCULO =====")
        print("===========================")
        print("1. Calcular área de círculo 🏐")
        print("2. Mostrar última área del círculo ♻️")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            radio = input("Ingresa el radio del círculo 🏐 : ")
            figura = Circulo(radio)
            area = figura.calcular_area()
            print(f"El área del círculo es 🏐 s: {area:.2f}")
            ultima_radio = radio  # ✅ Guardar último valor

        elif opcion == "2":
            if ultima_radio is None:
                print("⚠️ No hay valores previos. Usa primero la opción 1.")
                continue

            figura = Circulo(ultima_radio)
            print("Reutilizando el último radio ingresado ♻️ :")
            print(f"Radio del círculo 🏐 : {ultima_radio}")

            sub = input("1) Calcular área nuevamente: ").strip()
            if sub == "1":
                area = figura.calcular_area()
                print(f"El área del círculo es 🏐 : {area:.2f}")
            else:
                print("🚫 Opción no válida")

        elif opcion == "3":
            print("programa finalizado 😴")
            break
        else:
            print("🚫 Opción no válida")

# ========================================
# EJECUCIÓN
# ========================================
if __name__ == "__main__":
    main()
