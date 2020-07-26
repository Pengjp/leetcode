def removeDuplicates(S):
    if len(S) == 1:
        return S
    from collections import deque
    d = deque()
    d.append(S[0])
    
    for i in S[1:]:
        if d and i == d[-1]:
            d.pop()
        else:
            d.append(i)
    return ''.join((d))

import unittest

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(removeDuplicates("abbaca"), 'ca')
        self.assertEqual(removeDuplicates("a"), 'a')
        self.assertEqual(removeDuplicates("aa"), '')

if __name__ == '__main__':
    unittest.main()