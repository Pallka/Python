import unittest
import math
from unittest.mock import patch

def solve_kvadrat_equation(a, b, c):
    """Функція для розв'язання квадратного рівняння ax^2 + bx + c = 0"""

    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        raise TypeError("Коефіцієнти повинні бути числами")
    
    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0:
        raise ValueError("Коефіцієнт 'a' не може бути нулем.")

    descriminant = pow(b, 2) - 4*a*c
    
    if descriminant < 0:
        return None 
    elif descriminant >= 0:
        x1 = (-b + math.sqrt(descriminant)) / (2*a)
        x2 = (-b - math.sqrt(descriminant)) / (2*a)
        return (x1, x2)
    # else:
    #     x = -b / (2*a)
    #     return x

def main():
    print("Програма для розв'язання квадратного рівняння ax^2 + bx + c = 0")
    try:
        a = input("Введіть коефіцієнт a=")
        b = input("Введіть коефіцієнт b=")
        c = input("Введіть коефіцієнт c=")
        result = solve_kvadrat_equation(a, b, c)
        if result is None:
            print("Розв'язків немає")
        else:
            print("Корені рівняння:", result)
    except ValueError:
        print("Помилка. Будь ласка, введіть числові значення!")

class TestFindResultKvadratEquation(unittest.TestCase):
    def test_koef_is_number(self):
        with self.assertRaises(TypeError):
            solve_kvadrat_equation("string", "four", "two")

    def test_koef_is_bool(self):
        with self.assertRaises(TypeError):
            solve_kvadrat_equation("true", "true", "false")

    def test_koef(self):
        with self.assertRaises(TypeError):
            solve_kvadrat_equation("3", "1", "5")

    def test_no_solution(self):
        self.assertIsNone(solve_kvadrat_equation(2, 2, 1))

    def test_two_solutions(self):
        self.assertEqual(solve_kvadrat_equation(1, -5, 6), (3.0, 2.0))

    def test_one_solution(self):
        self.assertEqual(solve_kvadrat_equation(1, -6, 9), (3.0, 3.0))

    def test_zero_a(self):
        with self.assertRaises(ValueError):
            solve_kvadrat_equation(0, 2, 1)

    @patch('__main__.solve_kvadrat_equation') 
    def test_mocked__KvadratEquation(self, mock__KvadratEquation):
        mock__KvadratEquation.return_value = (3.0, 3.0)
       
        result = solve_kvadrat_equation(1, -6, 9)
        
        mock__KvadratEquation.assert_called_once_with(1, -6, 9)
        
        self.assertEqual(result, (3.0, 3.0))

if __name__ == "__main__":
    # main()
    unittest.main(exit=False)
