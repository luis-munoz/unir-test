import math


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y
    
    def square_root(self, x):
        self.check_types_single(x)
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(x)
    
    def log10(self, x):
        self.check_types_single(x)
        if x <= 0:
            raise ValueError("Cannot calculate logarithm of zero or negative number")
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

    def check_types_single(self, x):
        """Validación de tipo para operaciones de un solo parámetro"""
        if not isinstance(x, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    
    print("=== Calculator Demo ===\n")
    
    # ADD
    result = calc.add(2, 2)
    print(f"ADD: 2 + 2 = {result}")
    
    # SUBSTRACT
    result = calc.substract(5, 3)
    print(f"SUBSTRACT: 5 - 3 = {result}")
    
    # MULTIPLY
    result = calc.multiply(3, 4)
    print(f"MULTIPLY: 3 * 4 = {result}")
    
    # DIVIDE
    result = calc.divide(10, 2)
    print(f"DIVIDE: 10 / 2 = {result}")
    
    # POWER
    result = calc.power(2, 3)
    print(f"POWER: 2 ^ 3 = {result}")
    
    # SQUARE ROOT
    result = calc.square_root(16)
    print(f"SQUARE ROOT: √16 = {result}")
    
    # LOG10
    result = calc.log10(100)
    print(f"LOG10: log10(100) = {result}")
    
    print("\n=== All operations completed successfully! ===")