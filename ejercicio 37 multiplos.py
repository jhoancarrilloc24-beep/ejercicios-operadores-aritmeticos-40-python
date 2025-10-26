# zona clase

class Multiplo:
    #constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def es_multiplo(self):
        if self.num2 == 0:
            return "❌ Error: No se puede dividir entre cero."
        elif self.num1 % self.num2 == 0:
            return f"{self.num1} es múltiplo de {self.num2}"
        else:
            return f"{self.num1} no es múltiplo de {self.num2}"

#codigo principal

def main():
    ultimo_num1 = None
    ultimo_num2 = None
    ultimo_resultado = None

    while True:
        print("===============================")
        print("       MENÚ DE MÚLTIPLOS 🔁")
        print("===============================")
        print("1. Verificar si un número es múltiplo de otro ✖️")
        print("2. Mostrar resultado guardado ♻️")
        print("3. Salir")
        print("===============================")

        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == "1":
            num1 = int(input("Ingrese el primer número 🔺: "))
            num2 = int(input("Ingrese el segundo número 🔺: "))
            m = Multiplo(num1, num2)
            resultado = m.es_multiplo()
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
            print("fi de Programa. 😴")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.\n")


# ejecutar el programa
if __name__ == "__main__":
    main()
