import unittest
import sys
sys.path.append('./TimeProcess')
from TimeLine import TimeLine

# 并集测试
class unionTest(unittest.TestCase):
    # 空
    def test1(self):
        tl = []
        result = TimeLine.union(tl)
        self.assertEqual(result,[])
    # 单个时间线
    def test2(self):
        tl = [
            [1,10]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result,[
            [1,10]
        ])
    # 不相交
    def test3(self):
        tl = [
            [1,10],
            [20,30]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result,[
            [1,10],
            [20,30]
        ])
    # 相交
    def test4(self):
        tl = [
            [1,10],
            [5,30]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result,[
            [1,30]
        ])
    # 重叠
    def test5(self):
        tl = [
            [1,10],
            [1,10]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result,[
            [1,10]
        ])

    # 完全包含
    def test6(self):
        tl = [
            [1, 10],
            [5, 9]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result, [
            [1, 10]
        ])

    # 左边界
    def test7(self):
        tl = [
            [1, 10],
            [1, 9]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result, [
            [1, 10]
        ])

    # 右边界
    def test8(self):
        tl = [
            [1, 10],
            [2, 10]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result, [
            [1, 10]
        ])
    # 多个包含
    def test9(self):
        tl = [
            [1, 10],
            [2, 9],
            [3, 8]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result, [
            [1, 10]
        ])
    # 多个重叠
    def test10(self):
        tl = [
            [1, 3],
            [2, 4],
            [3, 5],
            [4, 6]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result, [
            [1, 6]
        ])

    # 多个不相交
    def test10(self):
        tl = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result, [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ])

    # 多个边界贴合
    def test11(self):
        tl = [
            [1, 3],
            [3, 5],
            [5, 7],
            [7, 9]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result, [
            [1, 9]
        ])

    # 左右相等
    def test12(self):
        tl = [
            [2, 2]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result, [
            [2, 2]
        ])

    # 多个左右相等
    def test13(self):
        tl = [
            [2, 2],
            [2, 2]
        ]
        result = TimeLine.union(tl)
        self.assertEqual(result, [
            [2, 2]
        ])
