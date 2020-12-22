import time
import copy
from walsh_and_nonlinearity import walshCompute, nonlinearityCompute
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
    八元全输入真值表
'''
def EightVars_AllTruthTable():
    resList = []
    lineLen = pow(2, 8)
    # dicValueOfx = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0}
    # for i1 in range(0, 2):
    #     for i2 in range(0, 2):
    #         for i3 in range(0, 2):
    #             for i4 in range(0, 2):
    #                 for i5 in range(0, 2):
    #                     for i6 in range(0, 2):
    #                         for i7 in range(0, 2):
    #                             for i8 in range(0, 2):
    #                                 dicValueOfx["x1"] = i1
    #                                 dicValueOfx["x2"] = i2
    #                                 dicValueOfx["x3"] = i3
    #                                 dicValueOfx["x4"] = i4
    #                                 dicValueOfx["x5"] = i5
    #                                 dicValueOfx["x6"] = i6
    #                                 dicValueOfx["x7"] = i7
    #                                 dicValueOfx["x8"] = i8
    #                                 resList.append(copy.deepcopy(list(dicValueOfx.values())))
    #                                 with open("eight_vars_input_table.txt", mode="a+", encoding="utf-8") as f:
    #                                      f.write(str(list(dicValueOfx.values())) + "\n")
    with open("eight_vars_input_table.txt", mode="r+", encoding="utf-8") as f:
        for i in range(lineLen):
            line = f.readline()
            lst = strToList(line)
            resList.append(lst)
    return resList


def NineVars_AllTruthTable():
    resList = []
    lineLen = pow(2, 9)
    # dicValueOfx = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0, "x9" : 0}
    # for i1 in range(0, 2):
    #     for i2 in range(0, 2):
    #         for i3 in range(0, 2):
    #             for i4 in range(0, 2):
    #                 for i5 in range(0, 2):
    #                     for i6 in range(0, 2):
    #                         for i7 in range(0, 2):
    #                             for i8 in range(0, 2):
    #                                 for i9 in range(0, 2):
    #                                     dicValueOfx["x1"] = i1
    #                                     dicValueOfx["x2"] = i2
    #                                     dicValueOfx["x3"] = i3
    #                                     dicValueOfx["x4"] = i4
    #                                     dicValueOfx["x5"] = i5
    #                                     dicValueOfx["x6"] = i6
    #                                     dicValueOfx["x7"] = i7
    #                                     dicValueOfx["x8"] = i8
    #                                     dicValueOfx["x9"] = i9
    #                                     resList.append(copy.deepcopy(list(dicValueOfx.values())))
    #                                     with open("nine_vars_input_table.txt", mode="a+", encoding="utf-8") as f:
    #                                         f.write(str(list(dicValueOfx.values())) + "\n")
    with open("nine_vars_input_table.txt", mode="r+", encoding="utf-8") as f:
        for i in range(lineLen):
            line = f.readline()
            lst = strToList(line)
            resList.append(lst)
    return resList



'''
    根据当前布尔函数元数，选择输入全真值表算法
'''
def AllTruthTableSelect(varsNum):
    if varsNum == 8:
        return EightVars_AllTruthTable()
    elif varsNum == 9:
        return NineVars_AllTruthTable()

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
    计算八元布尔函数自相关谱
    truthTable: 该布尔函数真值表
    dicIndexList: 该布尔函数的索引值
    :return 返回自相关谱求和结果
'''
def EightautocorrelationCompute(varsNum, truthTable, dicIndexList):
    ResList = []
    dicOfa = {"a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "a8": 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    dicOfa["a1"] = i1
                                    dicOfa["a2"] = i2
                                    dicOfa["a3"] = i3
                                    dicOfa["a4"] = i4
                                    dicOfa["a5"] = i5
                                    dicOfa["a6"] = i6
                                    dicOfa["a7"] = i7
                                    dicOfa["a8"] = i8
                                    ResList.append(abs(autocorrelation(varsNum, dicOfa, truthTable, dicIndexList)))
    correlationRes = 0
    for i in range(1, len(ResList)):
        correlationRes = ResList[i] + correlationRes
    return correlationRes



'''
    计算八元布尔函数自相关谱
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
    if varsNum == 4:
        return NineautocorrelationCompute(varsNum, truthTable, dicIndexList)
    elif varsNum == 8:
        return EightautocorrelationCompute(varsNum, truthTable, dicIndexList)
    elif varsNum == 9:
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
    计算论文中的cost2
    :return cost2计算结果
'''
def costFunction2(varsNum, truthTable, dicIndexList):
    return transparencyCompute(varsNum, truthTable, dicIndexList)

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
    根据传入的dicIndexList求出八元真值表
'''
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


'''
    根据当前布尔函数元数求出真值表
'''
def TruthTableSelect(varsNum, dicIndexList):
    if varsNum == 4:
        return NineTruthTable(dicIndexList)
    elif varsNum == 8:
        return EightTruthTable(dicIndexList)
    elif varsNum == 9:
        return NineTruthTable(dicIndexList)

'''
    根据传入 翻转RSBF真值表，翻转旋转对称真值表的第i个轨道
'''
def flipTruthTable(varsNum, OribitList, ithOribit):
    dicOribit = {}
    for i in range(len(OribitList)):
        dicOribit[i + 1] = OribitList[i]
    # print(dicOribit)
    oneNumTmpList = []
    for ele in dicOribit:
        if ele == ithOribit:
            oneNumTmpList.append(dicOribit[ele])
    # print(oneNumTmpList)
    transRes = truthTableTrans(varsNum, oneNumTmpList[0])
    # print(transRes)
    # 输出真值表对应的dicIndexList
    return transRes


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


def randomFlapTruthTable(oneNumList, OribitList):
    oneNumResList = []
    for i in range(len(OribitList)):
        num = random.randint(1, len(OribitList))
        if num in oneNumList:
            oneNumList.remove(num)
        else:
            oneNumList.insert(num, num)
        oneNumResList.append(copy.deepcopy(oneNumList))
    return oneNumResList


'''
    获取当前布尔函数的非线性度、透明阶、输出为1索引值的真值表长度
'''
def nonlinearityAndTransparency(varsNum, lst):
    OribitList = finalOribit(varsNum)
    dicIndexList = initRSBF(varsNum, lst, OribitList)

    truthTable = TruthTableSelect(varsNum, dicIndexList)

    res1 = nonlinearityCompute(varsNum, truthTable)
    res2 = transparencyCompute(varsNum, truthTable, dicIndexList)

    return res1, res2, len(dicIndexList)

# [{'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0}, {'x1': 0, 'x2': 0, 'x3': 1, 'x4': 1},
# {'x1': 1, 'x2': 0, 'x3': 0, 'x4': 1}, {'x1': 1, 'x2': 1, 'x3': 0, 'x4': 0},
# {'x1': 0, 'x2': 1, 'x3': 1, 'x4': 0}]

'''
    一次翻转两个短表输出值
'''
def updateRSBF2(oneNumList, OribitList):
    # 记录最后结束输出值
    oneNumResList = []
    # 记录短表长度
    tmpList = []
    for i in range(len(OribitList)):
        tmpList.append(i + 1)

    randNum = []
    # 产生两个随机数
    while 1:
        randNum = np.random.randint(1, 36, 3)
        if randNum[0] != randNum[1] and randNum[0] != randNum[2] and randNum[1] != randNum[2]:
            break

    # print(randNum)
    for ele in randNum:
        if ele in oneNumList:
            oneNumList.remove(ele)
        else:
            oneNumList.insert(ele, ele)


    outputOneNum = 0
    for ele in oneNumList:
        outputOneNum = len(OribitList[ele - 1]) + outputOneNum
    # print(outputOneNum)
    return outputOneNum, oneNumList


if __name__ == '__main__':
    oribit = finalOribit(8)
    count = 0
    for i in range(20):
        count += len(oribit[i])
    print(count)






