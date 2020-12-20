
from transparency import transparencyCompute
from S_Box_nonlinearity import nonlinearity
from RSBF import finalOribit, initRSBF, TruthTableSelect, nonlinearityCompute, innerProductSelect
from judge import longTableToTable, AllTruthTableSelect, trans, isRotationSymmetric

class BooleanFunction:
    def __init__(self, varsNum, shortTable = None, longTable = None, S_BOX_Table = None):
        self.varsNum = varsNum
        self.shortTable = shortTable
        self.longTable = longTable
        self.S_BOX_Table = S_BOX_Table

    def __midProcess(self):
        if self.longTable != None:
            truthTable = longTableToTable(self.longTable)
            alltruthTable = AllTruthTableSelect(self.varsNum)
            dicIndexList = trans(self.varsNum, truthTable, alltruthTable)
            return truthTable, dicIndexList
        else:
            OribitList = finalOribit(self.varsNum)
            dicIndexList = initRSBF(self.varsNum, self.shortTable, OribitList)
            truthTable = TruthTableSelect(self.varsNum, dicIndexList)
            return truthTable, dicIndexList

    def oribitCount(self):
        return len(finalOribit(self.varsNum))

    def tableNonliearity(self):
        midRes = self.__midProcess()
        return nonlinearityCompute(self.varsNum, midRes[0], innerProductSelect(self.varsNum))

    def tableTransparency(self):
        midRes = self.__midProcess()
        return transparencyCompute(self.varsNum, midRes[0], midRes[1])

    def nonlinearityAndTransparency(self):
        midRes = self.__midProcess()
        return nonlinearityCompute(self.varsNum, midRes[0], innerProductSelect(self.varsNum)), \
               transparencyCompute(self.varsNum, midRes[0], midRes[1])

    def S_Box_Nonlinearity(self):
        return nonlinearity(self.varsNum, self.S_BOX_Table)

    def isRotationSymmetric(self):
        midRes = self.__midProcess()
        return isRotationSymmetric(self.varsNum, midRes[0])

    def isBalanced(self):
        if self.__midProcess()[0].count(1)  == pow(2, self.varsNum - 1):
            return "balanced function"
        else:
            return "unbalanced function"


if __name__ == '__main__':
    '''
        短表使用
    '''
    shortTable = [1, 2, 3, 4, 8, 11, 13, 17, 18,  20, 22, 25, 26, 30, 31, 33, 34, 36, 37, 38, 39, 40, 42, 47, 49, 50, 53, 55, 56, 57]
    bf = BooleanFunction(9, shortTable=shortTable)
    print(bf.nonlinearityAndTransparency())
    print(bf.isRotationSymmetric())
    print(bf.isBalanced())


    '''
        长表使用
    '''
    longTable = "04757A727ED96F087EFCE2C768EB04947AECFBA5B91DE42E7CC1AC8B1060D6712FCCEDB0EE8B8926CAD357A2E92148ED3AB4A1128DF0918B46143C51A66D2B16"
    bf = BooleanFunction(9, longTable=longTable)
    print(bf.nonlinearityAndTransparency())
    print(bf.isRotationSymmetric())
    print(bf.isBalanced())


    '''
        S盒使用
    '''
    TRUTHTABLE1 = ["6 3", "7 C", "7 7", "7 B", "F 2", "6 B", "6 F", "C 5", "3 0", "0 1", "6 7", "2 B", "F E", "D 7",
                   "A B", "7 6",
                   "C A", "8 2", "C 9", "7 D", "F A", "5 9", "4 7", "F 0", "A D", "D 4", "A 2", "A F", "9 C", "A 4",
                   "7 2", "C 0",
                   "B 7", "F D", "9 3", "2 6", "3 6", "3 F", "F 7", "C C", "3 4", "A 5", "E 5", "F 1", "7 1", "D 8",
                   "3 1", "1 5",
                   "0 4", "C 7", "2 3", "C 3", "1 8", "9 6", "0 5", "9 A", "0 7", "1 2", "8 0", "E 2", "E B", "2 7",
                   "B 2", "7 5",
                   "0 9", "8 3", "2 C", "1 A", "1 B", "6 E", "5 A", "A 0", "5 2", "3 B", "D 6", "B 3", "2 9", "E 3",
                   "2 F", "8 4",
                   "5 3", "D 1", "0 0", "E D", "2 0", "F C", "B 1", "5 B", "6 A", "C B", "B E", "3 9", "4 A", "4 C",
                   "5 8", "C F",
                   "D 0", "E F", "A A", "F B", "4 3", "4 D", "3 3", "8 5", "4 5", "F 9", "0 2", "7 F", "5 0", "3 C",
                   "9 F", "A 8",
                   "5 1", "A 3", "4 0", "8 F", "9 2", "9 D", "3 8", "F 5", "B C", "B 6", "D A", "2 1", "1 0", "F F",
                   "F 3", "D 2",
                   "C D", "0 C", "1 3", "E C", "5 F", "9 7", "4 4", "1 7", "C 4", "A 7", "7 E", "3 D", "6 4", "5 D",
                   "1 9", "7 3",
                   "6 0", "8 1", "4 F", "D C", "2 2", "2 A", "9 0", "8 8", "4 6", "E E", "B 8", "1 4", "D E", "5 E",
                   "0 B", "D B",
                   "E 0", "3 2", "3 A", "0 A", "4 9", "0 6", "2 4", "5 C", "C 2", "D 3", "A C", "6 2", "9 1", "9 5",
                   "E 4", "7 9",
                   "E 7", "C 8", "3 7", "6 D", "8 D", "D 5", "4 E", "A 9", "6 C", "5 6", "F 4", "E A", "6 5", "7 A",
                   "A E", "0 8",
                   "B A", "7 8", "2 5", "2 E", "1 C", "A 6", "B 4", "C 6", "E 8", "D D", "7 4", "1 F", "4 B", "B D",
                   "8 B", "8 A",
                   "7 0", "3 E", "B 5", "6 6", "4 8", "0 3", "F 6", "0 E", "6 1", "3 5", "5 7", "B 9", "8 6", "C 1",
                   "1 D", "9 E",
                   "E 1", "F 8", "9 8", "1 1", "6 9", "D 9", "8 E", "9 4", "9 B", "1 E", "8 7", "E 9", "C E", "5 5",
                   "2 8", "D F",
                   "8 C", "A 1", "8 9", "0 D", "B F", "E 6", "4 2", "6 8", "4 1", "9 9", "2 D", "0 F", "B 0", "5 4",
                   "B B", "1 6"]
    bf = BooleanFunction(8, S_BOX_Table=TRUTHTABLE1)
    print(bf.S_Box_Nonlinearity())