import unittest

from formatting import encode, _get_decimal_digits, _get_binary_digits, _scramble_digits, _get_decimal_value


class IntegrationTests(unittest.TestCase):

    def test_single_character(self):
        input_text = 'A'
        
        expected = 16777217
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_full_bundle(self):
        input_text = 'FRED'
        
        expected = 251792692 
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_non_alphanumerics(self):
        input_text = ' :^)'

        expected = 79094888
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_lowercase(self):
        input_text = 'foo'

        expected = 124807030
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_space_lowercase(self):
        input_text = ' foo'

        expected = 250662636
        actual = encode(input_text)
        
        self.assertEqual(expected, actual)

    def test_four_lowercase(self):
        input_text = 'foot'

        expected = 267939702
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_uppercase(self):
        input_text = 'BIRD'

        expected = 251930706
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_periods(self):
        input_text = '....'

        expected = 15794160
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_carets(self):
        input_text = '^^^^'

        expected = 252706800
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_capitalized_word(self):
        input_text = 'Woot'

        expected = 266956663
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_two_lowercase(self):
        input_text = 'no'

        expected = 53490482
        actual = encode(input_text)

        self.assertEqual(expected, actual)

class UnitTests(unittest.TestCase):
    
    def test_get_decimal_digits_123(self):
        input_number = 123 

        actual = _get_decimal_digits(input_number)
        expected = [1, 2, 3]

        self.assertEqual(expected, actual)
    
    def test_binary_digits_8(self):
        input_number = 8

        actual = _get_binary_digits(input_number)
        expected = [
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 1, 0, 0, 0,
        ]

        self.assertEqual(expected, actual)

    def test_scramble_digits(self):
        input_binary = [
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 1, 0, 0, 0, 0, 0, 1,
        ]

        actual = _scramble_digits(input_binary)
        expected = [
            0, 0, 0, 0, 0, 0, 0, 1, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 1, 
        ]

        self.assertEqual(expected, actual)

    def test_get_decimal_value(self):
        input_binary = [
            0, 0, 0, 0, 0, 0, 0, 1, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 1, 
        ]

        actual = _get_decimal_value(input_binary)
        expected = 16777217

        self.assertEqual(expected, actual)

class TestSingleCharacter(unittest.TestCase):

    def setUp(self):
        self.raw_characters = 'A'

        self.input_binary = [
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 1, 0, 0, 0, 0, 0, 1 
        ]
        
        self.output_binary = [
            0, 0, 0, 0, 0, 0, 0, 1, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 1 
        ]

        self.output_decimal = 16777217 

    def test_get_binary_digits(self):
        '''First step is to convert raw characters into binary'''

        actual = self.input_binary
        expected = _get_binary_digits(self.raw_characters)

        self.assertEqual(actual, expected)

    def test_scramble_digits(self):
        '''Second step is to scramble binary digits''' 
        
        actual = self.output_binary
        expected = _scramble_digits(self.input_binary)

        self.assertEqual(actual, expected)

    def test_get_decimal_value(self):
        '''Third step is convert binary digits into binary'''

        actual = self.output_decimal
        expected = _get_decimal_value(self.output_binary)

        self.assertEqual(actual, expected)

    def test_encode(self):
        '''Public function does all the steps in one'''

        actual = self.output_decimal
        expected = encode(self.raw_characters)

        self.assertEqual(actual, expected)


class TestFullBundle(unittest.TestCase):

    def setUp(self):
        self.raw_characters = 'FRED'

        self.input_binary = [
            0, 1, 0, 0, 0, 1, 0, 0, 
            0, 1, 0, 0, 0, 1, 0, 1, 
            0, 1, 0, 1, 0, 0, 1, 0, 
            0, 1, 0, 0, 0, 1, 1, 0, 
        ]

        self.output_binary = [
            0, 0, 0, 0, 1, 1, 1, 1, 
            0, 0, 0, 0, 0, 0, 1, 0, 
            0, 0, 0, 0, 1, 1, 0, 1, 
            0, 0, 1, 1, 0, 1, 0, 0, 
        ]

        self.output_decimal = 251792692

    def test_get_binary_digits(self):
        '''Step 1 is to convert raw characters into binary'''

        actual = self.input_binary
        expected = _get_binary_digits(self.raw_characters)

        self.assertEqual(actual, expected)

    def test_encode(self):
        input_text = 'FRED'
        
        expected = 251792692 
        actual = encode(input_text)

        self.assertEqual(expected, actual)
    

if __name__ == '__main__':
    unittest.main()