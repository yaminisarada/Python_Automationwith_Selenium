import unittest
from Examples import Example

class Mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This will run before class")
    @classmethod
    def tearDownClass(cls):
        print("This will run after class")
    def setUp(self):
        print("This will run before all methods")
    def tearDown(self):
        print("This will run after all methods")

    def test_add(self):
        result = Example.add(self,10, 20)
        self.assertEqual(result, 30)
        print("This is addition")
    def test_sub(self):
        result = Example.sub(self, 40, 20)
        self.assertEqual(result, 20)
        print("This is sub")

    # def test_example(self):
    #     self.assertEqual(Example.add(self,10,20), 30)
    #     self.assertEqual(Example.sub(self, 40, 20), 20)

if __name__ == '__main__':
    unittest.main()
