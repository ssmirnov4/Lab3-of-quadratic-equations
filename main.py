import unittest

from equaration import discriminant

class TestDiscriminant(unittest.TestCase):
    def setUp(self):
        self.result = discriminant(1, 7, 6)

    def testDiscriminant1(self):
        result = discriminant(1, 7, 6)
        self.assertEqual(result, (f"Корни данного уравнения: x1 = {-6.0}, x2 = {-1.0}"))

    def testDiscriminant2(self):
        result = discriminant(0, 2, -2)
        self.assertEqual(result, (f"Данное уравнение имеет один корень: x = {1.0}"))

    def testDiscriminant3(self):
        result = discriminant(1, 2, 76)
        self.assertEqual(result,("Данное уравнение корней не имеет"))

    def testDiscriminant4(self):
        result = discriminant(1, -4, 4)
        self.assertEqual(result, (f"Данное уравнение имеет один корень: x = {2.0}"))

    def testDiscriminant5(self):
        result = discriminant(0, 0, 1)
        self.assertEqual(result, ("Данное уравнение корней не имеет"))


if __name__ == "__main__":
  unittest.main()