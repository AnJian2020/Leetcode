"""
树的存储结构，双亲表示法
"""
class PTNode(object):
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent

class PTree(object):
    def __init__(self):
        self.nodes=[]
        self.n=0