# zona clase

class tiempo:
    def __init__(self,horas):
        self.horas = horas

    def convertir_a_minutos(self):
        return self.horas * 60    

# zona de codigo principal

def main():
    ultimas_horas = None

    while True:
        print("")
        print("==================================")
        print("===== menu de horas a mintos =====")
        print("==================================")
        print("1. convertir horas a minutos ⏱️.")
        print("2. mostrar datos guardados ♻️.")
        print("3. salir .")
        opciones = input("elija una opcion: ")
        
        if opciones == "1":
            print("")
            horas = int(input("ingresa las horas ⏱️ : "))
            tim = tiempo(horas) 
            minutos = tim.convertir_a_minutos()
            print(f"los minutos son ⏱️: {minutos}")
            print("")
            ultimas_horas = horas

        elif opciones == "2":
            if ultimas_horas is None:
                print("")
                print("⚠️ no hay datos guardados aun. selecione la opcion 1 primero.")
                print("")
            else:
                tim = tiempo(horas)
                print("")
                print("buscando horas recientes ⏱️ 🔎")
                print(f"ultimas horas guardadas :{horas}")
                print(f"ultimos minutos convertidos {tim.convertir_a_minutos()} ")

        elif opciones == "3":
            print("")
            print("proceso terminado 😴")
            break
        else:
            print("")
            print("🚫 opcion no valida")
            print("")

# ejecucion

if __name__ == "__main__":
    main()