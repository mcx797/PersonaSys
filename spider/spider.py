import sys
import urllib.request

class githubSpider:
    authorName = "MengTo"
    codeName = "Spring"
    gitName = authorName + '/' + codeName + '/'

    def __init__(self, name, code):
        self.authorName = name
        self.codeName = code

    def __init__(self):
        return

    def spiderCommitList(self):
        commitUrlName = "https://api.github.com/repos/" + self.gitName + "commits"
        strHtml = urllib.request.urlopen(commitUrlName).read()
        fileName = self.codeName + '\\commit.txt'
        f = open(fileName, 'a')
        old_sysout = sys.stdout
        sys.stdout = f
        print(strHtml)
        sys.stdout = old_sysout

    def spiderCommitMes(self, Sha):
        commitUrlName = "https://api.github.com/repos/" + self.gitName + 'commits/' + Sha
        strHtml = urllib.request.urlopen(commitUrlName).read()
        print(strHtml)
        return strHtml

