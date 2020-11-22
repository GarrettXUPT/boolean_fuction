import copy

def ThreeVars_truthTable(dicIndexList):
    resList = []
    hang = int(input("请输入行数："))
    for i in range(0, hang):
        indexStr = input(f"请输入第{i + 1}行：")
        indexlist = list(indexStr.split(" "))
        dic_index = {"x1": int(indexlist[0]), "x2": int(indexlist[1]), "x3": int(indexlist[2])}
        dicIndexList.append(dic_index)

    dic_value = {"x1": 0, "x2": 0, "x3": 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                dic_value["x1"] = i1
                dic_value["x2"] = i2
                dic_value["x3"] = i3
                resTmpList = []
                for i in range(0, hang):
                    resTmpList.append(itemRes(dicIndexList[i], dic_value))
                resList.append(sum(resTmpList) % 2)
    return resList

def FourVars_truthTable(dicIndexList):

    resList = []
    hang = int(input("请输入行数："))
    for i in range(0, hang):
        indexStr = input(f"请输入第{i + 1}行：")
        indexlist = list(indexStr.split(" "))
        dic_index = {"x1": int(indexlist[0]), "x2": int(indexlist[1]), "x3": int(indexlist[2]), "x4" : int(indexlist[3])}
        dicIndexList.append(dic_index)

    print(dicIndexList)
    dic_value = {"x1": 0, "x2": 0, "x3": 0, "x4" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    dic_value["x1"] = i1
                    dic_value["x2"] = i2
                    dic_value["x3"] = i3
                    dic_value["x4"] = i4
                    resTmpList = []
                    for i in range(0, hang):
                        resTmpList.append(itemRes(dicIndexList[i], dic_value))
                    resList.append(sum(resTmpList) % 2)
    return resList

def FiveVars_truthTable(dicIndexList):
    resList = []
    hang = int(input("请输入行数："))
    for i in range(0, hang):
        indexStr = input(f"请输入第{i + 1}行：")
        indexlist = list(indexStr.split(" "))
        dic_index = {"x1": int(indexlist[0]), "x2": int(indexlist[1]), "x3": int(indexlist[2]), "x4": int(indexlist[3]), "x5" : int(indexlist[4])}
        dicIndexList.append(dic_index)

    dic_value = {"x1": 0, "x2": 0, "x3": 0, "x4": 0, "x5" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        dic_value["x1"] = i1
                        dic_value["x2"] = i2
                        dic_value["x3"] = i3
                        dic_value["x4"] = i4
                        dic_value["x5"] = i5
                        resTmpList = []
                        for i in range(0, hang):
                            resTmpList.append(itemRes(dicIndexList[i], dic_value))
                        resList.append(sum(resTmpList) % 2)
    return resList


def EightVars_truthTable(dicIndexList):
    resList = []
    hang = int(input("请输入行数："))
    for i in range(0, hang):
        indexStr = input(f"请输入第{i + 1}行：")
        indexlist = list(indexStr.split(" "))
        dic_index = {"x1": int(indexlist[0]), "x2": int(indexlist[1]), "x3": int(indexlist[2]), "x4": int(indexlist[3]), "x5" : int(indexlist[4]), "x6" : int(indexlist[5]), "x7" : int(indexlist[6]), "x8" : int(indexlist[7])}
        dicIndexList.append(dic_index)

    dic_value = {"x1": 0, "x2": 0, "x3": 0, "x4": 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    dic_value["x1"] = i1
                                    dic_value["x2"] = i2
                                    dic_value["x3"] = i3
                                    dic_value["x4"] = i4
                                    dic_value["x5"] = i5
                                    dic_value["x6"] = i6
                                    dic_value["x7"] = i7
                                    dic_value["x8"] = i8
                                    resTmpList = []
                                    for i in range(0, hang):
                                        resTmpList.append(itemRes(dicIndexList[i], dic_value))
                                    resList.append(sum(resTmpList) % 2)
    return resList

def NineVars_truthTable(dicIndexList):
    resList = []
    hang = int(input("请输入行数："))
    for i in range(0, hang):
        indexStr = input(f"请输入第{i + 1}行：")
        indexlist = list(indexStr.split(" "))
        dic_index = {"x1": int(indexlist[0]), "x2": int(indexlist[1]), "x3": int(indexlist[2]), "x4": int(indexlist[3]),
                     "x5" : int(indexlist[4]), "x6" : int(indexlist[5]), "x7" : int(indexlist[6]), "x8" : int(indexlist[7]), "x9" : int(indexlist[8])}
        dicIndexList.append(dic_index)

    dic_value = {"x1": 0, "x2": 0, "x3": 0, "x4": 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0, "x9" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    for i9 in range(0, 2):
                                        dic_value["x1"] = i1
                                        dic_value["x2"] = i2
                                        dic_value["x3"] = i3
                                        dic_value["x4"] = i4
                                        dic_value["x5"] = i5
                                        dic_value["x6"] = i6
                                        dic_value["x7"] = i7
                                        dic_value["x8"] = i8
                                        dic_value["x9"] = i9
                                        resTmpList = []
                                        for i in range(0, hang):
                                            resTmpList.append(itemRes(dicIndexList[i], dic_value))
                                        resList.append(sum(resTmpList) % 2)
    return resList

def TenVars_truthTable(dicIndexList):
    resList = []
    hang = int(input("请输入行数："))
    for i in range(0, hang):
        indexStr = input(f"请输入第{i + 1}行：")
        indexlist = list(indexStr.split(" "))
        dic_index = {"x1": int(indexlist[0]), "x2": int(indexlist[1]), "x3": int(indexlist[2]), "x4": int(indexlist[3]),
                     "x5" : int(indexlist[4]), "x6" : int(indexlist[5]), "x7" : int(indexlist[6]), "x8" : int(indexlist[7]), "x9" : int(indexlist[8]), "x10" : int(indexlist[9])}
        dicIndexList.append(dic_index)

    dic_value = {"x1": 0, "x2": 0, "x3": 0, "x4": 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0, "x9" : 0, "10" : 0}
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
                                            dic_value["x1"] = i1
                                            dic_value["x2"] = i2
                                            dic_value["x3"] = i3
                                            dic_value["x4"] = i4
                                            dic_value["x5"] = i5
                                            dic_value["x6"] = i6
                                            dic_value["x7"] = i7
                                            dic_value["x8"] = i8
                                            dic_value["x9"] = i9
                                            dic_value["x10"] = i10
                                            resTmpList = []
                                            for i in range(0, hang):
                                                resTmpList.append(itemRes(dicIndexList[i], dic_value))
                                            resList.append(sum(resTmpList) % 2)
    return resList





def itemRes(dic_index, dic_value):
        for key in dic_value.keys():
            if dic_value.get(key) != dic_index.get(key):
                return 0
        return 1

def truthTableSelect(varsNum, dicIndexList):
    if varsNum == 3:
        return ThreeVars_truthTable(dicIndexList)
    elif varsNum == 4:
        return FourVars_truthTable(dicIndexList)
    elif varsNum == 5:
        return FiveVars_truthTable(dicIndexList)
    elif varsNum == 8:
        return EightVars_truthTable(dicIndexList)
    elif varsNum == 9:
        return NineVars_truthTable(dicIndexList)
    elif varsNum == 10:
        return TenVars_truthTable(dicIndexList)


def AlltruTable(varsNum):
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


def tableList():
    return [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0]

if __name__ == '__main__':
    # dicIndexList = []
    # resList = NineVars_truthTable(dicIndexList)
    # print(resList)
    res = AlltruTable(9)
    print(len(res))
    print(res[1])
    print(res[-1])










