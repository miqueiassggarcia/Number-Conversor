#só não funciona ainda para base hexadecimal
def decimal_qualquer(numero, base):
    dividendo = numero
    quociente = 1
    lista = []

    if not base == 1:
        while quociente >=1:
            resto = dividendo % base
            lista.append(resto)
            quociente = dividendo//base
            dividendo = quociente
        lista.reverse()

        lista = "".join(map(str, lista))
        return lista
    return

def binario_decimal(numero):
    string_numero = str(numero)
    lista = []
    numero_convertido = 0

    resultado = 0
    for i in range(len(string_numero)):
        lista.append(int(string_numero[i]))

    lista.reverse()
    for i in range(len(lista)):
        numero_convertido += lista[i]*(2**i)

    return numero_convertido

def iniciar():
    ini = int(input("Digite algo\n"
                    "1 - Parar\n"
                    "2 - Converter"))
    return ini

def main():

    while iniciar() !=1:
        baseIni = int(input("Digite a base de inicio: "))
        baseDes = int(input("Digite a base de destino: "))
        numero = int(input("Digite o número que deseja converter: "))

        if baseIni == 2:
            n1 = binario_decimal(numero)
            if baseDes != 10:
                print(f"O número {numero} em base {baseDes} é: ",decimal_qualquer(n1, baseDes))
            else:
                print(f"O número {numero} em base {baseDes} é: ",n1)

        else:
            n1 = binario_decimal(numero)
            decimal_qualquer(n1, baseDes)


if(__name__== "__main__"):
    main()

