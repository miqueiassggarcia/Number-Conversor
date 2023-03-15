import { convertFromDecimal, convertToDecimal } from "./conversor"

test("Return a binary value of this decimal", () => {
    expect(convertToDecimal(10, 2)).toBe(2)
})