import unittest
import sys
sys.path.append('./TimeProcess')
from TimeLine import TimeLine

# 并集测试
class intersectTest(unittest.TestCase):
    # 空
    def test1(self):
        tl = []
        result = TimeLine.intersect(tl)
        self.assertEqual(result,[])
    # 单个时间线
    def test2(self):
        tl = [
            [1,10]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result,[
        ])
    # 不相交
    def test3(self):
        tl = [
            [1,10],
            [20,100]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result,[
        ])

    # 边界贴合
    def test3(self):
        tl = [
            [1, 10],
            [10, 100]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [10,10]
        ])
    # 首尾一致
    def test4(self):
        tl = [
            [10, 10],
            [10, 10]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [10,10]
        ])
    # 重叠
    def test5(self):
        tl = [
            [1, 10],
            [1, 10]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [1,10]
        ])
    # 相交
    def test6(self):
        tl = [
            [1, 10],
            [5, 20]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [5,10]
        ])
    # 完全包含
    def test7(self):
        tl = [
            [1, 10],
            [5, 9]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [5,9]
        ])
    # 左边界
    def test8(self):
        tl = [
            [1, 10],
            [1, 9]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [1,9]
        ])
    # 右边界
    def test9(self):
        tl = [
            [1, 10],
            [5, 10]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [5,10]
        ])
    # 多个包含
    def test10(self):
        tl = [
            [1, 100],
            [20, 90],
            [30, 70],
            [40, 60],
            [50, 55],
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [20,90]
        ])
    # 多个包含
    def test11(self):
        tl = [
            [1, 100],
            [20, 110],
            [0, 70]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [1,70],
            [70,100]
        ])
    # 多个包含
    def test12(self):
        tl = [
            [1, 100],
            [10, 50],
            [50, 70]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [10, 50],
            [50, 70]
        ])
    # 多个包含
    def test13(self):
        tl = [
            [1, 100],
            [10, 50],
            [40, 70]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [10, 50],
            [50, 70]
        ])
    # 多个重叠
    def test14(self):
        tl = [
            [1, 3],
            [2, 4],
            [3, 5],
            [4, 6],
            [5, 7],
            [6, 8]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [6, 7]
        ])
    # 多个不相交
    def test15(self):
        tl = [
            [1, 3],
            [4, 6],
            [7, 9],
            [10, 12],
            [13, 15],
            [16, 18]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
        ])
    # 多个边界贴合
    def test16(self):
        tl = [
            [1, 3],
            [3, 6],
            [6, 9],
            [9, 12],
            [12, 15],
            [15, 18]
        ]
        result = TimeLine.intersect(tl)
        self.assertEqual(result, [
            [3, 3],
            [6, 6],
            [9, 9],
            [12, 12],
            [15, 15]
        ])