
import unittest
import challenge_functions as cf


class TestChallenge(unittest.TestCase):
    def test_divisible_by_five_and_seven(self):
        self.assertEqual(cf.divisible_by_five_and_seven(100, 210), [100, 110, 115, 120, 125, 130, 135, 145, 150, 155, 160, 165, 170, 180, 185, 190, 195, 200, 205])
    
    def test_base_converter(self):
        self.assertEqual(cf.base_converter(25, 2), '11001')
        self.assertEqual(cf.base_converter(25, 8), '31')
        
    def test_perfect_squares(self):
        self.assertEqual(sum(cf.perfect_squares(30)), 55)
        self.assertEqual(sum(cf.perfect_squares(10)), 14)
        self.assertEqual(sum(cf.perfect_squares(100)), 285)
        
    def test_find_phrase(self):
        self.assertTrue(cf.find_phrase("Just not all at once", "data.txt"))
        self.assertFalse(cf.find_phrase("hello", "data.txt"))
        
    def test_sum_column(self):
        self.assertEqual(sum(cf.sum_column('data.csv', 0)), 15)
        self.assertEqual(sum(cf.sum_column('data.csv', 2)), 21)


if __name__ == '__main__':
    unittest.main()