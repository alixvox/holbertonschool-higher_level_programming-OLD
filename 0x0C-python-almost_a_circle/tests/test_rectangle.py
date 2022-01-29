#!/usr/bin/python3
"""
Unittesting for the Base module/class
Tests are done for each method of the class.
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import inspect
import pep8


class TestClassRectangle(unittest.TestCase):
    """Test class for testing Rectangle class"""

    @classmethod
    def setUpClass(cls):
        """Sets __nb_object to 0 and creates objects to be tested"""
        Base.clear()
        cls.r1 = Rectangle(10, 5)
        cls.r2 = Rectangle(2, 2, 2, 2, -7)
        cls.r3 = Rectangle(7, 5, 6, 7, 8)
        cls.r4 = Rectangle(1, 1, 4, 2, 78)
        cls.r5 = Rectangle(4, 6, 2, 1, 12)
        cls.r6 = Rectangle(1, 1, 1, 1)
        cls.r7 = Rectangle(10, 2, 1, 9, 1)
        cls.r8 = Rectangle(10, 7, 2, 8)
        cls.r9 = Rectangle(2, 4)
        cls.r10 = Rectangle(3, 5, 1)
        cls.r12 = Rectangle(10, 7, 2, 8)
        cls.r13 = Rectangle(2, 4)

    @classmethod
    def tearDownClass(cls):
        """Deletes all the objects"""
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4
        del cls.r5
        del cls.r6
        del cls.r7
        del cls.r8
        del cls.r9
        del cls.r10
        del cls.r12
        del cls.r13

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

    def test_task_two(self):
        """basic id tests"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, -7)

        with self.assertRaises(TypeError):
            r3 = Rectangle("hello", 4)
            r4 = Rectangle(4, "hello")
            r5 = Rectangle(10, 10, 5.5, 6)
            r6 = Rectangle(64, 85, 3, True)

        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 5)
            r8 = Rectangle(7, 0)
            r9 = Rectangle(9, -4)
            r10 = Rectangle(-5, 6)
            r11 = Rectangle(1, 2, -6, 7)
            r12 = Rectangle(3, 4, 7, -6)

    def test_str(self):
        """tests str"""
        self.assertEqual(str(self.r5), "[Rectangle] (12) 2/1 - 4/6")

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

    def test_update(self):
        """tests update function"""
        self.r6.update(89)
        self.assertEqual(self.r6.id, 89)
        self.r6.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r6.width, 2)
        self.assertEqual(self.r6.height, 3)
        self.assertEqual(self.r6.x, 4)
        self.assertEqual(self.r6.y, 5)
        self.r6.update(width=10, height=9, x=8, y=7, id=11)
        self.assertEqual(self.r6.width, 10)
        self.assertEqual(self.r6.height, 9)
        self.assertEqual(self.r6.x, 8)
        self.assertEqual(self.r6.y, 7)
        self.assertEqual(self.r6.id, 11)

    def test_to_dictionary(self):
        """tests to dictionary"""
        r7_dict = self.r7.to_dictionary()
        self.assertEqual(r7_dict, {'x': 1, 'y': 9, 'id': 1,
                                   'height': 2, 'width': 10})
        self.assertEqual(type(r7_dict), dict)
        self.assertEqual(Rectangle.to_json_string([]), "[]")
        self.assertEqual(Rectangle.to_json_string(None), "[]")

    def test_load_from_file(self):
        """tests load_from_file"""
        list_rectangles_input = [self.r12, self.r13]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]),
                         '[Rectangle] (6) 2/8 - 10/7')

    def setUp(self):
        self.inst = Rectangle(1, 2, 3, 4, 5)

    def test_width(self):
        """
        test rectangle height
        """
        self.assertEqual(self.inst.width, 1)

    def test_height(self):
        """
        test rectangle width
        """
        self.assertEqual(self.inst.height, 2)

    def test_x(self):
        """
        text x
        """
        self.assertEqual(self.inst.x, 3)

    def test_y(self):
        """
        test y
        """
        self.assertEqual(self.inst.y, 4)

    def test_raise_y(self):
        """
        test raise y error
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.inst.y = "Y Error"

    def test_raise_x(self):
        """
        test raise x error
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.inst.x = "X Error"

    def test_raise_width(self):
        """
        test raise width error
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.inst.width = "Width Error"

    def test_raise_height(self):
        """
        test raise heigt
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.inst.height = "Height Error"

    def test_pep8_conformance_rectangle(self):
        """Test that models/rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

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

    def test_too_many_args(self):
        """
        test too many args to init
        """
        with self.assertRaises(TypeError):
            b = Rectangle(1, 1, 2, 3, 4, 5, 6, 7, 8)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

if __name__ == '__main__':
    unittest.main()
