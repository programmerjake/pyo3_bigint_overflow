from pyo3_bigint_overflow import to_string
import unittest


class TestBigInt(unittest.TestCase):
    def test_bigint(self):
        for i in range(0, 128):
            for v in (1 << i, (1 << i) - 1, -1 << i, (-1 << i) - 1):
                with self.subTest(i=i, v=v):
                    self.assertEqual(str(v), to_string(v))
