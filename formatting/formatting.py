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
    scrambled = [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8]]

    for i in range(8):
        _move_bit(digits, scrambled, i)

    return scrambled        

def _move_bit(src, dst, i):
    src_i0 = 8 - i - 1
    src_i1 = 8*2 - i - 1
    src_i2 = 8*3 - i - 1
    src_i3 = 8*4 - i - 1

    dst_i0 = 
    

