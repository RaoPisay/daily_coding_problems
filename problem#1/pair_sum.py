import unittest

def is_pair_exists(arr, sum):
	sets = set()
	for i in arr:
		if sets.__contains__(i):
			return True
		sets.add(sum - i)
	return False

class TestPairSum(unittest.TestCase):
	def test_pair(self):
		self.assertTrue(is_pair_exists([10, 15, 3, 7], 17))
		self.assertTrue(is_pair_exists([10, 15, 3, 7], 18))
		self.assertFalse(is_pair_exists([10, 15, 3, 7], 19))
		self.assertFalse(is_pair_exists([10, 15, 3, 7], 20))
		self.assertTrue(is_pair_exists([10, 15, 3, 7], 10))
		self.assertTrue(is_pair_exists([10, 15, 3, 7], 13))
		self.assertTrue(is_pair_exists([10, 15, 3, 7], 25))
		self.assertTrue(is_pair_exists([10, 15, 3, 7], 22))
		self.assertTrue(is_pair_exists([1,0], 1))
		self.assertTrue(is_pair_exists([0,0], 0))

if __name__ == '__main__':
    unittest.main()