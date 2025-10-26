# zona de clase

class paralelogramo:
    # constructor
    def __init__(self,base,altura):
        self.base =base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura 
    
# codigo principal

def main():
    ultima_base = None
    ultimas_altura = None
    
    while True:
        print("===============================")
        print("==== menu de paralelograma ====")
        print("===============================")
        print("1. calcular area del paralelograma ❔")
        print("2. mostrar ultima area guardada del paralelograma ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            base = int(input("ingresa la base del paralelograma ❔ : "))
            altura = int(input("ingresa la altura del paralelograma ❔: "))
            figura = paralelogramo(base,altura)
            area = figura.calcular_area()
            print(f"lo area del paralelograma es ❔ : {area:.2f}")
            ultima_base = base
            ultimas_altura = altura
            print("")

        elif opciom == "2":
            if ultima_base is None or ultimas_altura is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                figura = paralelogramo(base,altura)
                print("")
                print("buscando ultima base,area y altura guardada 🔎")
                print(f"la ultims base ingresada es ❔ :{base}")
                print(f"la ultima altura ingresada es ❔ :{altura}")
                print(f"ultima area guardada ❔ : {figura.calcular_area():.2f} ")
                print("")

        elif opciom == "3":
            print("")
            print("programa finalizado 😴")
            break
        else:
            print("")
            print("🚫 opcion invalida.")
            print("")

# ejecucion 

if __name__ == "__main__":
    main()