const correspondences = {
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

function getKeyByValueOfCorrespondences(value) {
    for(const obj in correspondences) {
        if(correspondences[obj] == value) {
            return obj
        }
    }
}

function convertToDecimal(value, numeral) {
    valueParse = String(value).split("").reverse()

    result = valueParse.reduce((result, value, index) =>
        {if(value >= "A" && value <= "F") {
            return result += getKeyByValueOfCorrespondences(value) * Math.pow(numeral, index)
        }else {
            return result += Number(value) * Math.pow(numeral, index)
        }}
    , 0)

    return result
}