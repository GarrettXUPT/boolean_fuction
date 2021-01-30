
from addDeg import getDegree
from xiao_massey import xiao_messay
from transparency import transparencyCompute
from autocorrelation import maxAbsolute
from differentialUniform import uniform
from S_Box_nonlinearity import nonlinearity, binartToHex
from S_BOX_Transparency import modifyMTO, shortTableToLong, revisedTO, boxDegree
from nonAbsoluteIndicator import non_absolute_indicatorSelect
from RSBF import finalOribit, initRSBF, TruthTableSelect, nonlinearityCompute
from judge import longTableToTable, AllTruthTableSelect, trans, isRotationSymmetric


class BooleanFunction:
    def __init__(self, varsNum, shortTable = None, longTable = None, S_BOX_Table = None):
        self.varsNum = varsNum
        self.shortTable = shortTable
        self.longTable = longTable
        self.S_BOX_Table = S_BOX_Table
        if S_BOX_Table == None and longTable == None and shortTable == None:
            print("无真值表输入")


    def __alltruthTable(self):
        return AllTruthTableSelect(self.varsNum)


    def __allOribit(self):
        return finalOribit(self.varsNum)


    def __midProcess(self):
        if self.longTable != None:
            truthTable = longTableToTable(self.longTable)
            dicIndexList = trans(self.varsNum, truthTable, self.__alltruthTable())
            return truthTable, dicIndexList
        else:
            dicIndexList = initRSBF(self.varsNum, self.shortTable, self.__allOribit())
            truthTable = TruthTableSelect(self.varsNum, dicIndexList)
            return truthTable, dicIndexList


    def oribitCount(self):
        return len(self.__allOribit())


    def nonliearity(self):
        midRes = self.__midProcess()
        return nonlinearityCompute(self.varsNum, midRes[0])


    def transparency(self):
        midRes = self.__midProcess()
        return transparencyCompute(self.varsNum, midRes[0], midRes[1])


    def nonlinearityAndTransparency(self):
        midRes = self.__midProcess()
        return nonlinearityCompute(self.varsNum, midRes[0]), \
               transparencyCompute(self.varsNum, midRes[0], midRes[1])


    def S_Box_Nonlinearity(self):
        return nonlinearity(self.varsNum, binartToHex(self.varsNum, shortTableToLong(self.varsNum, self.S_BOX_Table)))

    def S_BOX_MTO(self):
        return modifyMTO(self.varsNum, shortTableToLong(self.varsNum, self.S_BOX_Table))

    def S_BOX_RTO(self):
        return revisedTO(self.varsNum, self.S_BOX_Table)

    def autoCorrelationMaxAbsolute(self):
        return maxAbsolute(self.varsNum, self.S_BOX_Table)

    def isRotationSymmetric(self):
        truthTable, indexList = self.__midProcess()
        return isRotationSymmetric(self.varsNum, truthTable)


    def nonAbsoluteIndictor(self):
        truthTable, indexList = self.__midProcess()
        return non_absolute_indicatorSelect(self.varsNum, truthTable, indexList)


    def relisentCompute(self):
        if self.isBalanced():
            truthTable, indexList = self.__midProcess()
            return xiao_messay(self.varsNum, truthTable, self.__alltruthTable())
        else:
            print("this is a unBalanced function")


    def degree(self):
        truthTable, indexList = self.__midProcess()
        return getDegree(truthTable, self.__alltruthTable())

    def differentialUniformValue(self):
        return uniform(self.varsNum, self.S_BOX_Table)

    def sBoxDegree(self):
        return boxDegree(self.varsNum, self.S_BOX_Table)

    def isBalanced(self):
        if self.__midProcess()[0].count(1)  == pow(2, self.varsNum - 1):
            return "balanced function"
        else:
            return "unbalanced function"


if __name__ == '__main__':
    # for ele in finalOribit(6):
    #     if len(ele) == 6:
    #         print((ele))

    '''
        短表使用
    '''
    varsNum = 8
    shortTable = [3.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 21.0, 23.0, 24.0, 25.0, 26.0, 27.0, 30.0, 31.0, 32.0, 34.0]
    bf = BooleanFunction(varsNum, shortTable=shortTable)

    print(bf.nonlinearityAndTransparency())
    print(bf.isRotationSymmetric())
    print(bf.isBalanced())
    print(bf.relisentCompute())
    print(bf.degree())
    print(bf.nonliearity())
    print(bf.transparency())


    '''
        长表使用
    '''
    varsNum = 8
    longTable = "18CA9ED8BC4EC1AFE2F4C023FA63E78949455BC59DB873BE79409BAE4B289029"
    bf = BooleanFunction(varsNum, longTable=longTable)
    print(bf.nonlinearityAndTransparency())
    print(bf.isRotationSymmetric())
    print(bf.isBalanced())
    print(bf.nonAbsoluteIndictor())
    print(bf.relisentCompute())


    '''
        S盒使用
    '''

    varsNum = 8
    table = [69, 82, 172, 84, 3, 4, 188, 93, 88, 52, 252, 246, 251, 135, 213, 152, 27, 169, 165,
            102, 67, 214, 244, 137, 231, 57, 161, 109, 139, 147, 32, 209, 125, 69, 205, 58, 106,
            30, 143, 41, 224, 167, 85, 189, 158, 193, 108, 220, 184, 215, 182, 111, 16, 64, 140,
            185, 6, 218, 35, 83, 39, 14, 241, 38, 116, 157, 240, 154, 174, 136, 104, 43, 40, 166,
            179, 197, 124, 103, 78, 155, 28, 181, 0, 21, 8, 113, 79, 92, 48, 47, 9, 44, 56, 10,
            226, 151, 129, 159, 225, 119, 76, 62, 230, 175, 126, 253, 138, 236, 162, 160, 53,
            107, 150, 149, 242, 101, 249, 191, 24, 5, 131, 73, 75, 60, 80, 207, 55, 11, 21, 248,
            238, 33, 228, 117, 74, 86, 105, 45, 216, 148, 66, 110, 36, 20, 250, 23, 180, 121,
            130, 194, 115, 99, 192, 171, 59, 232, 243, 208, 254, 127, 217, 210, 146, 202, 134,
            50, 176, 90, 91, 63, 91, 112, 71, 255, 97, 222, 223, 145, 94, 54, 239, 13, 128, 95,
            2, 144, 49, 19, 118, 96, 217, 64, 177, 234, 132, 122, 168, 25, 195, 227, 153, 77, 18,
            22, 12, 183, 221, 233, 170, 42, 247, 200, 178, 190, 187, 114, 206, 212, 164, 15, 17,
            229, 156, 1, 237, 201, 51, 100, 142, 245, 81, 203, 141, 34, 37, 173, 163, 46, 72,
            199, 219, 31, 87, 204, 61, 235, 120, 186, 198, 7, 196, 70, 123, 26, 133, 98]
    bf = BooleanFunction(varsNum, S_BOX_Table=table)
    print(bf.S_Box_Nonlinearity())
    print(bf.autoCorrelationMaxAbsolute())
    print(bf.differentialUniformValue())
    print(bf.sBoxDegree())
    # print(bf.S_BOX_MTO())
