# zona de clase

class convertir_dolar:
    def __init__(self,dolares,tasa_cambio):
        self.dolares = float(dolares)
        self.tasa_cambio = float(tasa_cambio)

    def convertir_a_euro(self):
        return self.dolares * self.tasa_cambio
    

# zona codigo principal

def main():
    ultimo_dolar = None
    ultima_tasa = None

    while True:
        print("================================")
        print("===== menu de cambio dolar =====")
        print("================================")
        print("1. convertir dolares a euros 💰")
        print("2. mostrar ultima conversion ♻️")
        print("3. salir")

        opcion = input("ingresa una opcion: ")

        if opcion == "1":
            dolares = input("ingresa la cantidad de dolares a convertir: ")
            tasa_cambio = input("ingresa la tasa de cambio: ")
            convertir = convertir_dolar(dolares,tasa_cambio)
            euros = convertir.convertir_a_euro()
            print(f"{dolares} usd equivalen a {euros:.2f} eur (tasa de cambio: {tasa_cambio})")
            ultimo_dolar = dolares
            ultima_tasa = tasa_cambio

        elif opcion == "2":
            if ultimo_dolar is None or ultima_tasa is None:
                print("⚠️ opcion vo valida ")
            else:
                convertir = convertir_dolar(ultimo_dolar,ultima_tasa)
                euros = convertir.convertir_a_euro()
                print(f"ultima conversión guardada ♻️ :")
                print(f"dolar {ultimo_dolar} = euros {euros} tasa de cambio = {ultima_tasa}")

        elif opcion == "3":
            print("programa finalizado 😴 .")
            break
        else:
            print("🚫 opcion no valida. intente de nuevo:")


# ejecucion  de codigo

if __name__ == "__main__":
    main()