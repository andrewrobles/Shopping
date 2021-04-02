def encode(input_text):
    ascii_number = ord('A')

    return ascii_number

def _get_decimal_digits(number):
    return _get_digits(number, 10)

def _get_binary_digits(number):
    return _get_digits(number, 2)

def _get_digits(number, base):
    digits = []

    while True:
        curr_digit = number % base 
        digits.insert(0, curr_digit)
        number = number - curr_digit

        if number == 0:
            break

        number = number // base 
        
    return digits

def _scramble_digits(digits):
    scrambled = []
    
    for i in range(8, -1, -1):

        nibble = [
            digits[i * 4 - 1],
            digits[i * 3 - 1],
            digits[i * 2 - 1],
            digits[i - 1],
        ]

        scrambled = nibble + scrambled

    return scrambled        