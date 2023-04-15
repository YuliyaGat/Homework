class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def dec_mistake(func):
       def wrapped(self, elem):
         if not isinstance(elem, type(self)) or not isinstance(self.denominator, int) or not isinstance(elem.denominator, int) or not isinstance(self.numerator, int) or not isinstance(elem.numerator, int):
             try:
               raise Exception
             except Exception:
               return ('Wrong type for operand')
         elif self.denominator == 0 or elem.denominator == 0:
            try:
               raise ZeroDivisionError
            except ZeroDivisionError:
               return ('Divide by 0 is not possible')
         else:
             return func(self, elem)
       return wrapped

    @dec_mistake
    def __add__(self, other):
        #self.mistakes(other)
        num = self.numerator*other.denominator + other.numerator*self.denominator
        den = self.denominator * other.denominator
        num, den = shorten_fraction(num, den)
        return Fraction(int(num), int(den))

    @dec_mistake
    def __sub__(self, other):
        #self.mistakes(other)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        num, den = shorten_fraction(num, den)
        return Fraction(int(num), int(den))

    @dec_mistake
    def __mul__(self, other):
        #self.mistakes(other)
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        num, den = shorten_fraction(num, den)
        return Fraction(int(num), int(den))

    @dec_mistake
    def __truediv__(self, other):
        p = other.denominator
        other.denominator = other.numerator
        other.numerator = p
        n = self.__mul__(other)
        other.numerator = other.denominator
        other.denominator = p
        return n

    @dec_mistake
    def __eq__(self, other):
        num1, num2 = common_denominator (self.numerator, self.denominator, other.numerator, other.denominator)
        return num1 == num2

    @dec_mistake
    def __ne__(self, other):
        num1, num2 = common_denominator (self.numerator, self.denominator, other.numerator, other.denominator)
        return num1 != num2

    @dec_mistake
    def __gt__(self, other):
        num1, num2 = common_denominator (self.numerator, self.denominator, other.numerator, other.denominator)
        return num1 > num2

    @dec_mistake
    def __lt__(self, other):
        num1, num2 = common_denominator (self.numerator, self.denominator, other.numerator, other.denominator)
        return num1 < num2

    @dec_mistake
    def __ge__(self, other):
        num1, num2 = common_denominator (self.numerator, self.denominator, other.numerator, other.denominator)
        return num1 >= num2

    @dec_mistake
    def __le__(self, other):
        num1, num2 = common_denominator (self.numerator, self.denominator, other.numerator, other.denominator)
        return num1 <= num2

    def __str__(self):
        return f'Fraction({self.numerator}, {self.denominator})'
    def __repr__(self):
        return self.__str__()

def shorten_fraction(a, b):
    j = 1
    while j != 0:
        j = 0
        for i in range(2, int(min(abs(a), abs(b))) + 1):
            if a % i == 0 and b % i == 0:
                a /= i
                b /= i
                j += 1
    return a, b

def common_denominator(n1,d1,n2,d2):
    #com_den = d1 * d2
    num1 = n1 * d2
    num2 = n2 * d1
    return num1, num2

if __name__ == "__main__":
  _x = Fraction(1, 2)
  _y = Fraction(1, 4)
  print(_x + _y)
  print(_x - _y)
  print(_x * _y)
  print(_x / _y)
  print(_x + _y == Fraction(3, 4))
