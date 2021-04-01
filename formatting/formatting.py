def encode(input_text):
    ascii_number = ord('A')

    return ascii_number

def _get_decimal_digits(number):
    digits = []

    while True:
        curr_digit = number % 10
        digits.insert(0, curr_digit)
        number = number - curr_digit

        if number == 0:
            break

        number = number // 10 
        

    return digits



    



result = encode('A')
print(result)