import math

# Zona de clase
class Cono:
    # Constructor del cono
    def __init__(self, radio, altura):
        self.radio = float(radio)
        self.altura = float(altura)
        
    # Método para calcular el volumen
    def calcular_volumen(self):
        return (1/3) * math.pi * (self.radio ** 2) * self.altura
    

# Código principal
def main():
    ultima_radio = None
    ultima_altura = None
    
    while True:
        print("==========================")
        print("====== MENÚ DE CONO ======")
        print("==========================")
        print("1. Calcular volumen del cono 🗼")
        print("2. Mostrar último volumen calculado ♻️")
        print("3. Salir 🚪")
        
        opcion = input("Ingresa una opción: ")
        
        if opcion == "1":
            radio = input("Ingresa el radio del cono 🗼: ")
            altura = input("Ingresa la altura del cono 🗼: ")
            figura = Cono(radio, altura)
            volumen = figura.calcular_volumen()
            print(f"El volumen del cono es: {volumen:.2f}")
            ultima_radio = radio
            ultima_altura = altura
            
        elif opcion == "2":
            if ultima_radio is None or ultima_altura is None:
                print("⚠ No hay datos guardados aún. Usa primero la opción 1.")
            else:
                figura = Cono(ultima_radio, ultima_altura)
                print("Reutilizando el último volumen ingresado ♻️:")
                print(f"Radio: {ultima_radio} | Altura: {ultima_altura}")
                print(f"Volumen del cono anterior: {figura.calcular_volumen():.2f}")
                
        elif opcion == "3":
            print("programa finalizado 😴")
            break
        
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# Ejecutar programa
if __name__ == "__main__":
    main()
