# zona de clase

class piramide:
    # constructor
    def __init__(self,longitud_base,ancho_base,altura):
        self.longitud_base = longitud_base
        self.ancho_base = ancho_base 
        self.altura = altura
        
    def calcular_volumen(self):
        return (self.longitud_base * self.ancho_base * self.altura) / 3

# codigo principal    
    
def main():
    ultima_longitud = None
    ultimo_ancho = None
    ultima_altura = None

    while True:
        print("==========================")
        print("==== menu de piramide ====")
        print("==========================")
        print("1. calcular volumen de piramide 🔺")
        print("2. mostrar ultimo volumen de piramide ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            longitud_base = int(input("ingresa la longitud de la piramide 🔺 : "))
            ancho_base = int(input("ingresa la base de la piramide 🔺 : "))
            altura = int(input("ingresa la altura de la piramide 🔺 : "))
            figura = piramide(longitud_base,ancho_base,altura)
            volumen = figura.calcular_volumen()
            print(f"el volumen de la piramide es es: {volumen:.2f}")
            ultima_longitud = longitud_base
            ultimo_ancho = ancho_base
            ultima_altura = altura

        elif opciom == "2":
            if ultima_longitud is None or ultimo_ancho is None or ultima_altura is None:
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
            else:
                figura = piramide(longitud_base,ancho_base,altura)
                print("buscando volumen de la piramide 🔎")
                print(f"ultima longitud de la piramide 🔺 :{longitud_base}")
                print(f"ultima base de la piramide 🔺:{ancho_base}")
                print(f"ultima altura de la piramide 🔺 :{altura}")
                print(f"ultimo volumen guardado del cuadrado ◻ : {figura.calcular_volumen():.2f} ")

        elif opciom == "3":
            print("programa finalizado 😴")
            break
        else:
            print("🚫 opcion invalida.")

# ejecucion 

if __name__ == "__main__":
    main()