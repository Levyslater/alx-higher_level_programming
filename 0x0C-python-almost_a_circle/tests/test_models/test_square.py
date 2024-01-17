#!/usr/bin/python3
"""Test case for square class"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_init(self):
        # Test constructor
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_invalid_size(self):
        # Test invalid size
        with self.assertRaises(ValueError):
            Square(0, 2, 3, 1)

    def test_invalid_type_size(self):
        # Test invalid type for size
        with self.assertRaises(TypeError):
            Square("5", 2, 3, 1)

    def test_size_property(self):
        # Test size property
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        # Test size setter
        square = Square(5, 2, 3, 1)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_str(self):
        # Test string representation
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update_args(self):
        # Test update method with positional arguments
        square = Square(5, 2, 3, 1)
        square.update(2, 8, 6, 1)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 1)

    def test_update_kwargs(self):
        # Test update method with keyword arguments
        square = Square(5, 2, 3, 1)
        square.update(id=2, size=8, x=6, y=1)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 1)

    def test_to_dictionary(self):
        # Test to_dictionary method
        square = Square(5, 2, 3, 1)
        dictionary = square.to_dictionary()
        expected_dict = {'id': 1, 'x': 2, 'size': 5, 'y': 3}
        self.assertEqual(dictionary, expected_dict)

if __name__ == '__main__':
    unittest.main()