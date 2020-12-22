import numpy as np
import time
from innerproduct import EightVars_innerProduct, strToList
'''
十六进制转化为二进制列表
return 转化结果
'''
def hexToBinary(hexList):
    ResList = []
    for ele in hexList:
        tmpEle = int(ele, base = 16)   # 将16进制转化为十进制
        binRes = str(bin(tmpEle))[2:]  # 将十进制转化为二进制
        binLen = len(binRes)  # 计算二进制表示的长度
        if binLen < 4:  # 若长度小于4，则补全
            binRes = '0' * (4 - binLen) + binRes
        tmpList = []
        for i in range(0, 4):
            tmpList.append(int(binRes[i]))
        ResList.extend(tmpList)
    return ResList


'''
    AES S盒真值表
    :return f0-->f7的真值表组成的列表
'''
def S_BOX_TRUTHTABLE(TRUTHTABLE):
    TRUTHTABLE1 = ["6 3", "7 C", "7 7", "7 B", "F 2", "6 B", "6 F", "C 5", "3 0", "0 1", "6 7", "2 B", "F E", "D 7", "A B", "7 6",
                  "C A", "8 2", "C 9", "7 D", "F A", "5 9", "4 7", "F 0", "A D", "D 4", "A 2", "A F", "9 C", "A 4", "7 2", "C 0",
                  "B 7", "F D", "9 3", "2 6", "3 6", "3 F", "F 7", "C C", "3 4", "A 5", "E 5", "F 1", "7 1", "D 8", "3 1", "1 5",
                  "0 4", "C 7", "2 3", "C 3", "1 8", "9 6", "0 5", "9 A", "0 7", "1 2", "8 0", "E 2", "E B", "2 7", "B 2", "7 5",
                  "0 9", "8 3", "2 C", "1 A", "1 B", "6 E", "5 A", "A 0", "5 2", "3 B", "D 6", "B 3", "2 9", "E 3", "2 F", "8 4",
                  "5 3", "D 1", "0 0", "E D", "2 0", "F C", "B 1", "5 B", "6 A", "C B", "B E", "3 9", "4 A", "4 C", "5 8", "C F",
                  "D 0", "E F", "A A", "F B", "4 3", "4 D", "3 3", "8 5", "4 5", "F 9", "0 2", "7 F", "5 0", "3 C", "9 F", "A 8",
                  "5 1", "A 3", "4 0", "8 F", "9 2", "9 D", "3 8", "F 5", "B C", "B 6", "D A", "2 1", "1 0", "F F", "F 3", "D 2",
                  "C D", "0 C", "1 3", "E C", "5 F", "9 7", "4 4", "1 7", "C 4", "A 7", "7 E", "3 D", "6 4", "5 D", "1 9", "7 3",
                  "6 0", "8 1", "4 F", "D C", "2 2", "2 A", "9 0", "8 8", "4 6", "E E", "B 8", "1 4", "D E", "5 E", "0 B", "D B",
                  "E 0", "3 2", "3 A", "0 A", "4 9", "0 6", "2 4", "5 C", "C 2", "D 3", "A C", "6 2", "9 1", "9 5", "E 4", "7 9",
                  "E 7", "C 8", "3 7", "6 D", "8 D", "D 5", "4 E", "A 9", "6 C", "5 6", "F 4", "E A", "6 5", "7 A", "A E", "0 8",
                  "B A", "7 8", "2 5", "2 E", "1 C", "A 6", "B 4", "C 6", "E 8", "D D", "7 4", "1 F", "4 B", "B D", "8 B", "8 A",
                  "7 0", "3 E", "B 5", "6 6", "4 8", "0 3", "F 6", "0 E", "6 1", "3 5", "5 7", "B 9", "8 6", "C 1", "1 D", "9 E",
                  "E 1", "F 8", "9 8", "1 1", "6 9", "D 9", "8 E", "9 4", "9 B", "1 E", "8 7", "E 9", "C E", "5 5", "2 8", "D F",
                  "8 C", "A 1", "8 9", "0 D", "B F", "E 6", "4 2", "6 8", "4 1", "9 9", "2 D", "0 F", "B 0", "5 4", "B B", "1 6"]
    hexTableList =[]
    for ele in TRUTHTABLE:
        hexTableList.append(ele.split(" "))

    binaryListTmp = []
    for ele in hexTableList:
        binaryListTmp.append(hexToBinary(ele))

    binaryList = []
    for ele in binaryListTmp:
        tmpList = []
        for elem in ele:
            for elebinary in elem:
                tmpList.append(int(elebinary))
        binaryList.append(tmpList)
    # print(binaryList[0])
    f0TruthTableList = []
    f1TruthTableList = []
    f2TruthTableList = []
    f3TruthTableList = []
    f4TruthTableList = []
    f5TruthTableList = []
    f6TruthTableList = []
    f7TruthTableList = []
    for ele in binaryList:
        f0TruthTableList.append(ele[7])
        f1TruthTableList.append(ele[6])
        f2TruthTableList.append(ele[5])
        f3TruthTableList.append(ele[4])
        f4TruthTableList.append(ele[3])
        f5TruthTableList.append(ele[2])
        f6TruthTableList.append(ele[1])
        f7TruthTableList.append(ele[0])
    resList = []
    resList.append(f0TruthTableList)
    resList.append(f1TruthTableList)
    resList.append(f2TruthTableList)
    resList.append(f3TruthTableList)
    resList.append(f4TruthTableList)
    resList.append(f5TruthTableList)
    resList.append(f6TruthTableList)
    resList.append(f7TruthTableList)
    return resList

'''
    八元乘积
    return:各个情况的乘积结果，共 2 ** (2 ** n) 个
'''
def S_BOX_EightVars_innerProduct():
    resList = EightVars_innerProduct()
    ResultList = []
    for i in range(pow(2, 8)):
        ResultList.append(resList[0 + i * 256: 256 + i * 256])
    return ResultList

'''
    数值之间的相乘
    :return:乘积的结果
'''
def multiply(x, w):
    return x * w

'''
    向量间的相乘
    :return:相乘结果向量
'''
def vectorMutiply(vec1, vec2):
    npRes = np.multiply(np.array(vec1), np.array(vec2))
    return npRes.tolist()

'''
    向量间的加法
    :return:加法计算结果向量
'''
def vectorAdd(vec1, vec2):
    npRes = np.add(np.array(vec1), np.array(vec2))
    return npRes.tolist()

'''
    S盒walsh谱所需的向量
    return:theta向量,共2**8种
'''
def thetaGenerate():
    thetaList = []
    dicValueOftheta = {"w1": 0, "w2": 0, "w3": 0, "w4": 0, "w5": 0, "w6": 0, "w7": 0, "w8": 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    dicValueOftheta["w1"] = i1
                                    dicValueOftheta["w2"] = i2
                                    dicValueOftheta["w3"] = i3
                                    dicValueOftheta["w4"] = i4
                                    dicValueOftheta["w5"] = i5
                                    dicValueOftheta["w6"] = i6
                                    dicValueOftheta["w7"] = i7
                                    dicValueOftheta["w8"] = i8
                                    thetaList.append(list(dicValueOftheta.values()))
    return thetaList

'''
    input:theta 由thetaGenerate产生的theta矩阵
    truthtableList 由AES转化而来的真值表矩阵
'''
def multiply_theta_truthTable(varsNum, theta, truthtableList):
    ResLst = []
    for i in range(pow(2, varsNum)):
        tmpList = []
        for ele in truthtableList:
            tmpList.append(ele[i])
        ResLst.append(vectorMutiply(theta, tmpList))
        # print(ResLst)
    return ResLst

'''
    walsh谱指数部分计算 theta * F + X * W
    :return:返回计算结果
'''
def indexCompute(multiply_theta_truthtable, innerproductRes):
    resList = []
    for inner in innerproductRes:
        tmpList = vectorAdd(inner, multiply_theta_truthtable)
        resList.append(tmpList)
    return resList

'''
    S盒Walsh谱计算
    :return walsh谱向量
'''
def S_Box_Walsh(varsNum, truthTableList, innerRes, thetaList):
    Mul_theta_and_F_ResList = []
    for theta in thetaList:
        Mul_theta_and_F_ResList.append(multiply_theta_truthTable(varsNum,theta, truthTableList))
    # print(Mul_theta_and_F_ResList)

    resList = []
    for ele in Mul_theta_and_F_ResList:
        tmpList = []
        for elem in ele:
            tmpList.append(sum(elem) % 2)
        resList.append(tmpList)


    indexAddList = []
    for mutiply_theta_truthTable in resList:
        indexAddList.append(indexCompute(mutiply_theta_truthTable, innerRes))
    # print(indexAddList)
    WalshTmp = []
    for ele in indexAddList:
        for elem in ele:
            for element in elem:
                if element % 2 == 0:
                    WalshTmp.append(1)
                elif element % 2 == 1:
                    WalshTmp.append(-1)
                else:
                    print("Error")

    WalshTmpList = []
    for i in range(len(WalshTmp) // pow(2, varsNum)):
        WalshTmpList.append(abs(sum(WalshTmp[0 + i * pow(2, varsNum) : pow(2, varsNum) + i * pow(2, varsNum)])))

    WalshVectorList = []
    for i in range(len(WalshTmpList) // pow(2, varsNum)):
        WalshVectorList.append(WalshTmpList[0 + i * pow(2, varsNum) : pow(2, varsNum) + i * pow(2, varsNum)])

    return  WalshVectorList

'''
    S盒非线性度的计算
    :print 打印S盒非线性度
'''
def S_BOX_nolinearityCompte(varsNum, WalshVectorList):
    WalshMaxValueList = []
    for ele in WalshVectorList:
        WalshMaxValueList.append(max(ele))
    WalshMax = max(WalshMaxValueList[1:])
    nolinearity = pow(2, varsNum - 1) - 0.5 * WalshMax
    print("AES_S_BOX_Nolinearity = ", nolinearity)

'''
    非线性度计算主程序
'''
def nonlinearity(varsNum, S_BOX_LIST):
    innerList = S_BOX_EightVars_innerProduct()
    truthTableList = S_BOX_TRUTHTABLE(S_BOX_LIST)
    thetaList = thetaGenerate()
    WalshVectorList = S_Box_Walsh(varsNum,truthTableList, innerList, thetaList)
    S_BOX_nolinearityCompte(varsNum, WalshVectorList)

if __name__ == '__main__':
    start = time.time()
    # TRUTHTABLE = new_S_BOX(random_gen(0.1, 0.00011))
    # nonlinearity(8, TRUTHTABLE)
    end = time.time()
    print(end - start)




