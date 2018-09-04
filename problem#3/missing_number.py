import unittest

def find_missing_num(arr:[]):
	shift = segregate(arr)
	diff = len(arr) - shift
	for i in arr[shift:]:
		if abs(i) - 1 < diff and arr[abs(i) - 1 + shift] > 0:
			arr[abs(i) - 1 + shift] = -arr[abs(i) - 1 + shift]
	num = -1
	for idx, val in enumerate(arr[shift:]):
		idx+=shift
		if val > 0:
			num = idx - shift + 1
			break
	return num

def segregate(arr:[]):
	shift = 0
	for idx, val in enumerate(arr):
		if val < 0:
			arr[idx], arr[shift] = arr[shift], arr[idx]
			shift+=1
	return shift

class TestMissingNumber(unittest.TestCase):
	def test_pair(self):
		#self.assertEqual(find_missing_num([2, 12, -1, 13, -2]), 1)
		#self.assertEqual(find_missing_num([3, 4, -1, 1]), 2)
		#self.assertEqual(find_missing_num([1, 2, 3]), -1)
		self.assertEqual(find_missing_num([1, 2, -1]), 3)

if __name__ == '__main__':
    unittest.main()
	#print(find_missing_num([2, 12, -1, 13, -2]))