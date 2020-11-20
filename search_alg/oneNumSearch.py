import numpy as np
from judge import functionTruthTable, EightVars_AllTruthTable, trans
from walsh_and_nonlinearity import nonlinearityCompute
from transparency import transparencyCompute, truthTableAndIndexLixt


def flipTruthTable(oneNumdic, zeroNumdic, randList):
    # print(oneNumdic)
    # print(zeroNumdic)
    oneTmpDic = {}
    zeroTmpDic = {}
    for ele in randList:
        if ele in oneNumdic:
            zeroTmpDic[ele] = oneNumdic[ele]
            oneNumdic.pop(ele)

        if ele in zeroNumdic:
            oneTmpDic[ele] = zeroNumdic[ele]
            zeroNumdic.pop(ele)

    oneNumdic.update(oneTmpDic)
    zeroNumdic.update(zeroTmpDic)
    # print(oneNumdic)
    return oneNumdic.values(), zeroNumdic.values()

def reformTruthtable(varsNum, NumList):
    truthtableList = [0 for i in range(pow(2, varsNum))]
    for ele in NumList[0]:
        truthtableList[ele] = 1
    return truthtableList


def classifier(varsNum, truthTable):
    count = -1
    oneNumList = []
    zeroNumList = []
    for ele in truthTable:
        count = count + 1
        if ele == 1:
            oneNumList.append(count)
        elif ele == 0:
            zeroNumList.append(count)
        else:
            print("fail")

    oneNumdic = {}
    oneNumcount = 0
    for ele in oneNumList:
        oneNumdic[oneNumcount] = ele
        oneNumcount = oneNumcount + 1
    # print(oneNumdic)

    zeroNumdic = {}
    zeroNumcount = 0
    for ele in zeroNumList:
        zeroNumdic[zeroNumcount] = ele
        zeroNumcount = zeroNumcount + 1
    # print(zeroNumdic)

    randList = np.random.randint(0, 128, 64)

    one_zero_list = flipTruthTable(oneNumdic, zeroNumdic, randList)

    newTruthTable = reformTruthtable(varsNum, one_zero_list)

    alltruthTable = EightVars_AllTruthTable()
    indexDicList = trans(8, newTruthTable, alltruthTable)

    nonlinearity = nonlinearityCompute(varsNum, newTruthTable)
    transparency = transparencyCompute(varsNum, newTruthTable, indexDicList)
    if nonlinearity > 110:
        print(f"the nonlinearity = {nonlinearity}")
        print(f"the transparency = {transparency}")
    return newTruthTable

if __name__ == '__main__':
    newTruthtable = functionTruthTable()
    while 1:
        newTruthtable = classifier(8, newTruthtable)




