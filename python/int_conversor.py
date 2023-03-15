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
    integerValue = int(value)

    # realizando operações de inteiros e invertendo para ordem correta
    while (integerValue > 0):
        rests.append(integerValue%numeral)
        integerValue = integerValue//numeral
    rests.reverse()
    result = concatenateArrayIntsInString(rests)
    
    return result

# função para realizar potencialização de números de um array e soma-los
def powArrayNumbersAndSum(values, numeral):
    result = 0

    for i in range(len(values)):
        if(values[i] >= "A" and values[i] <= "F"):
            value = [j for j in correspondences if correspondences[j] == values[i]]
            result += value[0] * pow(numeral, i)
        else:
            result += int(values[i])*pow(numeral, i)
    return result

# converter das demais bases para a base decimal
def convertToDecimal(value, numeral):
    intergerValues = reverseString(str(value))
    result = powArrayNumbersAndSum(intergerValues, numeral)

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