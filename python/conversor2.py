#só não funciona ainda para base hexadecimal
dicionario = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}
def decimal_qualquer(numero, base):
    dividendo = numero
    quociente = 1
    lista = []

    if not base == 1:
        while quociente >=1:
            resto = dividendo % base
            if base == 16:
                if resto >=10 and resto <=16:
                    lista.append(dicionario[resto])
                else:
                    lista.append(resto)
                    quociente = dividendo//base
                    dividendo = quociente
            else:
                lista.append(resto)
                quociente = dividendo // base
                dividendo = quociente

        lista.reverse()
        lista = "".join(map(str, lista))

        return lista

    return

def qualquer_decimal(numero, baseIni):
    string_numero = str(numero)
    lista = []
    numero_convertido = 0

    resultado = 0
    for i in range(len(string_numero)):
        lista.append(int(string_numero[i]))

    lista.reverse()
    for i in range(len(lista)):
        numero_convertido += lista[i]*(baseIni**i)

    return numero_convertido

def iniciar():
    ini = int(input("Digite algo\n"
                    "1 - Parar\n"
                    "2 - Converter\n"
                    "Opção: "))
    return ini

def main():

    while iniciar() !=1:
        baseIni = int(input("Digite a base de inicio: "))
        baseDes = int(input("Digite a base de destino: "))
        numero = int(input("Digite o número que deseja converter: "))
        n1 = qualquer_decimal(numero, baseIni)
        if baseIni < baseDes:
            if baseDes != 10:
                print(f"O número {numero} em base {baseDes} é: ",decimal_qualquer(n1, baseDes))
            else:
                print(f"O número {numero} em base {baseDes} é: ",n1)
        else:
            n1 = qualquer_decimal(numero, baseIni)
            print(decimal_qualquer(n1,baseDes))

if(__name__== "__main__"):
    main()

