import unittest
from functions_error import append, prepend, insert

class TesyMyMethods(unittest.TestCase):
    def test_prepend(self):
        self.assertEqual(prepend("bar", "foo"), "foobar")
    def test_append(self):
        self.assertEqual(append("bar", "foo"), "barfoo")
    def test_insert(self):
        self.assertEqual(insert("wetor", "buca", 2), "webucator")
        # the above test fail, insert should return s[0:pos] + c + s[pos:] to be correct.

if __name__ == "__main__":
    unittest.main()