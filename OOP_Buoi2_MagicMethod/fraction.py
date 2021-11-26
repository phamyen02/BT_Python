import math
class Fraction(object):
    def __init__(self, nr, dr=1):
        if dr == 0:
            raise ZeroDivisionError("Mẫu số phải khác 0")
        if dr < 0:
            self.nr = -nr
        else:
            self.nr = nr

        self.nr = int(self.nr)
        self.dr = int(abs(dr))
        self.reduce()
    
    def __str__(self) -> str:
        if self.nr == 0:
            return str(self.nr)
        if self.dr == 1:
            return str(self.nr)
        return "%d/%d" % (self.nr, self.dr) 

    def hcf(self):
        return math.gcd(self.nr, self.dr)

    def reduce(self):
        usc = self.hcf()
        self.nr = self.nr / usc
        self.dr = self.dr / usc

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)
        return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)
        return Fraction(self.nr * other.dr - other.nr * self.dr, self.dr * other.dr)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)
        return Fraction(self.nr * other.dr, other.nr * self.dr)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)
        return Fraction(self.nr * other.nr, self.dr * other.dr)

if __name__ == '__main__':
    f1 = Fraction(1, 2)
    print(f1)
    f2 = Fraction(2, 9)
    print(f2)

    print(f'{f1} + {f2} = {f1 + f2}')
    print(f'{f1} - {f2} = {f1 - f2}')
    print(f'{f1} / {f2} = {f1 / f2}')
    print(f'{f1} * {f2} = {f1 * f2}')