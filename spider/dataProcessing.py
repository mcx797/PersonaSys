'''
对爬取到的数据进行处理，转存
'''

import json
import os
import sys
import graph
from graph import MyGraph
import spider
from spider import githubSpider


class DataProce:
    reposName = "" #编辑的仓库名
    commitList = ""

    def __init__(self, name):
        self.reposName = name

    def readCommit(self):
        srcName = self.reposName + '\commit.txt'
        f = open(srcName, 'r')
        self.commitList = json.loads(f.read())
        f.close()

    def loadCommit(self):
        srcName = self.reposName + '\commit\\'
        for i in range(len(self.commitList)):
            f = open(srcName + self.commitList[i]['sha'] + '\commit.txt', 'a')
            old_sysout = sys.stdout
            sys.stdout = f
            for key in self.commitList[i]:
                print(key)
                print(self.commitList[i][key])
            sys.stdout = old_sysout

    '''
    得到图信息（首先得到所有节点的信息）
    '''
    def getCommitGraph(self):
        myNodes = []
        CommitGraph = MyGraph()
        myspider = githubSpider()
        for i in self.commitList:
            print(i['sha'])
            shaPath = self.reposName + '\commits\\' + i['sha']
            isExists = os.path.exists(shaPath)
            if not isExists:
                os.makedirs(shaPath)
        return CommitGraph




'''
    def toCsv(self, typeName):
        name1 = self.fileName + '.txt'
        filesrc = '/' + self.fileName + '/'
        f = open(name1, 'r')
        str = f.read()
        f.close()
        fileList = json.loads(str)
        print(fileList[2]['parents'])
        if isinstance(fileList, list):
            str111 = filesrc + typeName + '.csv'
            print(str111)
            f = open(str111, 'a')
            f.write("hahaha")
        if isinstance(fileList,dict):
            print(2)
'''
