from RSBF import finalOribit, initRSBF, TruthTableSelect
from walsh_and_nonlinearity import nonlinearityCompute
from innerproduct import innerProductSelect
from transparency import transparencyCompute
from readTensor import resultMatrix

def perprority(varsNum, lst):
    OribitList = finalOribit(varsNum)
    dicIndexList = initRSBF(varsNum, lst, OribitList)
    truthTable = TruthTableSelect(varsNum, dicIndexList)
    res1 = nonlinearityCompute(varsNum, truthTable, innerProductSelect(varsNum))
    print(res1)
    if res1 < 230:
        return
    flag = ""
    if truthTable.count(1) == pow(2, varsNum):
        flag = "balanced"
    res2 = transparencyCompute(varsNum, truthTable, dicIndexList)
    with open("best.txt", mode = "a+", encoding="utf-8") as f:
        f.write(str(lst) + "    nonlinearity = " + str(res1) + "    transparency = " + str(res2) + "    " + flag + "\n")
    print("nonlinearity = ", res1)
    print("transparency", res2)

if __name__ == '__main__':
    lst = resultMatrix("res.txt")
    # print(len(lst))
    for ele in lst:
        perprority(9, ele)