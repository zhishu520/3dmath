import unittest
from Math.Vec3 import Vec3


class Vec3Test(unittest.TestCase):
    def tearDown(self) -> None:
        pass

    def test_vec3_add(self):
        a, b, c = Vec3(1,1,1), Vec3(1,1,1), Vec3(2,2,2)
        self.assertEqual(a+b, c)

        a, b, c = Vec3(2, 1, 3), Vec3(100, 1.5, 40.2), Vec3(102, 2.5, 43.2)
        self.assertEqual(a+b, c)

    def test_vec3_dot(self):
        a, b, c = Vec3(1,2,3), Vec3(11,22,33), 1*11+2*22+3*33
        self.assertEqual(a*b, c)

