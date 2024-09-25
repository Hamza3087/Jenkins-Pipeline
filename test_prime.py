import unittest
from prime import is_prime

class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))   # 5 is prime
        self.assertFalse(is_prime(4))   # 4 is not prime
        self.assertTrue(is_prime(13))  # 13 is prime
        self.assertFalse(is_prime(1))   # 1 is not prime
        self.assertFalse(is_prime(0))   # 0 is not prime
        self.assertFalse(is_prime(-7))  # Negative numbers are not prime

if __name__ == '__main__':
    unittest.main()
