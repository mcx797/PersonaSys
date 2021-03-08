'''
github api文件调用得到字符串
对字符串进行处理得到json文件
梦回编译
'''

import sys
import json
import dataProcessing
import os
from dataProcessing import DataProce
import spider
from spider import githubSpider


spring = DataProce('Spring')
spring.readCommit()
spring.getCommitGraph()





'''
isExists = os.path.exists('spark\co1')
if not isExists:
    os.makedirs('spark\co1')
'''


'''
if isinstance(list_list, list):
    print('kkkkkkkkkkkkkkkkk')
if isinstance(list_list[0], dict):
    print('kkkkkkkkkkkkkkkkk')
'''


'''
for key in list_list[0]:
    print(key)
    print(list_list[0][key])
'''

'''
处理str文本
'''
