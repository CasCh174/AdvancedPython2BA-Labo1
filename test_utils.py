#gçit test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0) , 1)
        self.assertEqual(utils.fact(5) , 120)
    
    def test_roots(self):
        self.assertEqual(utils.roots(0,0,1), 0)
        self.assertEqual(utils.roots(2,0,2), ())
    
    def test_integrate(self):
        self.assertTrue(utils.integrate('x**2 - 1', -1, 1) > -1.4)
        self.assertTrue(utils.integrate('x**2 - 1', -1, 1) < -1.2)
        
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
#pour le push
