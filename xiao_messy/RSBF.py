import time
import copy
from walsh_and_nonlinearity import walshCompute, nonlinearityCompute
from innerproduct import innerProductSelect
from transparency import truthTableAndIndexLixt, autocorrelation, transparencyCompute
import random
from innerproduct import strToList
import numpy as np


"================================创建轨道(四、六、八元)======================================"
'''
    真值表输入循环移位
    input: lst 当前需要移位的列表
'''
def moveBit(lst, num):
    tmpList = copy.deepcopy(lst)
    for i in range(num):
        tmpList.insert(0, tmpList.pop())
    return tmpList

'''
    轨道输入移位
    input: oribit 当前需要移位的轨道
    output: 移位结果
'''
def oribitMoveBit(varsNum, oribit):
    oribitRes = []
    for i in range(varsNum):
        oribitRes.append(moveBit(oribit, i))
    return oribitRes



'''
    根据当前布尔函数元数，选择输入全真值表算法
'''
def AllTruthTableSelect(varsNum):
    TableList = []
    for i in range(0, pow(2, varsNum)):
        tmp = str(bin(i)).split("0b")
        for elem in tmp:
            if elem == '':
                continue
            tmpList = []
            for element in elem:
                tmpList.append(int(element))
            if len(tmpList) != varsNum:
                for i in range(varsNum - len(tmpList)):
                    tmpList.insert(0, 0)
            TableList.append(copy.deepcopy(tmpList))
    return TableList


'''
    去掉各轨道中重复的输入项
'''
def removedepriate(elementList, List):
    FlagList = []
    for ele in List:
        for elem in elementList:
            if elem in ele:
                FlagList.append(False)
            else:
                FlagList.append(True)
    if False in FlagList:
        return False
    else:
        return True

'''
    创建轨道输入项
'''
def generateOribit(varsNum, truthTable):
    tmpList = [[]]
    depriateFlag = True
    for i in range(len(truthTable)):
        oribitTmp = oribitMoveBit(varsNum, truthTable[i])
        depriateFlag = removedepriate(oribitTmp, tmpList)
        if depriateFlag is True:
            tmpList.append(oribitTmp)
    # print(tmpList[1 : ])
    # for ele in tmpList[1 : ]:
    #     print(ele)
    # print(len(tmpList[1 : ]))
    resList = []
    for ele in tmpList[1 : ]:
        tmp = []
        for elem in ele:
            if elem not in tmp:
                tmp.append(elem)
        resList.append(tmp)
    # for ele in resList:
    #     print(ele)
    # print(len(resList))
    return resList
"========================================================================================"
'''
    生成当前轨道数，及各轨道真值表输入
    :return 得到各轨道取值
'''
def finalOribit(varsNum):
    truthTable = AllTruthTableSelect(varsNum)
    resList = generateOribit(varsNum, truthTable)
    # for ele in resList:
    #     print(ele)
    # print(len(resList))
    # print(resList)
    return resList


'''
    根据小项表达式计算多项式该项的值
    :return 返回该项的值
'''
def itemRes(dic_index, dic_value):
    for key in dic_value.keys():
        if dic_value.get(key) != dic_index.get(key):
            return 0
    return 1



'''
    计算九元布尔函数自相关谱
    truthTable: 该布尔函数真值表
    dicIndexList: 该布尔函数的索引值
    :return 返回自相关谱求和结果
'''
def NineautocorrelationCompute(varsNum, truthTable, dicIndexList):
    ResList = []
    dicOfa = {"a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "a8": 0, "a9": 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    for i9 in range(0, 2):
                                        dicOfa["a1"] = i1
                                        dicOfa["a2"] = i2
                                        dicOfa["a3"] = i3
                                        dicOfa["a4"] = i4
                                        dicOfa["a5"] = i5
                                        dicOfa["a6"] = i6
                                        dicOfa["a7"] = i7
                                        dicOfa["a8"] = i8
                                        dicOfa["a9"] = i9
                                        ResList.append(abs(autocorrelation(varsNum, dicOfa, truthTable, dicIndexList)))
    correlationRes = 0
    for i in range(1, len(ResList)):
        correlationRes = ResList[i] + correlationRes
    return correlationRes


def autocorrelationSelect(varsNum, truthTable, dicIndexList):
    if varsNum == 9:
        return NineautocorrelationCompute(varsNum, truthTable, dicIndexList)


'''
    计算论文中的cost1
    :return cost1计算结果
'''
def costFunction1(varsNum, Truthtable, dicIndexList):
    walshSqureList = []
    walshResList = walshCompute(varsNum, Truthtable)
    # print(walshResList)

    for ele in walshResList:
        walshSqureList.append(ele ** 2)
    # print(walshSqureList)
    oneTermResTmpList = []
    for ele in walshSqureList:
        oneTermResTmpList.append(pow((ele - pow(2, varsNum)), 3))
    # print(oneTermResTmpList)

    oneTermRes = 0
    for ele in oneTermResTmpList:
        oneTermRes = ele + oneTermRes
    # print(oneTermRes)  # 28731506688
    twoTermRes = autocorrelationSelect(varsNum, Truthtable, dicIndexList)
    # print(twoTermRes)

    costOneRes = oneTermRes - twoTermRes
    return costOneRes


'''
    将真值表输入项(真值表2 ** n 长)转化为适合使用的dicIndexList
'''
def truthTableTrans(varsNum, oneNumListEle):
    Dic = {}
    List = []
    num = 0
    for ele in oneNumListEle:
        for elem in ele:
            Dic[num % varsNum] = elem
            num = num + 1
        List.append(copy.deepcopy(Dic))
    return List


'''
    根据传入的dicIndexList求出九元真值表
'''
def NineTruthTable(dicIndexList):
    resList = []
    hang = len(dicIndexList)
    dic_value = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    for i9 in range(0, 2):
                                        dic_value[0] = i1
                                        dic_value[1] = i2
                                        dic_value[2] = i3
                                        dic_value[3] = i4
                                        dic_value[4] = i5
                                        dic_value[5] = i6
                                        dic_value[6] = i7
                                        dic_value[7] = i8
                                        dic_value[8] = i9
                                        resTmpList = []
                                        for i in range(0, hang):
                                            resTmpList.append(itemRes(dicIndexList[i], dic_value))
                                        resList.append(sum(resTmpList) % 2)
    return resList

def EightTruthTable(dicIndexList):
    resList = []
    hang = len(dicIndexList)
    dic_value = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    dic_value[0] = i1
                                    dic_value[1] = i2
                                    dic_value[2] = i3
                                    dic_value[3] = i4
                                    dic_value[4] = i5
                                    dic_value[5] = i6
                                    dic_value[6] = i7
                                    dic_value[7] = i8
                                    resTmpList = []
                                    for i in range(0, hang):
                                        resTmpList.append(itemRes(dicIndexList[i], dic_value))
                                    resList.append(sum(resTmpList) % 2)
    return resList


def TenTruthTable(dicIndexList):
    resList = []
    hang = len(dicIndexList)
    dic_value = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    for i9 in range(0, 2):
                                        for i10 in range(0, 2):
                                            dic_value[0] = i1
                                            dic_value[1] = i2
                                            dic_value[2] = i3
                                            dic_value[3] = i4
                                            dic_value[4] = i5
                                            dic_value[5] = i6
                                            dic_value[6] = i7
                                            dic_value[7] = i8
                                            dic_value[8] = i9
                                            dic_value[9] = i10
                                            resTmpList = []
                                            for i in range(0, hang):
                                                resTmpList.append(itemRes(dicIndexList[i], dic_value))
                                            resList.append(sum(resTmpList) % 2)
    return resList


def ElevenTruthTable(dicIndexList):
    resList = []
    hang = len(dicIndexList)
    dic_value = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    for i9 in range(0, 2):
                                        for i10 in range(0, 2):
                                            for i11 in range(0, 2):
                                                dic_value[0] = i1
                                                dic_value[1] = i2
                                                dic_value[2] = i3
                                                dic_value[3] = i4
                                                dic_value[4] = i5
                                                dic_value[5] = i6
                                                dic_value[6] = i7
                                                dic_value[7] = i8
                                                dic_value[8] = i9
                                                dic_value[9] = i10
                                                dic_value[10] = i11
                                                resTmpList = []
                                                for i in range(0, hang):
                                                    resTmpList.append(itemRes(dicIndexList[i], dic_value))
                                                resList.append(sum(resTmpList) % 2)
    return resList

def TwelveTruthTable(dicIndexList):
    resList = []
    hang = len(dicIndexList)
    dic_value = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    for i9 in range(0, 2):
                                        for i10 in range(0, 2):
                                            for i11 in range(0, 2):
                                                for i12 in range(0, 2):
                                                    dic_value[0] = i1
                                                    dic_value[1] = i2
                                                    dic_value[2] = i3
                                                    dic_value[3] = i4
                                                    dic_value[4] = i5
                                                    dic_value[5] = i6
                                                    dic_value[6] = i7
                                                    dic_value[7] = i8
                                                    dic_value[8] = i9
                                                    dic_value[9] = i10
                                                    dic_value[10] = i11
                                                    dic_value[11] = i12
                                                    resTmpList = []
                                                    for i in range(0, hang):
                                                        resTmpList.append(itemRes(dicIndexList[i], dic_value))
                                                    resList.append(sum(resTmpList) % 2)
    return resList


'''
    根据当前布尔函数元数求出真值表
'''
def TruthTableSelect(varsNum, dicIndexList):
    if varsNum == 8:
        return EightTruthTable(dicIndexList)
    elif varsNum == 9:
        return NineTruthTable(dicIndexList)
    elif varsNum == 10:
        return TenTruthTable(dicIndexList)
    elif varsNum == 11:
        return ElevenTruthTable(dicIndexList)
    elif varsNum == 12:
        return TwelveTruthTable(dicIndexList)



'''
    input: 当前布尔函数元数
    oneNumOribitList: 当前输出为1的真值表列表
    OribitList:当前布尔函数的轨道真值表
    
    output: dicIndexList(当前布尔函数对应的索引值)
'''
def initRSBF(varsNum, oneNumOribitList, OribitList):
    # print("该布尔函数轨道总数" ,len(OribitList))
    dicOribit = {}
    for i in range(len(OribitList)):
        dicOribit[i + 1] = OribitList[i]

    oneNumList = []
    # print(len(oneNumOribitList))
    # print(oneNumOribitList)
    for ele in oneNumOribitList:
        oneNumList.append(dicOribit[ele])
    # print(oneNumList)

    transList = []
    for i in range(len(oneNumList)):
        transList.append(truthTableTrans(varsNum, oneNumList[i]))
    # print(transList)

    indexList = []
    for ele in transList:
        for elem in ele:
            indexList.append(elem)
    return indexList

def transparencyBoundy(varsNum, nonlinearity):
    firstTerm = ((pow(2, varsNum) - 2 * nonlinearity) ** 2) / (pow(2, varsNum) * (pow(2, varsNum) - 1))
    secondTerm = 1 / (pow(2, varsNum) - 1)
    return 1 - firstTerm + secondTerm

'''
    获取当前布尔函数的非线性度、透明阶、输出为1索引值的真值表长度
'''
def nonlinearityAndTransparency(varsNum, lst, innerProduct, OribitList):
    dicIndexList = initRSBF(varsNum, lst, OribitList)

    truthTable = TruthTableSelect(varsNum, dicIndexList)
    balanceFlag = ""
    if truthTable.count(1) == pow(2, varsNum - 1):
        balanceFlag = "balanced function"
    else:
        balanceFlag = "unbalanced function"
    res1 = nonlinearityCompute(varsNum, truthTable, innerProduct)
    res2 = transparencyCompute(varsNum, truthTable, dicIndexList)
    # print("nonlinearity = " + str(res1), "  transparency = " + str(res2))
    return res1, res2, balanceFlag


def RSST_to_NormalTable(varsNum, RSST, allOribitList, eigthAllTable):
    allTableLen = len(eigthAllTable)
    allOribitLen = len(allOribitList)

    i = 0
    truthDic = {}
    for ele in eigthAllTable:
        truthDic[i] = ele
        i += 1

    j = 0
    oribitDic = {}
    for ele in allOribitList:
        oribitDic[j] = ele
        j += 1

    oneNumLst = []
    for ele in RSST:
        for i in range(allOribitLen):
            if ele == (list(oribitDic.keys())[i] + 1):
                oneNumLst.append(copy.deepcopy(list(oribitDic.values())[i]))

    truthTable = []
    for ele in oneNumLst:
        for elem in ele:
            for i in range(allTableLen):
                if elem == (list(truthDic.values())[i]):
                    truthTable.append(list(truthDic.keys())[i] + 1)

    '''
        供测试使用
    '''
    # for ele in truthTable:
    #     for i in range(1, allTableLen + 1):
    #         if ele == i:
    #             print(eigthAllTable[i - 1])
    # print(truthTable)

    return truthTable

if __name__ == '__main__':

    start = time.time()
    varsNum = 8
    # oneNumList = [1, 3, 6, 11, 12, 13, 16, 18, 19, 20, 24, 26, 27, 28, 29, 31, 32, 33, 35, 36, 38, 39, 40, 44, 46, 47, 48, 51, 52, 53, 54, 60]
    oneNumList = [2, 4, 16, 17, 18, 19, 20, 21, 22, 24, 26, 28, 29, 30, 31, 34, 35, 36]
    #
    # oneNumList = [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 18, 19, 20, 22, 23, 24, 28, 29, 35, 36, 38, 39, 41, 43, 44, 45, 47, 51, 53, 54, 55, 56, 62, 66, 67, 68, 70, 71, 72, 74, 75, 79, 81, 83, 88, 89, 93, 94, 98, 99, 100, 101, 106, 107, 108, 109, 110, 111, 113, 116, 118, 119, 120, 121, 128, 130, 133, 138, 139, 140, 141, 142, 149, 152, 153, 155, 156, 159, 160, 161, 163, 164, 167, 168, 169, 171, 173, 176, 177, 179, 180, 182, 186, 187]
    OribitList = finalOribit(varsNum)
    all = AllTruthTableSelect(varsNum)
    print(len(OribitList))
    dicIndexList = initRSBF(varsNum, oneNumList, OribitList)
    truthTable = TruthTableSelect(varsNum, dicIndexList)
    # print(len(truthTable))
    # print(truthTable.count(1))
    # truthTable = RSST_to_NormalTable(varsNum, oneNumList, OribitList, all)
    # start = time.time()
    res1 = nonlinearityCompute(varsNum, truthTable)
    # res2 = transparencyCompute(varsNum, truthTable, dicIndexList)
    end = time.time()
    print("nonlinearity = ", res1)
    # print("transparency", res2)
    # print("during time is ", end - start)


 






