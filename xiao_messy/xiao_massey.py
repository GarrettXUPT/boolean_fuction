
from flieToLst import fileToList
from walsh_and_nonlinearity import walshCompute
from RSBF import initRSBF, finalOribit, TruthTableSelect, AllTruthTableSelect

def xiao_messay(varsNum, TruthTable, allTruthTable):
    oneNumStatic = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0}
    for ele in allTruthTable:
        num = ele.count(1)
        oneNumStatic[num] =  oneNumStatic[num] + 1

    walshVec = walshCompute(varsNum, TruthTable)
    zeroVec = []
    for i in range(len(walshVec)):
        if walshVec[i] == 0:
            zeroVec.append(i)
    truthTableVec = []
    for ele in zeroVec:
        truthTableVec.append(allTruthTable[ele].count(1))
    # print(oneNumStatic)
    # print(truthTableVec)
    oneNumStatic.pop(0)
    autoDeg = 0
    for k, v in oneNumStatic.items():
        if truthTableVec.count(k) == v:
            autoDeg = k
        else:
            break
    return autoDeg


def conclusion():
    varsNum = 8
    # lst = [6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 20, 22, 24, 25, 26, 32, 34]
    allTruthTable = AllTruthTableSelect(varsNum)
    oribit = finalOribit(varsNum)
    for i in range(1, 33):
        res = fileToList("116_" + str(16) + ".txt")
        for ele in res:
            dicIndexList = initRSBF(varsNum, ele[0], oribit)
            truthTable = TruthTableSelect(varsNum, dicIndexList)
            x = xiao_messay(varsNum, truthTable, allTruthTable)
            with open("relisent.txt", mode="a+", encoding="utf-8") as f:
                f.write(str(ele) + str(x) + "\n")
        print("check")

def unbalancedConclusion(varsNum, nonlinearity, address, oribit, allTruthTable):
    table = fileToList(address)
    for ele in table:
        dicIndexList = initRSBF(varsNum, ele[0], oribit)
        truthTable = TruthTableSelect(varsNum, dicIndexList)
        x = xiao_messay(varsNum, truthTable, allTruthTable)
        if x!= 0:
            with open("unbalanced" + str(nonlinearity) +  "_reslisent_" + str(x) + ".txt", mode="a+", encoding="utf-8") as f:
                f.write(str(ele) + "    " +str(x) + "\n")




if __name__ == '__main__':
    varsNum = 8
    allTruthTable = AllTruthTableSelect(varsNum)
    oribit = finalOribit(varsNum)

    nonlinearity = 117
    for i in range(1, 18):
        res = unbalancedConclusion(8, nonlinearity, "result/" + str(nonlinearity) + "_search" + str(i) + ".txt", oribit, allTruthTable)

    nonlinearity = 118
    for i in range(1, 18):
        res = unbalancedConclusion(8, nonlinearity, "result/" + str(nonlinearity) + "_search" + str(i) + ".txt", oribit, allTruthTable)

    nonlinearity = 119
    for i in range(1, 18):
        res = unbalancedConclusion(8, nonlinearity, "result/" + str(nonlinearity) + "_search" + str(i) + ".txt", oribit, allTruthTable)

    nonlinearity = 120
    for i in range(1, 14):
        res = unbalancedConclusion(8, nonlinearity, "result/" + str(nonlinearity) + "_search" + str(i) + ".txt", oribit, allTruthTable)


