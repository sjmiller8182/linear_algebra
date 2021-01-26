"""
Implementation of a vector
"""

from typing import List, Tuple, Union
from math import sqrt, acos, pi

def _in_delta(value, target_value, delta) -> bool:
    """
    Check if value is equal to target value within delta
    """
    return abs(value - target_value) < delta

class Vector:
    """
    The class represents a vector and provides utilites for vector operations

    Parameters
    ----------
    entries : list, tuple
        An iterable containing the vector elements

    Attributes
    ----------
    dim
    entries

    Notes
    -----
    The following operations are supported by overloading:
    * '+': scalar addition and vector addition (commutative)
    * '-': scalar subtraction and vector subtraction
    * '@': the dot product (commutative)
    * '*': scalar multiplication and element-wise multiplication
    * '/': scalar division
    """
    def __init__(self, entries: Union[list, tuple]):
        if not (isinstance(entries, list) or isinstance(entries, tuple)):
            raise TypeError(f"Unable to create Vector from object of type \
                {type(entries)}")

        if isinstance(entries, Vector):
            entries = entries.entries

        self.__idx = 0
        self.__entries = (*entries,)
        self.__size = len(self.entries)

    def __iter__(self):
        self.__idx = 0
        return self

    def __next__(self):
        if self.__idx < self.__size:
            result = self.entries[self.__idx]
            self.__idx += 1
            return result
        else:
            raise StopIteration

    def __len__(self):
        return self.__size

    def __eq__(self, v):
        if not isinstance(v, Vector):
            raise Exception(f'Operation "==" between Vector and \
                {type(v)} is not supported')
        if self.__size != len(v.entries):
            return False
        return self.entries == v.entries
    
    def __abs__(self):
        """
        Implemented as euclidean norm
        """
        return sqrt(sum([e**2 for e in self]))

    def __add__(self, other: Union[int, float]):
        """
        Implement scalar addition and vector addition
        """
        # implement scalar addition
        if isinstance(other, int) or isinstance(other, float):
            return Vector([other + e for e in self])
        # implement vector addition
        if isinstance(other, Vector):
            if self.__size != len(other):
                raise Exception(f"Addition is not defined between \
                    vectors of difference sizes. \
                    Sizes found are \
                    {self.__size} and {len(other)}")
            return Vector([o + e for o, e in zip(other, self)])
        else:
            raise TypeError(f"Addition with type {type(other)} is not implemented.")

    def __radd__(self, other: Union[int, float]):
        """
        Implement commutativity for addition
        """
        return self.__add__(other)

    def __truediv__(self, other):
        """
        """
        # implement scalar divison
        if isinstance(other, int) or isinstance(other, float):
            return self.__mul__(1 / other)
        else:
            raise TypeError(f"Divison with type {type(other)} is not implemented.")

    def __matmul__(self, other):
        """
        Implement inner product (dot product)
        """
        if not isinstance(other, Vector):
            raise TypeError("Inner product is only defined between Vectors")
        return sum([e * o for e, o in zip(self, other)])

    def __rmatmul__(self, other):
        """
        Implement communtativity for inner product
        """
        return self.__matmul__(other)

    def __mul__(self, other: Union[int, float]):
        """
        Implement scalar multiplication and element-wise multiplication
        """
        # implement scalar multiplication
        if isinstance(other, int) or isinstance(other, float):
            return Vector([other * e for e in self])
        # implement dot product
        elif isinstance(other, Vector):
            if self.__size != len(other):
                raise Exception(f"Multiplcation is not defined between \
                    vectors of difference sizes. \
                    Sizes found are \
                    {self.__size} and {len(other)}")
            return Vector([o * e for o, e in zip(other, self)])
        else:
            raise TypeError(f"Multiplication with type {type(other)} is not implemented.")
    
    def __rmul__(self, other: Union[int, float]):
        """
        Implement commutativity for multiplication and dot product
        """
        return self.__mul__(other)
    
    def __neg__(self):
        """
        Implement negation
        """
        return Vector([-e for e in self])

    def __repr__(self):
        return "Vector" + str(self.__entries)

    def __sub__(self, other: Union[int, float]):
        """
        Implement self - other
        """
        # implement scalar subtraction
        if isinstance(other, int) or isinstance(other, float):
            return self.__add__(-other)
        # implement vector subtraction
        if isinstance(other, Vector):
            if self.__size != len(other):
                raise Exception(f"Subtraction is not defined between \
                    vectors of difference sizes. \
                    Sizes found are \
                    {self.__size} and {len(other)}")
            return Vector([-o + e for o, e in zip(other, self)])
        else:
            raise TypeError(f"Subtraction with type {type(other)} is not implemented.")

    def __rsub__(self, other: Union[int, float]):
        """
        Implement other - self
        """
        # implement scalar subtraction
        if isinstance(other, int) or isinstance(other, float):
            return other + (-self)
        # implement vector subtraction
        if isinstance(other, Vector):
            if self.__size != len(other):
                raise Exception(f"Subtraction is not defined between \
                    vectors of difference sizes. \
                    Sizes found are \
                    {self.__size} and {len(other)}")
            return Vector([o - e for o, e in zip(other, self)])
        else:
            raise TypeError(f"Subtraction with type {type(other)} is not implemented.")

    @property
    def entries(self) -> tuple:
        """
        Get the entries in the vector

        Returns
        -------
        tuple
            a tuple containing the vector elements
        """
        return self.__entries
    
    @property
    def dim(self) -> int:
        """
        Get the dimension of the vector

        Returns
        -------
        int
            the number of elements in the vector
        """
        return self.__size


    def copy(self):
        """
        Copy vector to new instance

        Returns
        -------
        Vector
            vector copied to new instance
        """
        return Vector([e for e in self])

    def magnitude(self) -> float:
        """
        Caluclate euclidean norm of vector

        Returns
        -------
        float
            the euclidean norm
        """
        return abs(self)

    def unit_vector(self):
        """
        Calculate unit vector

        Returns
        -------
        Vector
            the vector divided by its magnitude
        """
        return self / abs(self)

    def scalar_projection(self, v) -> float:
        """
        Calculate the scalar projection onto v

        Parameters
        ----------
        v : Vector
            a vector of the same size

        Returns
        -------
        float
            the scalar projection onto v
        """
        return self @ v.unit_vector()

    def vector_projection(self, v):
        """
        Calculate the vector projection onto v

        Parameters
        ----------
        v : Vector
            a vector of the same size

        Returns
        -------
        Vector
            the vector projection onto v
        """
        scalar_proj = self.scalar_projection(v)
        return scalar_proj * v.unit_vector()

    def angle(self, v, unit='rad') -> float:
        """
        Calculate angle between vectors

        Parameters
        ----------
        v : Vector
            a vector of the same size
        unit : str
            'rad' for radians or 'deg' for degrees

        Returns
        -------
        float
            the angle between the vectors
        """
        if unit not in ['rad', 'deg']:
            raise ValueError(f"Arg 'unit' must be one of 'deg', \
                'rad'. Got {unit}.")
        dot = self.unit_vector() @ v.unit_vector()
        angle = {
            'rad': acos(dot),
            'deg': acos(dot) * 180 / pi
            }
        return angle.get(unit, angle)

    def is_orthogonal(self, v, tol: float = 1e-10) -> bool:
        """
        Check if vectors are orthogonal

        Parameters
        ----------
        v : Vector
            a vector of the same size
        tol : float
            a tolerance for the check

        Returns
        -------
        bool
            whether the vector is orthogonal
        """
        return (self.unit_vector() @ v.unit_vector()) < tol

    def is_parallel(self, v, tol: float = 1e-10) -> bool:
        """
        Check if vectors are parallel

        Parameters
        ----------
        v : Vector
            a vector of the same size
        tol : float
            a tolerance for the check

        Returns
        -------
        bool
            whether the vector is parallel
        """
        angle = self.angle(v)
        return _in_delta(angle, 0, tol) \
            or _in_delta(angle, pi, tol)

    def is_zero(self, tol: float = 1e-10) -> bool:
        """
        Check if vector is zero

        Parameters
        ----------
        tol : float
            a tolerance for the check

        Returns
        -------
        bool
            whether the vector is teh zero vector
        """
        return all([e < tol for e in self])
