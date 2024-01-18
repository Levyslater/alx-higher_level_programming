#!/usr/bin/python3
"""Test case for rectangle class"""
import unittest
import os
import sys
import io
import logging
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_integers(self):
        rectangle = Rectangle(18, 9, 3, 4, 2)
        self.assertEqual(rectangle.width, 18)
        self.assertEqual(rectangle.height, 9)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)
        self.assertEqual(rectangle.id, 2)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 4, 2, 1, 2)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -1, 2, 2, 3)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 3, -2, 2, 3)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 3, 2, -2, 3)

    def test_invalid_type_width(self):
        with self.assertRaises(TypeError):
            Rectangle("str", 4, 2, 3, 1)

    def test_invalid_type_height(self):
        with self.assertRaises(TypeError):
            Rectangle(7, "str", 2, 3, 1)

    def test_invalid_type_x(self):
        with self.assertRaises(TypeError):
            Rectangle(7, 4, "str", 3, 1)

    def test_invalid_type_y(self):
        with self.assertRaises(TypeError):
            Rectangle(7, 4, 2, "str", 1)

    def test_area(self):
        rectangle = Rectangle(10, 5, 3, 2, 1)
        self.assertEqual(rectangle.area(), 50)
    def test_display(self):
        rectangle = Rectangle(3, 2, 1, 0, 1)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            rectangle.display()
            output = captured_output.getvalue().strip().split('\n')
        finally:
            sys.stdout = sys.__stdout__

        expected_output = ['###', ' ###']
        self.assertEqual(output, expected_output)
    def test_str(self):
        rectangle = Rectangle(10, 5, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (4) 2/3 - 10/5")

    def test_update_args(self):
        rectangle = Rectangle(10, 5, 2, 3, 1)
        rectangle.update(2, 8, 4, 6, 1)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 6)
        self.assertEqual(rectangle.y, 1)

    def test_update_kwargs(self):
        rectangle = Rectangle(10, 5, 2, 3, 1)
        rectangle.update(id=2, width=8, height=4, x=6, y=1)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 6)
        self.assertEqual(rectangle.y, 1)

    def test_to_dictionary(self):
        rectangle = Rectangle(10, 5, 2, 3, 1)
        dictionary = rectangle.to_dictionary()
        return_dct = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        self.assertEqual(dictionary, return_dct)


if __name__ == "__main__":
    unittest.main()
