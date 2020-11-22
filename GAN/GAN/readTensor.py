import copy
import tensorflow as tf
import numpy as np

def tensorToStrArr(address):
    resLst = []
    with open(address, mode = "r+", encoding="utf-8") as f:
        tmp = f.read()
        leftbarc = 0
        rightbarc = 0
        strTmp = ""
        for ele in tmp:
            if leftbarc == 2:
                if ele is not ']' and ele is not '\n':
                    strTmp += ele
                    continue
                elif ele is ']':
                    rightbarc += 1
                    if rightbarc == 2:
                        leftbarc = 0
                        rightbarc = 0
                        resLst.append(strTmp)
                        strTmp = ""
            if ele == '[':
               leftbarc += 1
    return resLst

def strArrToArr(strArr):
    resLst = []
    for ele in strArr:
        tmpLst = []
        for i in range(len(ele) - 1):
            if ele[i].isdigit() and ele[i + 1].isdigit():
                tmpLst.append(int(ele[i]) * 10 + int(ele[i + 1]))
            elif ele[i].isdigit() and not ele[i - 1].isdigit():
                tmpLst.append(int(ele[i]))
            if (i == len(ele) - 2) and ele[len(ele) - 1].isdigit() and not ele[len(ele) - 2].isdigit():
                tmpLst.append(int(ele[len(ele) - 1]))
        resLst.append(copy.deepcopy(tmpLst))
    return resLst

def uniqueLst(matrix):
    tmpList = []
    for ele in matrix:
        tmpList.append(copy.deepcopy(list(set(ele))))
    resList = []
    for ele in tmpList:
        if 0 in ele:
            ele.remove(0)
        resList.append(ele)
    return resList

def resultMatrix(address):
    strArr = tensorToStrArr(address)
    arr = strArrToArr(strArr)
    return uniqueLst(arr)

def tensorTransToArr(tensor):
    resList = []
    for ele in tensor:
        resList.append(int(ele) + 1)
    return resList

def uniqueList(lst):
    s = set(lst)
    return list(s)

if __name__ == '__main__':

    # print(resultMatrix("res.txt")[0])
    tensor = tf.constant([1,2,3,4])
    print(tensor)
    res = tensorTransToArr(tensor)
    print(res, type(res))




