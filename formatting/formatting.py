def encode(input_text):
    input_ascii_digits = _get_ascii_digits(input_text)
    input_binary_digits = _get_binary_digits(input_ascii_digits)
    scrambled_binary_digits = _scramble_digits(input_binary_digits)
    output_decimal_value = _get_decimal_value(scrambled_binary_digits)

    return output_decimal_value 

def _get_ascii_digits(input_text):
    return [ord(char) for char in input_text]

def _get_decimal_digits(number):
    return _get_digits(number, 10)

def _get_binary_digits(ascii_digits):
    binary_digits = []

    for curr_ascii_digit in ascii_digits:
        curr_binary_chunk = _get_digits(curr_ascii_digit, 2)
        _zero_pad(curr_binary_chunk, 8)
        binary_digits = curr_binary_chunk + binary_digits

    _zero_pad(binary_digits, 32)

    return binary_digits

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

def _zero_pad(digits, length):
    for i in range(len(digits), length):
        digits.insert(0, 0)
    

def _scramble_digits(digits):
    scrambled = []

    for col in range(8):
        for row in range(4):
            scrambled.append(get_arr_value(digits, row, col))
        
    return scrambled        

def get_arr_value(arr, row, col):
    index = row * 8 
    return arr[index+ col]

def _get_decimal_value(binary_digits):
    decimal_value = 0

    for i in range(len(binary_digits)):
        binary_index = len(binary_digits) - i - 1
        binary_digit = binary_digits[binary_index]

        decimal_value += binary_digit * 2 ** i
    
    return decimal_value