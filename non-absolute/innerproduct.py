

'''
    将由文件读取的字符串转化为原来的列表形式
'''
def strToList(str):
    resList = []
    for ele in str:
        if ele.isdigit():
            resList.append(int(ele))
    return resList


'''
    三元点积结果的全表2**（2 * varsNum)长
'''
def ThreeVars_innerProduct():
    resList = []
    dicValueOfw = {"w1" : 0, "w2" : 0, "w3" : 0}
    dicValueOfx = {"x1" : 0, "x2" : 0, "x3" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
               dicValueOfw["w1"] = i1
               dicValueOfw["w2"] = i2
               dicValueOfw["w3"] = i3
               for j1 in range(0, 2):
                   for j2 in range(0, 2):
                       for j3 in range(0, 2):
                           dicValueOfx["x1"] = j1
                           dicValueOfx["x2"] = j2
                           dicValueOfx["x3"] = j3
                           resTmpList = []
                           resTmpList.append(multiply(dicValueOfx["x1"], dicValueOfw["w1"]))
                           resTmpList.append(multiply(dicValueOfx["x2"], dicValueOfw["w2"]))
                           resTmpList.append(multiply(dicValueOfx["x3"], dicValueOfw["w3"]))
                           resList.append(sum(resTmpList))
    return resList

'''
    四元点积结果的全表2**（2 * varsNum)长
'''
def FourVars_innerProduct():
    resList = []
    dicValueOfw = {"w1" : 0, "w2" : 0, "w3" : 0, "w4" : 0}
    dicValueOfx = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                   dicValueOfw["w1"] = i1
                   dicValueOfw["w2"] = i2
                   dicValueOfw["w3"] = i3
                   dicValueOfw["w4"] = i4
                   for j1 in range(0, 2):
                       for j2 in range(0, 2):
                           for j3 in range(0, 2):
                               for j4 in range(0, 2):
                                   dicValueOfx["x1"] = j1
                                   dicValueOfx["x2"] = j2
                                   dicValueOfx["x3"] = j3
                                   dicValueOfx["x4"] = j4
                                   resTmpList = []
                                   resTmpList.append(multiply(dicValueOfx["x1"], dicValueOfw["w1"]))
                                   resTmpList.append(multiply(dicValueOfx["x2"], dicValueOfw["w2"]))
                                   resTmpList.append(multiply(dicValueOfx["x3"], dicValueOfw["w3"]))
                                   resTmpList.append(multiply(dicValueOfx["x4"], dicValueOfw["w4"]))
                                   resList.append(sum(resTmpList))
    return resList

'''
    五元点积结果的全表2**（2 * varsNum)长
'''
def FiveVars_innerProduct():
    resList = []
    dicValueOfw = {"w1" : 0, "w2" : 0, "w3" : 0, "w4" : 0, "w5" : 0}
    dicValueOfx = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                       dicValueOfw["w1"] = i1
                       dicValueOfw["w2"] = i2
                       dicValueOfw["w3"] = i3
                       dicValueOfw["w4"] = i4
                       dicValueOfw["w5"] = i5
                       for j1 in range(0, 2):
                           for j2 in range(0, 2):
                               for j3 in range(0, 2):
                                   for j4 in range(0, 2):
                                       for j5 in range(0, 2):
                                           dicValueOfx["x1"] = j1
                                           dicValueOfx["x2"] = j2
                                           dicValueOfx["x3"] = j3
                                           dicValueOfx["x4"] = j4
                                           dicValueOfx["x5"] = j5
                                           resTmpList = []
                                           resTmpList.append(multiply(dicValueOfx["x1"], dicValueOfw["w1"]))
                                           resTmpList.append(multiply(dicValueOfx["x2"], dicValueOfw["w2"]))
                                           resTmpList.append(multiply(dicValueOfx["x3"], dicValueOfw["w3"]))
                                           resTmpList.append(multiply(dicValueOfx["x4"], dicValueOfw["w4"]))
                                           resTmpList.append(multiply(dicValueOfx["x5"], dicValueOfw["w5"]))
                                           resList.append(sum(resTmpList))
    return resList

'''
    八元点积结果的全表2**（2 * varsNum)长
'''
def EightVars_innerProduct():
    resList = []
    with open("eight_vars_innerproduct.txt", mode="r+", encoding="utf-8") as f:
        line = f.read()
        resList = strToList(line)
    return resList

'''
    八元点积结果的全表2**（2 * varsNum)长
'''
def NineVars_innerProduct():
    resList = []
    with open("nine_vars_innerproduct.txt", mode = "r", encoding = "utf-8") as f:
        line =  f.read()
        resList = strToList(line)
    return resList

'''
    单纯的乘积
'''
def multiply(x, w):
    return x * w

'''
    选择根据元数选择使用的点积运算
'''
def innerProductSelect(varsNum):
    if varsNum == 3:
        return ThreeVars_innerProduct()
    elif varsNum == 4:
        return FourVars_innerProduct()
    elif varsNum == 5:
        return FiveVars_innerProduct()
    elif varsNum == 8:
        return EightVars_innerProduct()
    elif varsNum == 9:
        return NineVars_innerProduct()

if __name__ == '__main__':
    resList = EightVars_innerProduct()
    print(resList.__len__())
    print(type(resList))
    print(resList)





