# zona de clase

class convertirtemperatura:
    # contructor
    def __init__(self,celsius):
        self.celsius = float(celsius)

    def convertir_a_fahrenheit(self):
        return (self.celsius * 9/5) + 32

# codigo principal

def main():
    
    ultima_tem = None

    while True:
        print("===========================")
        print("=== menu de temperatura ===")
        print("===========================")
        print("1. convertir celsius a fahrenheit 🌡️")
        print("2. mostrar ultima conversion ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            celsius = input("ingresa la temperatura en grados celsius: ")
            conversion = convertirtemperatura(celsius)
            fahrenheit = conversion.convertir_a_fahrenheit()
            print(f"{celsius}°C equivalen a {fahrenheit:2f} °F")
            ultima_tem = celsius

        elif opciom == "2":
            if ultima_tem is None:
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
            else:
                conversion = convertirtemperatura(ultima_tem)
                fahrenheit = conversion.convertir_a_fahrenheit()
                print(f"ultima conversión guardada ♻️:")
                print(F"{ultima_tem}°C = {fahrenheit:.2f}°F")

        elif opciom == "3":
            print("programa finalizado 😴")
            break

        else:
            print("🚫 opcion invalida.")

# ejecucion 

if __name__ == "__main__":
    main()