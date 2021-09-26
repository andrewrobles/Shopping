import unittest

from formatting import encode, decode


class IntegrationTests(unittest.TestCase):
    '''
    Tests from "More examples" section of problem spec
    '''

    def test_tacocat(self):
        '''
        taco
        116 97 99 111
        1110100 1100001 1100011 1101111
        01101111 01100011 01100001 01110100

        [267487694, 125043731]
        1111111100011000100111001110 111011101000000010000010011

        1. 267487694
        2. 00001111 11110001 10001001 11001110
        3. 01101111 01100011 01100001 01110100
        4. 1169799111


        '''
        # input_text = 'tacocat'
        encoded = 267487694
        expected = '00001111111100011000100111001110'
        actual = decode(encoded)
        print('LEN EXPECTED')
        print(len(expected))
        print('LEN ACTUAL')
        print(len(expected))

        # self.assertEqual(input_text, decode(encode(input_text)))
        self.assertEqual(expected, decode(encoded))

    def test_single_character(self):
        input_text = 'A'
        
        expected = [16777217]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_full_bundle(self):
        input_text = 'FRED'
        
        expected = [251792692]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_non_alphanumerics(self):
        input_text = ' :^)'

        expected = [79094888]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_lowercase(self):
        input_text = 'foo'

        expected = [124807030]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_space_lowercase(self):
        input_text = ' foo'

        expected = [250662636]
        actual = encode(input_text)
        
        self.assertEqual(expected, actual)

    def test_four_lowercase(self):
        input_text = 'foot'

        expected = [267939702]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_uppercase(self):
        input_text = 'BIRD'

        expected = [251930706]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_periods(self):
        input_text = '....'

        expected = [15794160]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_carets(self):
        input_text = '^^^^'

        expected = [252706800]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_capitalized_word(self):
        input_text = 'Woot'

        expected = [266956663]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_two_lowercase(self):
        input_text = 'no'

        expected = [53490482]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_7_letter_word(self):
        input_text = 'tacocat'

        expected = [267487694, 125043731]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_4_words(self):
        input_text = 'never odd or even'

        expected = [267657050, 233917524, 234374596, 250875466, 17830160]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_4_words_with_special_characters(self):
        input_text = 'lager, sir, is regal'

        expected = [267394382, 167322264, 66212897, 200937635, 267422503]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_8_words_with_special_characters_1(self):
        input_text = "go hang a salami, I'm a lasagna hog"

        expected = [200319795, 133178981, 234094669, 267441422, 78666124, 99619077, 267653454, 133178165, 124794470]
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_8_words_with_special_characters_2(self):
        input_text = 'egad, a base tone denotes a bad age'

        expected = [267389735, 82841860, 267651166, 250793668, 233835785, 267665210, 99680277, 133170194, 124782119]
        actual = encode(input_text)

        self.assertEqual(expected, actual)
    

class BaseTestCases:

    class BaseTest(unittest.TestCase):
        '''
        Classes that inherit from BaseTest require the following variables:

        - raw_characters
        - ascii_digits
        - input_binary
        - output_binary

        to be defined in test setUp function as class variables.
        '''

        def test_encode(self):
            '''Public function does all the steps in one'''

            actual = self.output_decimal
            expected = encode(self.raw_characters)

            self.assertEqual(actual, expected)


class TestSingleCharacter(BaseTestCases.BaseTest):
    '''
    Tests from "Examples" section of problem spec
    '''
    
    def setUp(self):
        self.raw_characters = 'A'

        self.ascii_digits = [65]

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

        self.output_decimal = [16777217]

class TestFullBundle(BaseTestCases.BaseTest):

    def setUp(self):
        self.raw_characters = 'FRED'

        self.ascii_digits = [70, 82, 69, 68]

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

        self.output_decimal = [251792692]

class TestNonAlphanumerics(BaseTestCases.BaseTest):
    
    def setUp(self):
        self.raw_characters = ' :^)'

        self.ascii_digits = [32, 58, 94, 41]

        self.input_binary = [
            0, 0, 1, 0, 1, 0, 0, 1,
            0, 1, 0, 1, 1, 1, 1, 0,
            0, 0, 1, 1, 1, 0, 1, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
        ]

        self.output_binary = [
            0, 0, 0, 0, 0, 1, 0, 0,
            1, 0, 1, 1, 0, 1, 1, 0,
            1, 1, 1, 0, 0, 1, 0, 0,
            0, 1, 1, 0, 1, 0, 0, 0,
        ]

        self.output_decimal = [79094888]


if __name__ == '__main__':
    unittest.main()