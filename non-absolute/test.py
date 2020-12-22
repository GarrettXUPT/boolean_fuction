
import time
from RSBF import finalOribit, initRSBF, TruthTableSelect
from walsh_and_nonlinearity import nonlinearityCompute
from transparency import transparencyCompute
from multiprocessing import Process

def numCheck(endlen):
    endPos = 0
    beginPos = 0
    for processSort in range(0, endlen):
        beginPos = pow(2, 26) + processSort * pow(2, 25)
        endPos = pow(2, 26) + (processSort + 1) * pow(2, 25)
    print(beginPos)
    print(endPos)


'''
    将[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]形式转化为[35, 36]
    input:布尔型短表取值list
    return:十进制形式短表列表
'''
def oneNumToOribit(oneNum):
    OribitList = []
    for i in range(len(oneNum)) :
        if oneNum[i] == 0:
            continue
        else:
            OribitList.append(i + 1)
    return OribitList

'''
    由[35, 36]判断该旋转对称布尔函数是否平衡
'''
def isBalanced(varsNum, oribitList, allOribit):
    count = 0
    for ele in oribitList:
        count += len(allOribit[ele - 1])
    if count == pow(2, varsNum - 1):
        return True
    else:
        return False


def possibleTable(varsNum, beginPos, endPos):
    start = time.time()
    count = 0
    allOribit = finalOribit(varsNum)

    for i in range(beginPos, endPos):
        tmp = str(bin(i)).split("0b")
        for elem in tmp:
            if elem == '':
                continue
            tmpList = []
            for element in elem:
                tmpList.append(int(element))

            if len(tmpList) != 36:
                for i in range(36 - len(tmpList)):
                    tmpList.insert(0, 0)

            oribitLocList = oneNumToOribit(tmpList)
            # print(oribitLocList)
            balancedFlag = isBalanced(varsNum, oribitLocList, allOribit)

            if balancedFlag == True:
                break

            indexList = initRSBF(varsNum, oribitLocList, allOribit)
            truthTable = TruthTableSelect(varsNum, indexList)
            nonlinearity = nonlinearityCompute(varsNum, truthTable)
            # print(nonlinearity)
            if nonlinearity == 116:
                transparency = transparencyCompute(varsNum, truthTable, indexList)
                with open("result/116_search" + str(endPos) + ".txt", mode="a+", encoding="utf-8") as f:
                    f.write(str(oribitLocList) + " " + str(nonlinearity) + " " + str(transparency) + "\n")
            elif nonlinearity == 117:
                transparency = transparencyCompute(varsNum, truthTable, indexList)
                with open("result/117_search" + str(endPos) + ".txt", mode="a+", encoding="utf-8") as f:
                    f.write(str(oribitLocList) + " " + str(nonlinearity) + " " + str(transparency) + "\n")
            elif nonlinearity == 118:
                transparency = transparencyCompute(varsNum, truthTable, indexList)
                with open("result/118_search" + str(endPos) + ".txt", mode="a+", encoding="utf-8") as f:
                    f.write(str(oribitLocList) + " " + str(nonlinearity) + " " + str(transparency) + "\n")
            elif nonlinearity == 119:
                transparency = transparencyCompute(varsNum, truthTable, indexList)
                with open("result/119_search" + str(endPos) + ".txt", mode="a+", encoding="utf-8") as f:
                    f.write(str(oribitLocList) + " " + str(nonlinearity) + " " + str(transparency) + "\n")
            elif nonlinearity == 120:
                transparency = transparencyCompute(varsNum, truthTable, indexList)
                with open("result/120_search" + str(endPos) + ".txt", mode="a+", encoding="utf-8") as f:
                    f.write(str(oribitLocList) + " " + str(nonlinearity) + " " + str(transparency) + "\n")

        count += 1
        if count % 1000000 == 0:
            print(str(beginPos) + "->" + str(endPos) + "check ", count)
    end = time.time()

    print(str(beginPos) + "->" + str(endPos)  + "during time1 is ", end - start)
    print(count)



def ergodic(varsNum, begin, processSort, step):
    beginPos = pow(2, begin) + processSort * pow(2, step)
    endPos = pow(2, begin) + (processSort + 1) * pow(2, step)
    possibleTable(varsNum, beginPos, endPos)


def multiProcessGeneration(varsNum, begin, end, step):
    endLen = pow(2, end)
    processNum = (endLen - pow(2, begin)) // pow(2, step)
    print("processNum = ", processNum)
    for i in range(0, processNum):
        p1 = Process(target = ergodic, args = (varsNum, begin, i, step, ))
        p1.start()

if __name__ == '__main__':
    multiProcessGeneration(8, 0, 36, 31)










