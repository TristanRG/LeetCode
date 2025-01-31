class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
            1000 : "M",
            900 : "CM",
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I"
        }
        roman_list = []

        for value, letter in romans.items():
            if num == 0:
                break
            count = num // value
            roman_list.append(letter * count)
            num -= count * value

        return "".join(roman_list)