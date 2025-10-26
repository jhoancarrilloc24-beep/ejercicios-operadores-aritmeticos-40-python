
# zona de clase
class Trapecio:
    # constructor
    def __init__(self,longitud,ancho,altura):
        self.longitud = longitud
        self.ancho = ancho
        self.altura = altura

    # método para calcular el área
    def calcular_volumen(self):
        return self.longitud * self.ancho * self.altura


# zona de código principal
def main():
    ultima_longitud = None
    ultimo_ancho = None
    ultima_altura = None

    while True:
        print("==========================")
        print("==== menu de trapecio ====")
        print("==========================")
        print("1. calcular area del trapecio 🕳️")
        print("2. mostrar ultima area ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            longitud = float(input("ingresa la longitud del trapecio : "))
            ancho = float(input("ingresa el ancho del trapecio : "))
            altura = float(input("ingresa la altura del trapecio : "))
            figura = Trapecio(longitud,ancho,altura)
            volumen =figura.calcular_volumen()
            print(f"el volumen es: {volumen:.2f}")
            ultima_longitud = longitud
            ultimo_ancho = ancho
            ultima_altura = altura

        elif opciom == "2":
            if ultima_longitud is None or ultimo_ancho is None or ultima_altura is None:
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
            else:
                figura = Trapecio(ultima_longitud,ultimo_ancho,ultima_altura)
                print("buscando actualizacion del volumen 🔎 ")
                print(f"la ultima longitud es: {ultima_longitud}")
                print(f"ultimo ancho ingresado: {ultimo_ancho}")
                print(f"ultima altura ingresada: {ultima_altura}")
                print(f"ultimo volumen del trapecio: {figura.calcular_volumen():.2f}")


        elif opciom == "3":
            print("programa finalizado 😴")
            break

        else:
            print("🚫 opcion invalida.")

# ejecucion 

if __name__ == "__main__":
    main()