# -*- coding:utf-8 -*-
"""
time: 2020/6/18
author: xuhao
"""
from typing import List
import os
class Solution:
    def departmentOptimization(self,n:int,people:List)->List:
        """
        :param n: 优化次数
        :param people: 各个项目组的人数
        :return: 经历n次优化后各个项目组的人数
        """
        while n>0:
            maxPeople=max(people)
            maxPeopleIndex=people.index(max(people))
            people[maxPeopleIndex]=maxPeople-3
            item = 0
            while item <len(people):
                if item !=maxPeopleIndex:
                    people[item]+=1
                item+=1
            n-=1
        return people


if __name__=="__main__":
    print(Solution().departmentOptimization(10,[10,10,5,4]))