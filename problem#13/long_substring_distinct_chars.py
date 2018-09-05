import unittest

def get_long_substring(bigstr:str, k:int):
    #Base cases
    word_len = len(bigstr)
    if bigstr is None or len(bigstr) < 1 or k < 1:
        return None
    elif word_len <= k:
        return bigstr
    i = 0
    j = 0
    chars = set()
    word = ''
    long_word = ''
    while i < word_len:
        chars.add(bigstr[i])
        if len(chars) <= k:
            word+=bigstr[i]
        else:
            if len(long_word) < len(word):
                long_word = word
            i=j
            j+=1
            word = ''
            chars.clear()
        i+=1
    if len(long_word) < len(word):
        long_word = word
    return long_word

class TestLongSubString(unittest.TestCase):
    def test_long_substr(self):
        self.assertEqual("bcb", get_long_substring('abcba', 2))
        self.assertEqual("abcba", get_long_substring('abcba', 3))
        self.assertEqual("abcdea", get_long_substring('abcdefghabcdea', 5))
        self.assertEqual(None, get_long_substring('abcba', 0))
        self.assertEqual(None, get_long_substring('', 0))
        self.assertEqual("abcbdefghihkl", get_long_substring('abcbdefghihkl', 20))
        
    
if __name__ == '__main__':
    unittest.main()