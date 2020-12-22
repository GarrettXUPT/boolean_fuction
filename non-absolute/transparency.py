
from truthTable import truthTableSelect

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
    计算真值表及小项表示指数
    :return 返回计算结果
'''
def truthTableAndIndexLixt(varsNum):
    dicIndexList = []
    truthTable = truthTableSelect(varsNum, dicIndexList)
    return truthTable, dicIndexList

'''
    计算自相关谱指数部分 f(x) + f(x + d)
    :return 计算结果
    
'''
def truthAdd(truthTable, addResList):
    ResList = []
    for i in range(len(truthTable)):
        ResList.append((truthTable[i] + addResList[i]) % 2)
    return ResList

'''
    三元透明阶的计算
    :return 返回计算结果
'''
def ThreeVarsTransparencyCompute(varsNum, truthTable, dicIndexList):
    ResList = []
    dicOfa = {"a1": 0, "a2": 0, "a3": 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                dicOfa["a1"] = i1
                dicOfa["a2"] = i2
                dicOfa["a3"] = i3
                ResList.append(abs(autocorrelation(varsNum, dicOfa, truthTable, dicIndexList)))
    correlationRes = 0
    for i in range(1, len(ResList)):
        correlationRes = ResList[i] + correlationRes
    tmp = 1 /(pow(2, varsNum) * (pow(2, varsNum) - 1))
    res = 1 - tmp * correlationRes
    # print(res)
    return res

'''
    四元透明阶的计算
    :return 返回计算结果
'''
def FourVarsTransparencyCompute(varsNum, truthTable, dicIndexList):

    ResList = []
    dicOfa = {"a1": 0, "a2": 0, "a3": 0, "a4" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    dicOfa["a1"] = i1
                    dicOfa["a2"] = i2
                    dicOfa["a3"] = i3
                    dicOfa["a4"] = i4
                    ResList.append(abs(autocorrelation(varsNum, dicOfa, truthTable, dicIndexList)))
    correlationRes = 0
    for i in range(1, len(ResList)):
        correlationRes = ResList[i] + correlationRes
    tmp = 1 /(pow(2, varsNum) * (pow(2, varsNum) - 1))
    res = 1 - tmp * correlationRes
    # print(res)
    return res

'''
    五元透明阶的计算
    :return 返回计算结果
'''
def FiveVarsTransparencyCompute(varsNum, truthTable, dicIndexList):

    ResList = []
    dicOfa = {"a1": 0, "a2": 0, "a3": 0, "a4" : 0, "a5" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        dicOfa["a1"] = i1
                        dicOfa["a2"] = i2
                        dicOfa["a3"] = i3
                        dicOfa["a4"] = i4
                        dicOfa["a5"] = i5
                        ResList.append(abs(autocorrelation(varsNum, dicOfa, truthTable, dicIndexList)))
    correlationRes = 0
    for i in range(1, len(ResList)):
        correlationRes = ResList[i] + correlationRes
    tmp = 1 /(pow(2, varsNum) * (pow(2, varsNum) - 1))
    res = 1 - tmp * correlationRes
    # print(res)
    return res

'''
    八元透明阶的计算
    :return 返回计算结果
'''
def EightVarsTransparencyCompute(varsNum, truthTable, dicIndexList):
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
                                    ResList.append(abs(autocorrelation(varsNum, dicOfa, truthTable, dicIndexList)))
    correlationRes = 0
    for i in range(1, len(ResList)):
        correlationRes = ResList[i] + correlationRes
    # print(correlationRes)
    tmp = 1 /(pow(2, varsNum) * (pow(2, varsNum) - 1))
    res = 1 - tmp * correlationRes
    # print(res)
    return res

def NineVarsTransparencyCompute(varsNum, truthTable, dicIndexList):
    ResList = []
    dicOfa = {"a1": 0, "a2": 0, "a3": 0, "a4" : 0, "a5" : 0, "a6" : 0, "a7" : 0, "a8" : 0, "a9" : 0}
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
    # print(correlationRes)
    tmp = 1 /(pow(2, varsNum) * (pow(2, varsNum) - 1))
    res = 1 - tmp * correlationRes
    # print(res)
    return res


'''
    透明阶计算选择
    根据传入当前布尔函数元数，选择透明阶计算函数
'''
def transparencyCompute(varsNum, truthTable, dicIndexList):
    if varsNum == 4:
        return FourVarsTransparencyCompute(varsNum, truthTable, dicIndexList)
    if varsNum == 5:
        return FiveVarsTransparencyCompute(varsNum, truthTable, dicIndexList)
    elif varsNum == 8:
        return EightVarsTransparencyCompute(varsNum, truthTable, dicIndexList)
    elif varsNum == 9:
        return NineVarsTransparencyCompute(varsNum, truthTable, dicIndexList)


if __name__ == '__main__':
    truthTable, dicIndexList = truthTableAndIndexLixt(5)
    FiveVarsTransparencyCompute(5, truthTable, dicIndexList)












