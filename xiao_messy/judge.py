
import copy
from S_Box_nonlinearity import hexToBinary
from walsh_and_nonlinearity import nonlinearityCompute
from transparency import transparencyCompute

'''
    判断长表的非线性度和透明阶
'''

def EightVars_AllTruthTable():
    resList = []
    dicValueOfx = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    dicValueOfx["x1"] = i1
                                    dicValueOfx["x2"] = i2
                                    dicValueOfx["x3"] = i3
                                    dicValueOfx["x4"] = i4
                                    dicValueOfx["x5"] = i5
                                    dicValueOfx["x6"] = i6
                                    dicValueOfx["x7"] = i7
                                    dicValueOfx["x8"] = i8
                                    resList.append(copy.deepcopy(list(dicValueOfx.values())))
    return resList

def NineVars_AllTruthTable():
    resList = []
    dicValueOfx = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0, 'x9' : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    for i9 in range(0, 2):
                                        dicValueOfx["x1"] = i1
                                        dicValueOfx["x2"] = i2
                                        dicValueOfx["x3"] = i3
                                        dicValueOfx["x4"] = i4
                                        dicValueOfx["x5"] = i5
                                        dicValueOfx["x6"] = i6
                                        dicValueOfx["x7"] = i7
                                        dicValueOfx["x8"] = i8
                                        dicValueOfx["x9"] = i9
                                        resList.append(copy.deepcopy(list(dicValueOfx.values())))
    return resList



def trans(varsNum, truthTable, AlltruthTable):
    print(truthTable)
    oneNumList = []
    for i in range(len(truthTable)):
        if truthTable[i] == 1:
            oneNumList.append(i)
    # print(oneNumList)
    # print(len(oneNumList))
    oneNumDic = {}
    for ele in oneNumList:
        oneNumDic[ele] = AlltruthTable[ele]

    resTmpList = []
    for k, ele in oneNumDic.items():
        resTmpList.append(ele)
    # print(resTmpList)

    Dic = {}
    List = []
    num = 0
    for ele in resTmpList:
        for elem in ele:
            Dic[num % varsNum] = elem
            num = num + 1
        List.append(copy.deepcopy(Dic))
    # print(List)
    return List





def functionTruthTable():
    TruthTableList1 = ["4 6 4 A B D 0 1 5 7 6 F 7 3 2 1 4 1 5 D E 0 6 2 B 3 D 7 7 B 2 1 "
                       "0 2 2 4 A E 7 B 3 5 D D 0 A 7 B A 8 7 8 2 A A 7 A 6 5 6 7 B 7 4"]

    TruthTableList2 = ["3 8 F 7 9 8 0 8 E 0 B 3 7 6 B 6 9 A 2 7 B D 6 C 4 D 0 A A C 4 B "
                       "E 5 E A 2 F 4 C E 9 D 0 1 A 8 3 1 2 9 0 3 6 E B E E C 3 0 3 B D"]

    '''
        九元函数
    '''
    nineTrutable = ["9 7 8 0 8 1 A E 7 E 1 6 3 7 A 9 9 1 F C E D 2 D 1 F C 5 8 C 7 D "
                    "8 2 E 8 F E 4 B 1 2 E 3 A 3 A 2 E 8 A F 4 E 6 6 8 4 4 A 2 A 0 C "
                    "8 0 E 2 E 9 7 E 5 1 B C 8 B D F F 8 "]
    tmpList = []
    for ele in TruthTableList1:
        tmpList = ele.split(" ")

    binaryListTmp = hexToBinary(tmpList)
    binaryList = []
    for ele in binaryListTmp:
        for elem in ele:
            binaryList.append(elem)
    # print(binaryList)
    return binaryList





if __name__ == '__main__':
    truthTable = functionTruthTable()
    alltruthTable = EightVars_AllTruthTable()
    indexDicList = trans(8, truthTable, alltruthTable)
    # print(indexDicList)
    # print(indexDicList)
    nonlinearity = nonlinearityCompute(8, truthTable)
    transparency = transparencyCompute(8, truthTable, indexDicList)
    #
    print(f"the nonlinearity = {nonlinearity}")
    print(f"the transparency = {transparency}")

