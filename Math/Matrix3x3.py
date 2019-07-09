
from Math.Vec3 import Vec3

class Matrix3x3(object):

    def __init__(self, arr):
        if type(arr) is list:
            self.m11, self.m12, self.m13 = arr[0][0], arr[0][1], arr[0][2]
            self.m21, self.m22, self.m23 = arr[1][0], arr[1][1], arr[1][2]
            self.m31, self.m32, self.m33 = arr[2][0], arr[2][1], arr[2][2]
        elif type(arr) == Matrix3x3:
            self.m11, self.m12, self.m13 = arr.m11, arr.m12, arr.m13
            self.m21, self.m22, self.m23 = arr.m21, arr.m22, arr.m23
            self.m31, self.m32, self.m33 = arr.m31, arr.m32, arr.m33
        else:
            self.m11, self.m12, self.m13 = 0, 0, 0
            self.m21, self.m22, self.m23 = 0, 0, 0
            self.m31, self.m32, self.m33 = 0, 0, 0

    def __mul__(self, other):
        if type(other) is Matrix3x3:
            r = Matrix3x3()

            r.a11 = self.m11 * other.m11 + self.m12 * other.m21 + self.m13 * other.m31
            r.a12 = self.m11 * other.m12 + self.m12 * other.m22 + self.m13 * other.m32
            r.a13 = self.m11 * other.m13 + self.m12 * other.m23 + self.m13 * other.m33

            r.a21 = self.m21 * other.m11 + self.m22 * other.m21 + self.m23 * other.m31
            r.a22 = self.m21 * other.m12 + self.m22 * other.m22 + self.m23 * other.m32
            r.a23 = self.m21 * other.m13 + self.m22 * other.m23 + self.m23 * other.m33

            r.a31 = self.m31 * other.m11 + self.m32 * other.m21 + self.m33 * other.m31
            r.a32 = self.m31 * other.m12 + self.m32 * other.m22 + self.m33 * other.m32
            r.a33 = self.m31 * other.m13 + self.m32 * other.m23 + self.m33 * other.m33

        elif type(other) is Vec3:
            # 列向量
            return Vec3(
                other.x * self.m11 + other.y * self.m12 + other.z * self.m13,
                other.x * self.m21 + other.y * self.m22 + other.z * self.m23,
                other.x * self.m31 + other.y * self.m32 + other.z * self.m33,
            )

    def __rmul__(self, other):
        if type(other) is Matrix3x3:
            r = Matrix3x3()

            r.a11 = other.m11 * self.m11 + other.m12 * self.m21 + other.m13 * self.m31
            r.a12 = other.m11 * self.m12 + other.m12 * self.m22 + other.m13 * self.m32
            r.a13 = other.m11 * self.m13 + other.m12 * self.m23 + other.m13 * self.m33

            r.a21 = other.m21 * self.m11 + other.m22 * self.m21 + other.m23 * self.m31
            r.a22 = other.m21 * self.m12 + other.m22 * self.m22 + other.m23 * self.m32
            r.a23 = other.m21 * self.m13 + other.m22 * self.m23 + other.m23 * self.m33

            r.a31 = other.m31 * self.m11 + other.m32 * self.m21 + other.m33 * self.m31
            r.a32 = other.m31 * self.m12 + other.m32 * self.m22 + other.m33 * self.m32
            r.a33 = other.m31 * self.m13 + other.m32 * self.m23 + other.m33 * self.m33

        elif type(other) is Vec3:
            # 行向量
            return Vec3(
                other.x * self.m11 + other.y * self.m12 + other.z * self.m13,
                other.x * self.m21 + other.y * self.m22 + other.z * self.m23,
                other.x * self.m31 + other.y * self.m32 + other.z * self.m33,
            )








