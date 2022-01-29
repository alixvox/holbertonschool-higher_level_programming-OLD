#!/usr/bin/python3
"""
Unittesting for the Base module/class
Tests are done for each method of the class.
"""
import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestClassRectangle(unittest.TestCase):
    """Test class for testing Rectangle class"""
    def test_pep8_rectangle(self):
            """
            Test that models/rectanlge.py is pep8 compliant.
            """
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['models/rectangle.py'])
            self.assertEqual(result.total_errors, 0, "Found \
            code style errors (and warnings).")

    def test_pep8_test_rectangle(self):
        """
        Test that tests/test_rectangle.py is pep8 compliant
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found \
        code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.area.__doc__) >= 1)

    def test_attributes_correct(self):
        """
        Test attributes of a correctly instantiated Rectangle
        """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_attributes_incorrect(self):
        """
        Test incorrectly instantiated Rectangles.
        """
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 1, -1, -1)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 'hi')

    def test_attribute_setters(self):
        """
        Test setter methods for Rectangle attributes.
        """
        r5 = Rectangle(1, 2, 3, 4, 5)
        r5.width = 3
        r5.height = 5
        r5.x = 7
        r5.y = 9
        r5.id = 15
        self.assertTrue(r5.width, 3)
        self.assertTrue(r5.height, 5)
        self.assertTrue(r5.x, 7)
        self.assertTrue(r5.y, 9)
        self.assertTrue(r5.id, 15)
        with self.assertRaises(TypeError):
            r5.width = 'raccoon'
        with self.assertRaises(TypeError):
            r5.height = 'oppossum'
        with self.assertRaises(TypeError):
            r5.x = 'fox'
        with self.assertRaises(TypeError):
            r5.y = 'badger'
        with self.assertRaises(ValueError):
            r5.width = 0
        with self.assertRaises(ValueError):
            r5.height = -5
        with self.assertRaises(ValueError):
            r5.x = -2
        with self.assertRaises(ValueError):
            r5.y = -100

    def test_area(self):
        """
        Test method area()
        """
        r6 = Rectangle(3, 4)
        self.assertEqual(r6.area(), 12)

    def test_str(self):
        """
        Test method __str__.
        """
        r7 = Rectangle(2, 3, 1, 1)
        r7_str = "[Rectangle] (4) 1/1 - 2/3        "
        print(r7.__str__())
        self.assertEqual(r7.__str__(), r7_str)

if __name__ == "__main__":
    unittest.main()
