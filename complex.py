#!/usr/bin/env python

import math

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

if __name__ == '__main__':
    pass
