def romanToInt(s):
    numeral = {
    'I': 1, 
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    val, prev = 0, 0

    for char in s[::-1]:
        if numeral[char] >= prev:
            val += numeral[char]
        else:
            val -= numeral[char]

        prev = numeral[char]
    return val

print(romanToInt('VL'))