import unittest
from parameterized import parameterized
from str_utils.utils import reverse_string_slicing

class TestStrUtilsSlicing(unittest.TestCase):
    @parameterized.expand([
        ('lower_case', 'something','gnihtemos'),
        ('upper_case', 'SOMETHING', 'GNIHTEMOS'),
        ('capitalized', 'Something','gnihtemoS'),
        ('empty', '','', 'error'),
        ('space', '  ','  ', 'error'),
        ('character', '','a', 'hahahahah'),
        ('number', '456','754','wrong output with numbers'),
    ])

    def test_1_revers_string_slicing(self, name, string,expected, error_message=''):
        self.assertEquals(reverse_string_slicing(string), expected,error_message)

    # def reverse_string_slicing(self):
    #     self.assertEquals(reverse_string_slicing('something'),'gnihtemos')

    # def test_reverse_string_slicing_upper_case(self):
    #     self.assertEqual(reverse_string_slicing("SOMETHING"), "GNIHTEMOS")
    #
    # def test_reverse_string_slicing_capitalized(self):
    #     self.assertEqual(reverse_string_slicing("Something"), "gnihtemoS")
    #
    # def test_reverse_string_slicing_number(self):
    #     self.assertEqual(reverse_string_slicing("456"), "754", "wrong output with numbers")
    #
    # def test_reverse_string_slicing_empty(self):
    #     self.assertEqual(reverse_string_slicing(""), "")
    #
    # def test_reverse_string_slicing_space(self):
    #     self.assertEqual(reverse_string_slicing(" "), " ")
    #
    # def test_reverse_string_slicing_character(self):
    #     self.assertEqual(reverse_string_slicing("a"), "a")

    # def test_negative_reverse_string_boolean(self):
    #     self.assertRaises(TypeError, reverse_string_slicing, True)


    def test_2_negative_revers_string(self, name, value):
        self.assertRaises(TypeError, reverse_string_slicing, value)

if __name__ == '__main__':
    unittest.main()
