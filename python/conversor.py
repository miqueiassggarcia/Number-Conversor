correspondences = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

# função para inverter string
def reverseString(string):
    return string[::-1]

# função para concatenar array de inteiros em uma string
def concatenateArrayIntsInString(values):
    result = ""
    for i in range(len(values)):
        if(values[i] > 9):
            result += correspondences[values[i]]
        else:
            result += str(values[i])
    return result

# conversor de decimal para demais bases
def convertFromDecimal(value, numeral):
    rests = []
    result = ""
    # separando valores inteiros e float
    if("." in str(value)):
        # adicionando 0 caso seja apenas números de ponto flutuante
        if (float(value) < 1):
            rests.append(0)
        values = str(value).split(".")
        integerValue = int(values[0])
        # arredondando de acordo com o tamanho parseado
        floatValue = round(int(values[1])*pow(10, -(len(values[1]))), (len(values[1])))

        restsFloat = []

        while(floatValue > 0):
            floatValue *= numeral
            restsFloat.append(int(floatValue))
            floatValue = floatValue - int(floatValue)
        result = concatenateArrayIntsInString(restsFloat)
    else:
        integerValue = int(value)


    # realizando operações de inteiros e invertendo para ordem correta
    while (integerValue > 0):
        rests.append(integerValue%numeral)
        integerValue = integerValue//numeral
    rests.reverse()

    if("." in str(value)):
        result = concatenateArrayIntsInString(rests) + "." + result
    else:
        result = concatenateArrayIntsInString(rests)
    
    return result

# função para realizar potencialização de números de um array e soma-los
def powArrayNumbersAndSum(values, init, end, numeral, step):
    result = 0
    position = 0

    for i in range(init, end, step):
        if(values[position] >= "A" and values[position] <= "F"):
            value = [j for j in correspondences if correspondences[j] == values[position]]
            result += value[0] * pow(numeral, i)
        else:
            result += int(values[position])*pow(numeral, i)
        position += 1
    return result

# converter iniciais para a base decimal
def convertToDecimal(value, numeral):
    if("." in str(value)):
        separetaValues = str(value).split(".")
        intergerValues = reverseString(separetaValues[0])
        floatValues = separetaValues[1]

        integers = powArrayNumbersAndSum(intergerValues, 0, len(intergerValues), numeral, 1)
        floats = powArrayNumbersAndSum(floatValues, -1, -(len(floatValues) + 1), numeral, -1)

        result = integers + floats
    else:
        intergerValues = reverseString(str(value))
        result = powArrayNumbersAndSum(intergerValues, 0, len(intergerValues), numeral, 1)
    
    return result

def main():
    baseInicial = int(input("Digite a base inicial que será convertida: "))
    baseFinal = int(input("Digite a base final para conversão: "))
    number = input("\nDigite o número que deseja converter: ")

    if(baseInicial != 10):
        decimalValue = convertToDecimal(number, baseInicial)
        if(baseFinal == 10):
            print("\nValor na base " + str(baseFinal) + ": " + str(decimalValue), sep="")
        else:
            convertedValue = convertFromDecimal(decimalValue, baseFinal)
            print("\nValor na base " + str(baseFinal) + ": " + convertedValue, sep="")
    else:
        convertedValue = convertFromDecimal(number, baseFinal)
        print("\nValor na base " + str(baseFinal) + ": " + convertedValue, sep="")

if(__name__ == "__main__"):
    main()