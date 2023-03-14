correspondences = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

function convertFromDecimal(value, numeral) {
    const rests = []

    while (value > 0) {
        if(value % numeral > 9) {
            rests.push(correspondences[value % numeral])
        } else {
            rests.push(value % numeral)
        }

        value = Math.floor(value / numeral)
    }

    return rests.reverse().join("")
}

function convertToDecimal(value, numeral) {
    value.split("").reverse()

    result = value.reduce((result, value, index) =>
        {if(value > 9) {
            correspondences.map()
        }else {
            result + value * Math.pow(numeral, index)
        }}
    , 0)

    return result
}

console.log(convertFromDecimal(255, 16))
console.log(convertFromDecimal("FF", 16))