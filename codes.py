correspondences = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def reverseString(string):
    return string[::-1]

def concatenateArrayIntsInString(values):
    result = ""
    for i in range(len(values)):
        if(values[i] > 9):
            result += correspondences[values[i]]
        else:
            result += str(values[i])
    return result

def convertFromDecimal(value, numeral):
    # array de resultado das operações
    rests = []
    if (int(value) < 1):
        rests.append(0)

    integerValue = int(value)
    floatValue = int(value) - int(value)

    # realizando operações e invertendo para ordem correta
    while (integerValue > 0):
        rests.append(integerValue%numeral)
        integerValue = integerValue//numeral
    rests.reverse()

    result = concatenateArrayIntsInString(rests)

    if(type(value) == float):
        restsFloat = []

        while(floatValue > 0):
            floatValue *= numeral
            restsFloat.append(int(floatValue))
            floatValue = floatValue - int(floatValue)
        
        result = result + "." + concatenateArrayIntsInString(restsFloat)
    
    return result

def powNumbers(values, init, end, numeral, step):
    result = 0
    for i in range(init, end, step):
        if(values[i] >= "A" and values[i] <= "F"):
            value = [j for j in correspondences if correspondences[j] == values[i]]
            result += value[0] * pow(numeral, i)
        else:
            result += int(values[i])*pow(numeral, i)
    return result

def convertToDecimal(value, numeral):
    if(type(value) == float):
        separetaValues = str(value).split(".")
        intergerValues = reverseString(separetaValues[0])
        floatValues = separetaValues[1]

        integers = powNumbers(intergerValues, 0, len(intergerValues), numeral, 1)
        floats = powNumbers(floatValues, -1, -(len(floatValues) + 1), numeral, -1)

        result = integers + floats
    else:
        intergerValues = reverseString(str(value))
        result = powNumbers(intergerValues, 0, len(intergerValues), numeral, 1)
    
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