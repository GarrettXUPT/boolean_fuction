
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


if __name__ == '__main__':
    varsNum = 8
    # # lst = [6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 20, 22, 24, 25, 26, 32, 34]
    allTruthTable = AllTruthTableSelect(varsNum)

    RSST = [3.0, 10.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 21.0, 24.0, 25.0, 26.0, 27.0, 30.0, 34.0]
    # tmp = (sorted(RSST))
    # print(tmp)
    oribit = finalOribit(varsNum)
    dicIndexList = initRSBF(varsNum, RSST, oribit)
    truthTable = TruthTableSelect(varsNum, dicIndexList)
    print(truthTable)
    print(xiao_messay(varsNum, truthTable, allTruthTable))

