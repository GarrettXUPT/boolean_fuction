
from initList import conditionList
import time, os, copy
from multiprocessing import Process, Pool
from innerproduct import innerProductSelect
from walsh_and_nonlinearity import nonlinearityCompute
from transparency import transparencyCompute
from RSBF import initRSBF, TruthTableSelect, finalOribit, nonlinearityAndTransparency

'''
    指定位置翻转一位
'''
def flapOneBit(pos, binaryList):
    lst= []
    for i in range(len(binaryList)):
        if i == pos:
            if binaryList[pos] == 1:
                lst.append(0)
            else:
                lst.append(1)
        else:
            lst.append(binaryList[i])
    return lst

'''
    二进制表转化为短表
'''
def binaryToShort(binaryList):
    resList = []
    for i in range(len(binaryList)):
        if binaryList[i] == 1:
            resList.append(i + 1)
    return resList

'''
    短表转化为二进制表
'''
def shortTobinary(shortList):
    binaryList = []
    for i in range(60):
        if i + 1 in shortList:
            binaryList.append(1)
        else:
            binaryList.append(0)
    return binaryList


'''
    轨道翻转，60个轨道翻转2个轨道，共1773种
'''
def updateOribit(short_lst):
    binaryList = shortTobinary(short_lst)
    # print(binaryList)
    FlapList = []
    for i in range(len(binaryList)):
        if i == len(binaryList) - 1:
            break
        tmpList =  flapOneBit(i, binaryList)
        board = len(binaryList) - i - 1
        if board == 0:
            break
        for j in range(board):
            tmpLst = flapOneBit(i + j + 1, tmpList)
            FlapList.append(copy.deepcopy(tmpLst))
    resList = []
    for ele in FlapList:
        resList.append(copy.deepcopy(binaryToShort(ele)))
    return resList


'''
    轨道翻转，60个轨道翻转3个轨道，共34220种
'''
def updateOribitThreePos(short_lst):
    binaryList = shortTobinary(short_lst)
    # print(binaryList)
    FlapList = []
    for i in range(len(binaryList)):
        if i == len(binaryList) - 1:
            break
        tmpList =  flapOneBit(i, binaryList)
        board = len(binaryList) - i - 1
        if board == 0:
            break
        for j in range(board):
            tmpLst = flapOneBit(i + j + 1, tmpList)
            lengths = len(binaryList) - i - j - 2
            if lengths == 0:
                break
            for k in range(lengths):
                tmplst = flapOneBit(i + j + k + 2, tmpLst)
                FlapList.append(copy.deepcopy(tmplst))

    resList = []
    for ele in FlapList:
        resList.append(copy.deepcopy(binaryToShort(ele)))
    print(len(resList))
    return resList


'''
    初始化损失值字典
'''
def initCostDic(varsNum):
    costDic = {}
    if varsNum == 9:
        for i in range(234, 243):
            costDic[i] = varsNum
    elif varsNum == 10:
        for i in range(484, 493):
            costDic[i] = varsNum
    elif varsNum == 11:
        for i in range(980, 993):
            costDic[i] = varsNum
    return costDic


'''
    损失函数
'''
def costFunction(varsNum, truthTable, indexList, nonlinearity):
    return -(nonlinearity / 241) + transparencyCompute(varsNum, truthTable, indexList)

'''
    评价函数
'''
def evalate(varsNum, costDicList, tableDic, innerProduct):
    for i in range(10):
        oneNumTable = tableDic[list(costDicList[i])[0]]
        nonlinearity, transparency = nonlinearityAndTransparency(varsNum, oneNumTable, innerProduct)
        with open("resultTable.txt", mode = "a+", encoding = "utf-8") as f:
            f.write(str(oneNumTable) + "        "  + "nonliearity = " +  str(nonlinearity) + "  transparency = " + str(transparency) + "\n")
        print("nonlinearity = " + str(nonlinearity), "  transparency = " + str(transparency))
        with open("resultTable.txt", mode=  "a+", encoding = "utf-8") as f:
            f.write("********************************************************" + "\n" + "\n")

def countInit(varsNum):
    if varsNum == 9:
        return 4
    elif varsNum == 10:
        return 5
    elif varsNum == 11:
        return 8

'''
    记录函数
'''
def record(varsNum, costDicList, tableDic, innerProduct, oribitList):
    recordNoteList = []
    Count = 0
    with open("resultTable4.txt", mode="a+", encoding="utf-8") as f:
        f.write("********************************************************" + "\n")
    for i in range(len(costDicList)):
        oneNumTable = tableDic[list(costDicList[i])[0]]
        nonlinearity, transparency, balancedFlag = nonlinearityAndTransparency(varsNum, oneNumTable, innerProduct, oribitList)
        if (nonlinearity in recordNoteList) and (nonlinearity != 234):
            continue
        if Count == countInit(varsNum):
            break
        Count += 1
        recordNoteList.append(copy.deepcopy(nonlinearity))
        with open("resultTable4.txt", mode="a+", encoding="utf-8") as f:
            f.write(str(oneNumTable) + "        " + "nonliearity = " + str(nonlinearity) + "  transparency = " + str(transparency) + "   " + balancedFlag + "\n")
    with open("resultTable4.txt", mode="a+", encoding="utf-8") as f:
        f.write("********************************************************" + "\n\n\n")


'''
    损失值统计并对好的结果进行记录
'''
def costStatisticAndRecord(varsNum, costDic, costDicList, tableDic, innerProduct, oribitList):
    recordNoteList = []
    Count = 0
    with open("resultTable.txt", mode="a+", encoding="utf-8") as f:
        f.write("********************************************************" + "\n")
    for i in range(len(costDicList)):
        oneNumTable = tableDic[list(costDicList[i])[0]]
        nonlinearity, transparency, balancedFlag = nonlinearityAndTransparency(varsNum, oneNumTable, innerProduct, oribitList)
        if (nonlinearity in recordNoteList) and (nonlinearity != 234):
            continue
        if Count == countInit(varsNum):
            break
        Count += 1
        recordNoteList.append(copy.deepcopy(nonlinearity))
        currentCost = int(costDicList[i][1])
        if currentCost < costDic[nonlinearity]:
            costDic[nonlinearity] = currentCost
            with open("resultTable.txt", mode="a+", encoding="utf-8") as f:
                f.write(str(oneNumTable) + "      " + "nonliearity = " + str(nonlinearity) + "  transparency = " + str(transparency) + "   " + balancedFlag + "\n")
    with open("resultTable.txt", mode="a+", encoding="utf-8") as f:
        f.write("********************************************************" + "\n\n\n")


'''
    单个进程需要完成的工作
'''
def oneProcess(varsNum, pos, oneNumList, oribitList, innerProduct):
    indexList = initRSBF(varsNum, oneNumList, oribitList)
    truthTable = TruthTableSelect(varsNum, indexList)
    nonlinearity = nonlinearityCompute(varsNum, truthTable, innerProduct)
    costDic = {}
    tableDic = {}
    if nonlinearity >= 234:
        cost = costFunction(varsNum, truthTable, indexList, nonlinearity)
        costDic[pos] = cost
        tableDic[pos] = oneNumList
        return costDic, tableDic


'''
    创建进程池并分配任务
    在任务结束以后，整合搜索结果，并对优秀结果进行记录
'''
def alg(varsNum, lst, oribitList, innerProduct, initCondtionNodeList):
    res = updateOribit(lst)
    processPool = Pool(os.cpu_count())
    costDic = {}
    tableDic = {}
    processResList = []
    for i in range(len(res)):
        processResType = processPool.apply_async(oneProcess, args = (varsNum, i, res[i], oribitList, innerProduct, ))
        processResList.append(processResType)
    processPool.close()
    processPool.join()
    for processRes in processResList:
        if processRes.get() is None:
            continue
        else:
            cost, table = processRes.get()
            costDic[list(cost.keys())[0]] = list(cost.values())[0]
            tableDic[list(table.keys())[0]] = list(table.values())[0]
    # 对字典依照value值进行排序，由小到大
    costDicList = sorted(costDic.items(), key=lambda x: x[1], reverse=False)
    record(varsNum, costDicList, tableDic, innerProduct, oribitList)

    '''
        判断本轮最优值，是否已经作为初始条件，
        若是，则由次优值作为初始条件列表，并将次优值加入初始条件列表，防止再次使用
    '''
    for i in range(len(costDicList)):
        if tableDic[list(costDicList[i])[0]] in initCondtionNodeList:
            continue
        else:
            initCondtionNodeList.append(tableDic[list(costDicList[i])[0]])
            with open("initCondition.txt", mode = "a+", encoding = "utf-8") as f:
                f.write(str(tableDic[list(costDicList[i])[0]]) + ",")
            return tableDic[list(costDicList[i])[0]]


'''
    初始主程序
'''
def compute(varsNum):
    count = 0
    lst1 = [1, 3, 6, 7, 9, 16, 17, 18, 19, 22, 25, 26, 27, 29, 31, 32, 35, 37, 38, 40, 41, 42, 46, 49, 50, 51, 53, 55, 59, 60]

    oribitList = finalOribit(varsNum)
    innerProduct = innerProductSelect(varsNum)
    initCondtionNodeList = []
    initCondtionNodeList.append(copy.deepcopy(lst1))
    for ele in conditionList():
        initCondtionNodeList.append(copy.deepcopy(ele))
    while count < 1000:
        count += 1
        lst = alg(varsNum, lst1, oribitList, innerProduct, initCondtionNodeList)
        lst1 = copy.deepcopy(lst)
        if count % 100 == 0 or count == 1:
            print(count)


if __name__ == '__main__':
    strat = time.time()
    compute(9)
    end = time.time()
    print("during time is ", (end - strat) / 60 )
    #
    # lst1 = [1, 2, 3, 5, 10, 11, 12, 13, 14, 16, 17, 18, 21, 33, 34, 35, 36, 37, 38, 42, 43, 44, 46, 47, 48, 52, 56, 59]
    # tmp = updateOribitThreePos(lst1)
    # res = updateOribit(lst1)
    # processTaskList = []
    # tmpList = []
    # for i in range(len(res)):
    #     tmpList.append(res[i])
    #     if (i % 295 == 0 or i == len(res) - 1) and i != 0:
    #         processTaskList.append(copy.deepcopy(tmpList))
    #         tmpList.clear()
    # print(len(processTaskList))





