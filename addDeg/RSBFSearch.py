
import copy
from RSBF import finalOribit, initRSBF, randomFlapTruthTable, TruthTableSelect, costFunction1, costFunction2, nonlinearityAndTransparency
from walsh_and_nonlinearity import nonlinearityCompute
from transparency import transparencyCompute

'''
    return:
        Dic序号与损失值的键值对       0: 0.9324142156862745, 1: 21460643212, 
        functionTruthTableList：取值为1的多项式的项   {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1}
'''
def oneStap(varsNum, oneNumList, nonlinearityBound, CostMin):

    functionTruthTableList = []     # 函数真值表列表
    Dict_ADJcost = {}               # 轨道数i和cost的键值对
    # 获取varsNum元布尔函数的轨道真值表列表(全表)
    OribitList = finalOribit(varsNum)
    # 当前真值表情况下，所有翻转情况的oneNumList
    oneNumResList = randomFlapTruthTable(oneNumList, OribitList)
    for i in range(len(oneNumResList)):
        # 将轨道式短表转换为索引形式
        indexList = initRSBF(varsNum, oneNumResList[i], OribitList)
        # 将索引形式的表转化为长输出真值表
        truthTable = TruthTableSelect(varsNum, indexList)
        # 判断是否为平衡的旋转对称布尔函数
        # if truthTable.count(1) != pow(2, varsNum - 1):
        #     continue
        # print("have a balanced function")
        functionTruthTableList.append(list(indexList))

        nolinearity = nonlinearityCompute(varsNum, truthTable)
        print(nolinearity)
        if nolinearity > nonlinearityBound:
            cost = costFunction2(varsNum, truthTable, indexList)
        else:
            cost = costFunction1(varsNum, truthTable, indexList)
        Dict_ADJcost[i] = cost

        if float(cost) < float(CostMin):
            CostMin = cost
    return Dict_ADJcost, functionTruthTableList

'''
    对字典的value进行排序
    :return value排序后的value列表
'''
def DictSorted(Dic):
    tmpList1 = []
    for ele in Dic.values():
        for elem in ele:
            tmpList1.append(list(elem.values()))
    return sorted(tmpList1)


def twoStep(varsNum, Dict_ADJcost, functionTruthTableList, F_MIN):
    index_TruthTable = {}
    i = 0
    for ele in Dict_ADJcost.keys():
        index_TruthTable[ele] = functionTruthTableList[i]
        i += 1

    # 对字典依照value值进行排序
    DictSortList = sorted(Dict_ADJcost.items(), key=lambda x : x[1], reverse = True)

    DictSortListLen = len(DictSortList)

    if DictSortListLen > 1:
        for i in range(DictSortListLen):
            indexList = index_TruthTable[DictSortList[DictSortListLen - i - 1][0]]
            tmpDic = {}
            tmpDic[DictSortList[DictSortListLen - i - 1][1]] = indexList
            sortList1 = DictSorted(tmpDic)
            tmpDic[DictSortList[DictSortListLen - i - 1][1]] = sortList1
            if tmpDic not in F_MIN:
                dicTmp = {}
                dicTmp[DictSortList[DictSortListLen - i - 1][1]] = indexList
                sortList2 = DictSorted(dicTmp)
                dicTmp[DictSortList[DictSortListLen - i - 1][1]] = sortList2
                # print(dicTmp)
                F_MIN.append(dicTmp)
                break
    else:
        indexList = functionTruthTableList[0]
        tmpDic = {}
        tmpDic[0] = indexList
        sortList1 = DictSorted(tmpDic)
        tmpDic[DictSortList[0]] = sortList1


        if tmpDic not in F_MIN:
            dicTmp = {}
            dicTmp[DictSortList[0][1]] = indexList
            sortList2 = DictSorted(dicTmp)
            dicTmp[DictSortList[0][1]] = sortList2
            F_MIN.append(dicTmp)


    tmpList = []
    for ele in list(F_MIN[-1].values()):
        for elem in ele:
            tmpList.append(elem)

    if len(tmpList) == pow(2, varsNum - 1):
        info = "balanced boolean function"
    else:
        info = "unbalanced boolean function"


    oneNumList = []
    allOribit = finalOribit(varsNum)
    for ele in tmpList:
        for i in range(len(allOribit)):
            if ele in allOribit[i]:
                oneNumList.append(i + 1)


    dicIndexList = initRSBF(varsNum, list(set(oneNumList)), allOribit)

    truthTable = TruthTableSelect(varsNum, dicIndexList)

    res1 = nonlinearityCompute(varsNum, truthTable)
    if res1 < 980:
        print("no write")
    if res1 >= 980:
        res2 = transparencyCompute(varsNum, truthTable, dicIndexList)
        with open("search_result/nobalanced_nonlinearity_" + str(res1) + "_resFile.txt", mode = "a", encoding= "utf-8") as f:
            f.write(str(list(set(oneNumList))) + "  nonlinearity = " + str(res1) + "  transparency = " + str(res2)  + " " + str(info) + "\n")

    return list(set(oneNumList))


if __name__ == '__main__':
    oneNumList = [1, 2, 3, 5, 10, 11, 12, 13, 14, 16, 17, 18, 20, 21, 28, 31, 33, 34, 35, 36, 38, 42, 43, 44, 46, 47, 48, 54, 56, 59]
    F_MIN = []
    iter = 0
    varsNum = 11
    nolinearityBound = 230
    costMin = 1

    while iter <= 5000:
        # print(oneNumList)
        Dict_ADJcost, functionTruthTableList = oneStap(varsNum, oneNumList, nolinearityBound, costMin)
        print(functionTruthTableList[0])
        print(functionTruthTableList[1])
        if len(functionTruthTableList) == 0:
            continue
        oneNumList = twoStep(varsNum, Dict_ADJcost, functionTruthTableList, F_MIN)
        iter = iter + 1


