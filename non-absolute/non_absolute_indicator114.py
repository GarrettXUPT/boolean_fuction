import copy
from RSBF import initRSBF, TruthTableSelect, finalOribit, AllTruthTableSelect
from S_Box_nonlinearity import hexToBinary
from walsh_and_nonlinearity import nonlinearityCompute
from transparency import transparencyCompute
from multiprocessing import Process
from flieToLst import fileToList1

'''
    三元模加
    input: w的生成结果
    :return x + a的模加结果
'''
def ThreeVarsAddMol(dicOfw):
    dicOfValue = {"x1" : 0, "x2" : 0, "x3" : 0}
    resList = []
    lstOfw = list(dicOfw.values())
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                dicOfValue["x1"] = i1
                dicOfValue["x2"] = i2
                dicOfValue["x3"] = i3
                lstOfValue = list(dicOfValue.values())
                for i in range(len(dicOfw)):
                    resList.append((lstOfw[i] + lstOfValue[i]) % 2)
    return resList

'''
    四元模加
    input: w的生成结果
    :return x + a的模加结果
'''
def FourVarsAddMol(dicOfw):
    dicOfValue = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0}
    resList = []
    lstOfw = list(dicOfw.values())
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    dicOfValue["x1"] = i1
                    dicOfValue["x2"] = i2
                    dicOfValue["x3"] = i3
                    dicOfValue["x4"] = i4
                    lstOfValue = list(dicOfValue.values())
                    for i in range(len(dicOfw)):
                        resList.append((lstOfw[i] + lstOfValue[i]) % 2)
    return resList

'''
    五元模加
    input: w的生成结果
    :return x + a的模加结果
'''
def FiveVarsAddMol(dicOfw):
    dicOfValue = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0}
    resList = []
    lstOfw = list(dicOfw.values())
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        dicOfValue["x1"] = i1
                        dicOfValue["x2"] = i2
                        dicOfValue["x3"] = i3
                        dicOfValue["x4"] = i4
                        dicOfValue["x5"] = i5
                        lstOfValue = list(dicOfValue.values())
                        for i in range(len(dicOfw)):
                            resList.append((lstOfw[i] + lstOfValue[i]) % 2)
    return resList

'''
    八元模加
    input: w的生成结果
    :return x + a的模加结果
'''
def EightVarsAddMol(dicOfw):
    dicOfValue = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0}
    resList = []
    lstOfw = list(dicOfw.values())
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    dicOfValue["x1"] = i1
                                    dicOfValue["x2"] = i2
                                    dicOfValue["x3"] = i3
                                    dicOfValue["x4"] = i4
                                    dicOfValue["x5"] = i5
                                    dicOfValue["x6"] = i6
                                    dicOfValue["x7"] = i7
                                    dicOfValue["x8"] = i8
                                    lstOfValue = list(dicOfValue.values())
                                    for i in range(len(dicOfw)):
                                        resList.append((lstOfw[i] + lstOfValue[i]) % 2)
    return resList


def NineVarsAddMol(dicOfw):
    dicOfValue = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0, "x9" : 0}
    resList = []
    lstOfw = list(dicOfw.values())
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    for i9 in range(0, 2):
                                        dicOfValue["x1"] = i1
                                        dicOfValue["x2"] = i2
                                        dicOfValue["x3"] = i3
                                        dicOfValue["x4"] = i4
                                        dicOfValue["x5"] = i5
                                        dicOfValue["x6"] = i6
                                        dicOfValue["x7"] = i7
                                        dicOfValue["x8"] = i8
                                        dicOfValue["x9"] = i9
                                        lstOfValue = list(dicOfValue.values())
                                        for i in range(len(dicOfw)):
                                            resList.append((lstOfw[i] + lstOfValue[i]) % 2)
    return resList


'''
    按当前布尔函数元数进行模加选择
'''
def AddmolSelect(varsNum, dicOfa):
    if varsNum == 3:
        return ThreeVarsAddMol(dicOfa)
    elif varsNum == 4:
        return FourVarsAddMol(dicOfa)
    elif varsNum == 5:
        return FiveVarsAddMol(dicOfa)
    elif varsNum == 8:
        return EightVarsAddMol(dicOfa)
    elif varsNum == 9:
        return NineVarsAddMol(dicOfa)


'''
    自相关谱的计算
    :return 自相关谱累加计算结果
'''
def autocorrelation(varsNum, dicOfa, truthTable, dicIndexList):

    valueList = []
    for ele in dicIndexList:
        valueList.append(list(ele.values()))

    addModList = AddmolSelect(varsNum, dicOfa)
    addResListTmp = []
    addResList = []

    for i in range(pow(2, varsNum)):
        addResListTmp.append(addModList[0 + varsNum * i : varsNum + varsNum * i])

    for i in range(len(addResListTmp)):
        for ele in valueList:
            if ele == addResListTmp[i]:
                addResListTmp[i] = "vaild"

    for ele in addResListTmp:
        if ele == "vaild":
            addResList.append(1)
        else:
            addResList.append(0)
    # print(addResList)  # [1, 0, 0, 0, 0, 1, 0, 1]

    indexAddResList = truthAdd(truthTable, addResList)
    ResTmpList = []
    for ele in indexAddResList:
        if ele == 0:
            ResTmpList.append(1)
        else:
            ResTmpList.append(-1)

    Res = 0
    for ele in ResTmpList:
        Res = ele + Res
    return Res


'''
    计算自相关谱指数部分 f(x) + f(x + d)
    :return 计算结果

'''
def truthAdd(truthTable, addResList):
    ResList = []
    for i in range(len(truthTable)):
        ResList.append((truthTable[i] + addResList[i]) % 2)
    return ResList

def non_absolute_indicator(varsNum, truthTable, dicIndexList):
    ResList = []
    dicOfa = {"a1": 0, "a2": 0, "a3": 0, "a4" : 0, "a5" : 0, "a6" : 0, "a7" : 0, "a8" : 0}
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
                                    ResList.append((autocorrelation(varsNum, dicOfa, truthTable, dicIndexList)))

    return max(ResList[1:])


def normalIndex(varsNum, truthTable):
    resList = []
    allThTable = AllTruthTableSelect(varsNum)
    for i in range(len(truthTable)):
        if truthTable[i] == 1:
            tableDic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
            for j in range(len(allThTable[i])):
                tableDic[j] = allThTable[i][j]
            resList.append(copy.deepcopy(tableDic))
    return resList

def fileToProcess(address, varsNum, oribitList, nonlinearity, ith):
    tableVec = fileToList1(address)
    for ele in tableVec:
        dicIndexList = initRSBF(varsNum, ele[0], oribitList)
        truthTable = TruthTableSelect(varsNum, dicIndexList)
        non_absolute = non_absolute_indicator(varsNum, truthTable, dicIndexList)
        with open("result/" + str(nonlinearity) + "_" + str(non_absolute) + "_" + str(ith) + ".txt", mode = "a+", encoding="utf-8") as f:
            f.write(str(ele) + "    " + str(non_absolute) + "\n")



def test():
    varsNum = 8
    hexTruthTable = "18CA9ED8BC4EC1AFE2F4C023FA63E78949455BC59DB873BE79409BAE4B289029"
    truthTable = hexToBinary(hexTruthTable)
    dicIndexList = normalIndex(varsNum, truthTable)
    res1 = nonlinearityCompute(varsNum, truthTable)
    res2 = transparencyCompute(varsNum, truthTable, dicIndexList)
    print("nonlinearity = ", res1)
    print("transparency = ", res2)
    res = non_absolute_indicator(varsNum, truthTable, dicIndexList)
    print("non_absolute_indicator = ", res)


def divProcess(ith):
    varsNum = 8
    oribitList = finalOribit(varsNum)
    fileToProcess("divData/" + "114" + "_" + str(ith) + ".txt", varsNum, oribitList, 114, ith)
    print(str(ith) + " check")

if __name__ == '__main__':
    for i in range(32):
        p1 = Process(target=divProcess, args=(i ,))  # args为创建进程的传参方式
        p1.start()

    # varsNum = 8
    # allThTable = AllTruthTableSelect(varsNum)
    # oribitList = finalOribit(varsNum)
    # nonlinearity = 116
    # for i in range(1, 33):
    #     fileToProcess("divData/" + str(nonlinearity) + "_" + str(i) + ".txt", varsNum, oribitList, nonlinearity)
    #
    # nonlinearity = 114
    # for i in range(1, 33):
    #     fileToProcess("divData/" + str(nonlinearity) + "_" + str(i) + ".txt", varsNum, oribitList, nonlinearity)
    #
    # nonlinearity = 112
    # for i in range(1, 33):
    #     fileToProcess("divData/" + str(nonlinearity) + "_" + str(i) + ".txt", varsNum, oribitList, nonlinearity)


