

from Math.Vec3 import Vec3
from Math.Matrix3x3 import Matrix3x3
from Math.MathUtils import MathUtils


if __name__ == '__main__':

    v = Vec3(10,0,0)
    m = Matrix3x3.getRotateMatrix(3, MathUtils.PI / 2)
    print(m)
    print(v * m)
