import unittest

def prod_arr(arr, prod_arr = []):
    prod = 1
    for i in arr:
        prod*=i
    for i in arr:
        prod_arr.append(divide(prod, i))
    return prod_arr

def divide(numer, denomer):
    result = 0
    while numer >=denomer:
        result+=1
        numer-=denomer
    return result

class TestProdArr(unittest.TestCase):
    def test_prod_arr(self):
        self.assertEqual([120, 60, 40, 30, 24], prod_arr([1, 2, 3, 4, 5]))

if __name__ == '__main__':
    unittest.main()