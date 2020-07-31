"""
给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。

另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。

返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）
"""
from typing import List

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dis_list=[ []for i in range(R+C)] #生成一个含有R+C个空列表的空列表
        result=[]
        for i in range(R):
            for j in range(C):
                distanct=abs(i-r0)+abs(j-c0)
                dis_list[distanct].append([i,j])
        for i in dis_list:  #将三层列表变为二层列表
            if i:
                result.extend(i)
            else:
                break
        return result


if __name__=="__main__":
    print(Solution().allCellsDistOrder(1,2,0,0))
