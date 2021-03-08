

class MyGraph:
    Nodes = []
    EdgesSon = []
    EdgesFat = []
    index1 = {}
    index2 = {}

    def __init__(self):
        return

    def sha2id(self, sha):
        return self.index1[sha]

    def addEdge(self, a, b):
        self.EdgesSon.append(a)
        self.EdgesFat.append(b)

    def showIndex1(self):
        for key in self.index1:
            print(key)
            print(self.index1[key])

    def showNode(self, i):
        if i >= len(self.Nodes):
            print("input wrong")
            return
        for key in self.Nodes[i]:
            print(key)
            print(self.Nodes[i][key])

    def showEdges(self):
        for i in range(self.EdgesSon):
            print(self.EdgesFat[i] + "   " + self.EdgesSon[i])