correspondencias = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def reverseString(string):
    return string[::-1]

def DivideMethod(value, numeral):
    # array de resultado das operações
    rests = []

    # realizando operações e invertendo para ordem correta
    while (value > 0):
        rests.append(value%numeral)
        value = value//numeral
    rests.reverse()

    result = ""
    for i in range(len(rests)):
        if(rests[i] > 9):
            result += correspondencias[rests[i]]
        else:
            result += str(rests[i])
    return result

def powMethod(value, numeral):
    valueParse = reverseString(str(value))
    result = 0
    for i in range(len(valueParse)):
        if(valueParse[i] >= "A" and valueParse[i] <= "F"):
            value = [j for j in correspondencias if correspondencias[j] == valueParse[i]]
            result += value[0] * pow(numeral, i)
        else:
            result += int(valueParse[i])*pow(numeral, i)
    return result

print(DivideMethod(990129, 16))
print(powMethod("FFAEB", 16))