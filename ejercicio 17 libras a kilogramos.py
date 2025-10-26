# zona clase

class convertir_libras:
    #constructor
    def __init__(self,libras):
        self.libras = libras
        
    def convertir_L_Kilogramos(self):
        return self.libras * 0.453592
    
# codigo principal

def main():
    ultima_libra = None
    
    while True:
        print("============================")
        print("==== menu de libras_a_K ====")
        print("============================")
        print("1. convertir libras a kilometros 🍕")
        print("2. mostrar ultimas kilometros guardados ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            libras = int(input("ingresa las libras 🍕 : "))
            convertir = convertir_libras(libras)
            kilogramos = convertir.convertir_L_Kilogramos()
            print(f"los kilogramos son ❔ : {kilogramos:.2f}")
            ultima_libra = libras
            print("")

        elif opciom == "2":
            if ultima_libra is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                convertir = convertir_libras(libras)
                print("")
                print("buscando las libras convertidos en kilogramos 🔎")
                print(f"las libras ingresadas son 🍕 :{libras}")
                print(f"ultimos kiligramos convertidos  son 🍕 : {convertir.convertir_L_Kilogramos():.2f} ")
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