# zona de clase

class convertir_pulgadas:
    #constructor
    def __init__(self,pulgadas):
        self.pulgadas = pulgadas
        
    def convertir_centimetros(self):
        return self.pulgadas * 2.54
    
# codigo principla
    
def main():
    ultimas_pulgadas = None
    
    while True:
        print("==========================")
        print("==== menu de pulgadas ====")
        print("==========================")
        print("1. convertir pulgadas a centimetros ❔")
        print("2. mostrar ultimas pulgadas convertidas a centimetros ♻️")
        print("3. salir ")

        opciom = input("elige una opción: ")

        if opciom == "1":
            print("")
            pulgadas = int(input("ingresa las pulgadas ❔ : "))
            convertir = convertir_pulgadas(pulgadas)
            centimetros = convertir.convertir_centimetros()
            print(f"los centimetros son ❔ : {centimetros:.2f}")
            ultimas_pulgadas = pulgadas
            print("")

        elif opciom == "2":
            if ultimas_pulgadas is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                convertir = convertir_pulgadas(pulgadas)
                print("")
                print("buscando centimetros convertidos 🔎")
                print(f"los centimertros convertidos son ❔ :{pulgadas}")
                print(f"ultimos centimetros convertidos ❔ : {convertir.convertir_centimetros():.2f} ")
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