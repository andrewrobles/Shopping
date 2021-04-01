import unittest

from formatting import encode, _to_binary_arr

class TestEncode(unittest.TestCase):

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

class TestToBinaryArr(unittest.TestCase):

    def test_number_2(self):
        input_number = 2

        expected = [1, 0]
        actual = _to_binary_arr(input_number)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()