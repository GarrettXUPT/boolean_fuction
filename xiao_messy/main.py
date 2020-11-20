
from walsh_and_nonlinearity import nonlinearityCompute
from transparency import transparencyCompute, truthTableAndIndexLixt


if __name__ == '__main__':

    varsNum = int(input("请输入布尔函数变元个数："))
    
    truthTable, dicIndexList = truthTableAndIndexLixt(varsNum)
    print(dicIndexList)

    balancedFlag = False
    oneNum = 0
    zeroNum = 0
    for ele in truthTable:
        if ele == 1:
            oneNum = oneNum + 1
        else:
            zeroNum = zeroNum + 1
    if oneNum == zeroNum:
        balancedFlag = True
        print("this is a balanced boolean function")

    nonlinearity = nonlinearityCompute(varsNum, truthTable)
    print(f"the nonlinearity = {nonlinearity}")

    transparency = transparencyCompute(varsNum, truthTable, dicIndexList)
    print(f"the transparency = {transparency}")

    # 输出为0的输入形式 [{'x1': 1, 'x2': 1, 'x3': 0}, {'x1': 0, 'x2': 1, 'x3': 1}]

    # [[[0, 0, 0, 0]], [[0, 0, 1, 1], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0]]]
