
from truthTable import truthTableSelect
from innerproduct import innerProductSelect
import copy
'''
    布尔函数walsh谱的计算
    :return walsh谱向量
'''
def walshCompute(varsNum, truthTable):
    # print(truthTable)
    innerProductRes = innerProductSelect(varsNum)
    walshTmpResList = []
    tmpList = []
    walshResList = []
    for i in range(len(innerProductRes)):
        tmpList.append((truthTable[i % len(truthTable)] + innerProductRes[i]) % 2)
    # print(tmpList)
    for i in range(len(tmpList)):
            if tmpList[i] == 0:
               walshTmpResList.append(1)
            else:
                walshTmpResList.append(-1)

    for i in range(len(truthTable)):
        tmpRes = 0
        for j in range(len(truthTable)):
            tmpRes = walshTmpResList[j + i * len(truthTable)] + tmpRes
        walshResList.append(tmpRes)

    # testResList = []
    # for ele in walshResList:
    #     testResList.append(copy.deepcopy(ele ** 2))
    #
    # testResList2 = []
    # for ele in testResList:
    #     testResList2.append(copy.deepcopy(pow(ele - pow(2, varsNum), 3)))
    #
    # testRes = 0
    # for ele in testResList2:
    #     testRes = ele + testRes
    # print(testRes)
    # print(walshResList)
    return walshResList

'''
    布尔函数非线性度的计算
    :return 布尔函数非线性度的值
'''
def nonlinearityCompute(varsNum, truthTable):
    tmpList = []
    for ele in walshCompute(varsNum, truthTable):
        tmpList.append(abs(ele))
    # print(tmpList)
    return pow(2, varsNum - 1) - 0.5 * max(tmpList)



if __name__ == '__main__':
    dicIndexList = []
    truthTable = truthTableSelect(3, dicIndexList)
    res = nonlinearityCompute(3, truthTable)
    print(f"nonlinearity = {res}")

