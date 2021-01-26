"""
Tests for the Vector class
"""

import unittest
import math
from vector import Vector

class TestProperties(unittest.TestCase):
    def test_dim(self):
        v = Vector([2,5])
        self.assertEqual(2, v.dim)

    def test_entries(self):
        v = Vector([2,5])
        self.assertEqual(2, v.entries[0])
        self.assertEqual(5, v.entries[1])

class TestCopy(unittest.TestCase):

    def test_copy(self):
        v = Vector([2,5])
        u = v.copy()
        self.assertFalse(v is u)

class TestAddition(unittest.TestCase):
    
    def test_vector_addition_communtivity(self):
        v = Vector([1,6])
        u = Vector([2,7])
        vector_sum_left = v + u
        vector_sum_right = u + v
        self.assertTrue(isinstance(vector_sum_right, Vector))
        self.assertTrue(isinstance(vector_sum_right, Vector))
        self.assertEqual(3, vector_sum_left.entries[0])
        self.assertEqual(3, vector_sum_right.entries[0])
        self.assertEqual(13, vector_sum_left.entries[1])
        self.assertEqual(13, vector_sum_right.entries[1])

    def test_scalar_addition_communtivity(self):
        v = Vector([1,6])
        vector_sum_left = v + 2
        vector_sum_right = 2 + v
        self.assertTrue(isinstance(vector_sum_right, Vector))
        self.assertTrue(isinstance(vector_sum_right, Vector))
        self.assertEqual(3, vector_sum_left.entries[0])
        self.assertEqual(3, vector_sum_right.entries[0])
        self.assertEqual(8, vector_sum_left.entries[1])
        self.assertEqual(8, vector_sum_right.entries[1])

    def test_addition_idenity(self):
        v = Vector([1,6])
        zero_vector = Vector([0,0])
        vector_sum = v + zero_vector
        self.assertTrue(isinstance(vector_sum, Vector))
        self.assertEqual(1, vector_sum.entries[0])
        self.assertEqual(6, vector_sum.entries[1])

    def test_exception_difference_sizes(self):
        v = Vector([1,6,1])
        u = Vector([2,7])
        with self.assertRaises(Exception):
            v + u
    
    def test_not_valid_type(self):
        v = Vector([1,6])
        u = (1,2)
        with self.assertRaises(TypeError):
            v + u

class TestIteration(unittest.TestCase):

    def test_iteration(self):
        v = Vector([0,1,5])
        elements = [e for e in v]
        self.assertEqual(3, len(elements))
        self.assertEqual(0, elements[0])
        self.assertEqual(1, elements[1])
        self.assertEqual(5, elements[2])

class TestEquality(unittest.TestCase):

    def test_equal_vectors(self):
        v = Vector([0,1,5])
        u = Vector([0,1,5])
        self.assertTrue(u==v)

    def test_unequal_same_size(self):
        u = Vector([4,5])
        v = Vector([1,5])
        self.assertFalse(u==v)

    def test_unequal_size_vectors(self):
        u = Vector([4,5])
        v = Vector([1,5,4])
        self.assertFalse(u==v)

class TestMultiplcation(unittest.TestCase):

    def test_scalar_multiplication(self):
        v = Vector([4,5])
        u = 4 * v
        w = v * 4
        self.assertTrue(isinstance(u, Vector))
        self.assertTrue(isinstance(w, Vector))
        self.assertEqual(16, u.entries[0])
        self.assertEqual(16, w.entries[0])
        self.assertEqual(20, u.entries[1])
        self.assertEqual(20, w.entries[1])

    def test_sclar_identity(self):
        v = Vector([4,5])
        v = 1 * v
        self.assertTrue(isinstance(v, Vector))
        self.assertEqual(4, v.entries[0])
        self.assertEqual(5, v.entries[1])

    def test_elementwise_multiplication(self):
        v = Vector([4,5])
        u = Vector([3,2])
        left_mul = v * u
        right_mul = u * v
        self.assertTrue(isinstance(left_mul, Vector))
        self.assertTrue(isinstance(right_mul, Vector))
        self.assertEqual(12, left_mul.entries[0])
        self.assertEqual(12, right_mul.entries[0])
        self.assertEqual(10, left_mul.entries[1])
        self.assertEqual(10, right_mul.entries[1])

    def test_elementwise_idenity(self):
        v = Vector([4,5])
        u = Vector([1,1])
        identity = v * u
        self.assertTrue(isinstance(identity, Vector))
        self.assertEqual(4, identity.entries[0])
        self.assertEqual(5, identity.entries[1])

class TestNegation(unittest.TestCase):

    def test_negation(self):
        v = Vector([4,5])
        v = -v
        self.assertTrue(isinstance(v, Vector))
        self.assertEqual(-4, v.entries[0])
        self.assertEqual(-5, v.entries[1])

class TestSubtraction(unittest.TestCase):

    def test_scalar_subtraction(self):
        v = Vector([4,5])
        v = v - 1
        self.assertTrue(isinstance(v, Vector))
        self.assertEqual(3, v.entries[0])
        self.assertEqual(4, v.entries[1])

        v = Vector([4,5])
        v = 1 - v
        self.assertTrue(isinstance(v, Vector))
        self.assertEqual(-3, v.entries[0])
        self.assertEqual(-4, v.entries[1])

    def test_vector_subtraction(self):
        v = Vector([4,5])
        u = Vector([2,2])
        v = v - u
        self.assertTrue(isinstance(v, Vector))
        self.assertEqual(2, v.entries[0])
        self.assertEqual(3, v.entries[1])

        v = Vector([4,5])
        u = Vector([2,2])
        v = u - v
        self.assertTrue(isinstance(v, Vector))
        self.assertEqual(-2, v.entries[0])
        self.assertEqual(-3, v.entries[1])

class TestDotProduct(unittest.TestCase):

    def test_dot_product(self):
        v = Vector([4,5])
        u = Vector([3,2])
        dot_prod_left = v @ u
        dot_prod_right = u @ v
        self.assertEqual(22, dot_prod_left)
        self.assertEqual(22, dot_prod_right)

class TestDivision(unittest.TestCase):

    def test_scalar_division(self):
        v = Vector([4,10])
        v = v / 2
        self.assertTrue(isinstance(v, Vector))
        self.assertAlmostEqual(2, v.entries[0], 10)
        self.assertAlmostEqual(5, v.entries[1], 10)

class TestMagnitude(unittest.TestCase):

    def test_magnitude(self):
        v = Vector([3, 4])
        mag = abs(v)
        self.assertEqual(5, mag)
        mag = v.magnitude()
        self.assertEqual(5, mag)

class TestUnitVector(unittest.TestCase):

    def test_unit_vector(self):
        v = Vector([2,2])
        unit_v = v.unit_vector()

        unit_vals = 2 / math.sqrt(8)

        self.assertTrue(isinstance(unit_v, Vector))
        self.assertAlmostEqual(unit_vals, unit_v.entries[0], 10)
        self.assertAlmostEqual(unit_vals, unit_v.entries[0], 10)

class TestAngle(unittest.TestCase):

    def test_angle_zero(self):
        v = Vector([2,0])
        u = Vector([1,0])
        angle_rad = v.angle(u, unit='rad')
        angle_deg = v.angle(u, unit='deg')
        self.assertAlmostEqual(0, angle_rad, 10)
        self.assertAlmostEqual(0, angle_deg, 10)

    def test_angle_180(self):
        v = Vector([-2,0])
        u = Vector([1,0])
        angle_rad = v.angle(u, unit='rad')
        angle_deg = v.angle(u, unit='deg')
        self.assertAlmostEqual(math.pi, angle_rad, 10)
        self.assertAlmostEqual(180, angle_deg, 10)

    def test_angle_90(self):
        v = Vector([0,1])
        u = Vector([1,0])
        angle_rad = v.angle(u, unit='rad')
        angle_deg = v.angle(u, unit='deg')
        self.assertAlmostEqual(math.pi / 2, angle_rad, 10)
        self.assertAlmostEqual(90, angle_deg, 10)

    def test_invalid_unit(self):
        v = Vector([0,1])
        u = Vector([1,0])
        with self.assertRaises(ValueError):
            v.angle(u, unit='somethingelse')

class TestIsOrthogonal(unittest.TestCase):

    def test_is_orthogonal(self):
        v = Vector([0,1])
        u = Vector([1,0])
        self.assertTrue(v.is_orthogonal(u))

        v = Vector([1,0])
        u = Vector([1,0])
        self.assertFalse(v.is_orthogonal(u))

class TestIsParallel(unittest.TestCase):

    def test_is_parallel(self):
        v = Vector([2,0])
        u = Vector([1,0])
        self.assertTrue(v.is_parallel(u))

        v = Vector([-2,0])
        u = Vector([1,0])
        self.assertTrue(v.is_parallel(u))

        v = Vector([-2,2])
        u = Vector([1,0])
        self.assertFalse(v.is_parallel(u))

class TestIsZero(unittest.TestCase):

    def test_is_zero(self):
        v = Vector([0,0])
        self.assertTrue(v.is_zero())
