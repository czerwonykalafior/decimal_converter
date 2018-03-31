import unittest

from dec_to_binary import dec_to_bin_rec, dec_to_bin_mem, dec_to_bin_while
from decimal_converter import dec_convert_while


class DecToBinTest(unittest.TestCase):
    def test_dec_to_bin(self):
        self.assertEqual(int(dec_to_bin_while(2)), 10)
        self.assertEqual(int(dec_to_bin_rec(2)), 10)
        self.assertEqual(int(dec_to_bin_mem(2)), 10)

    def test_dec_to_any(self):
        self.assertEqual(int(dec_convert_while(25, 4)), 121)
        self.assertEqual(int(dec_convert_while(35, 4)), 203)
        self.assertEqual(int(dec_convert_while(51, 16)), 33)
        self.assertEqual(int(dec_convert_while(51, 8)), 63)

if __name__ == '__main__':
    unittest.main()
