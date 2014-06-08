#!/usr/bin/env python

import math

# exceptions
class InvalidVectorException(Exception):
    pass
class VectorLenMismatchException(Exception):
    pass

# complex number, in Cartesian representation
class Complex(object):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __repr__(self):
        if self.a == 0:
            real_part = None
        else:
            real_part = str(self.a)

        if self.b == 0:
            imag_part = None
        elif self.b == 1:
            imag_part = 'i'
        elif self.b == -1:
            imag_part = '-i'
        else:
            imag_part = '{0}i'.format(self.b)

        if not real_part and not imag_part:
            return '0'

        if real_part and not imag_part:
            return real_part

        if imag_part and not real_part:
            return imag_part

        if self.b > 0:
            return '{0}+{1}'.format(real_part, imag_part)
        else:
            return '{0}{1}'.format(real_part, imag_part)

    def __add__(self, other):
        return Complex(
            self.a + other.a,
            self.b + other.b)

    def __sub__(self, other):
        return Complex(
            self.a - other.a,
            self.b - other.b)

    def __mul__(self, other):
        return Complex(
            self.a*other.a - self.b*other.b,
            self.a*other.b + other.a*self.b)

    def __div__(self, other):
        x = (self.a*other.a + self.b*other.b) / (other.a**2 + other.b**2)
        y = (other.a*self.b - self.a*other.b) / (other.a**2 + other.b**2)
        return Complex(x, y)

    def modulus(self):
        return math.sqrt(self.a**2 + self.b**2)

    def conjugate(self):
        return Complex(self.a, -self.y)

    # convert to polar coordinates
    def polar(self):
        p = self.modulus()
        theta = math.atan(self.a / self.b)
        return ComplexPolar(p, theta)

# complex number, in polar representation
class ComplexPolar(object):
    def __init__(self, p, theta):
        self.p = p
        self.theta = theta

    def __repr__(self):
        return 'p={0}, theta={1}'.format(self.p, self.theta)

    # convert to Cartesian coordinates
    def cartesian(self):
        a = self.p * math.cos(self.theta)
        b = self.p * math.sin(self.theta)
        return Complex(a, b)

# a vector in complex number space
class ComplexVector(object):
    def __init__(self, L):
        for c in L:
            if not isinstance(c, Complex):
                raise InvalidVectorException()
        self.L = L

    def __repr__(self):
        return str(self.L)

    def check_len(self, other):
        if len(self.L) == len(other.L):
            return True
        raise VectorLenMismatchException()

    def __add__(self, other):
        if not self.check_len(other):
            return

        L = []
        for i in range(len(self.L)):
            L.append(self.L[i] + other.L[i])
        return ComplexVector(L)

    def inverse(self):
        L = []
        for c in self.L:
            L.append(Complex(-c.a, -c.b))
        return ComplexVector(L)

    def scalar_mul(self, scalar_c):
        L = []
        for c in self.L:
            L.append(c*scalar_c)
        return ComplexVector(L)


if __name__ == '__main__':
    pass
