
import copy
import time
from S_Box_nonlinearity import hexToBinary
from walsh_and_nonlinearity import nonlinearityCompute
from transparency import transparencyCompute
from RSBF import finalOribit, AllTruthTableSelect, initRSBF, TruthTableSelect
from innerproduct import innerProductSelect

'''
    判断长表的非线性度和透明阶
'''

def EightVars_AllTruthTable():
    resList = []
    dicValueOfx = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    dicValueOfx["x1"] = i1
                                    dicValueOfx["x2"] = i2
                                    dicValueOfx["x3"] = i3
                                    dicValueOfx["x4"] = i4
                                    dicValueOfx["x5"] = i5
                                    dicValueOfx["x6"] = i6
                                    dicValueOfx["x7"] = i7
                                    dicValueOfx["x8"] = i8
                                    resList.append(copy.deepcopy(list(dicValueOfx.values())))
    return resList

def NineVars_AllTruthTable():
    resList = []
    dicValueOfx = {"x1" : 0, "x2" : 0, "x3" : 0, "x4" : 0, "x5" : 0, "x6" : 0, "x7" : 0, "x8" : 0, 'x9' : 0}
    for i1 in range(0, 2):
        for i2 in range(0, 2):
            for i3 in range(0, 2):
                for i4 in range(0, 2):
                    for i5 in range(0, 2):
                        for i6 in range(0, 2):
                            for i7 in range(0, 2):
                                for i8 in range(0, 2):
                                    for i9 in range(0, 2):
                                        dicValueOfx["x1"] = i1
                                        dicValueOfx["x2"] = i2
                                        dicValueOfx["x3"] = i3
                                        dicValueOfx["x4"] = i4
                                        dicValueOfx["x5"] = i5
                                        dicValueOfx["x6"] = i6
                                        dicValueOfx["x7"] = i7
                                        dicValueOfx["x8"] = i8
                                        dicValueOfx["x9"] = i9
                                        resList.append(copy.deepcopy(list(dicValueOfx.values())))
    return resList



def trans(varsNum, truthTable, AlltruthTable):
    # print(truthTable)
    oneNumList = []
    for i in range(len(truthTable)):
        if truthTable[i] == 1:
            oneNumList.append(i)
    # print(oneNumList)
    # print(len(oneNumList))
    oneNumDic = {}
    for ele in oneNumList:
        oneNumDic[ele] = AlltruthTable[ele]

    resTmpList = []
    for k, ele in oneNumDic.items():
        resTmpList.append(ele)
    # print(resTmpList)

    Dic = {}
    List = []
    num = 0
    for ele in resTmpList:
        for elem in ele:
            Dic[num % varsNum] = elem
            num = num + 1
        List.append(copy.deepcopy(Dic))
    # print(List)
    return List





def functionTruthTable():
    TruthTableList1 = ["4 6 4 A B D 0 1 5 7 6 F 7 3 2 1 4 1 5 D E 0 6 2 B 3 D 7 7 B 2 1 "
                       "0 2 2 4 A E 7 B 3 5 D D 0 A 7 B A 8 7 8 2 A A 7 A 6 5 6 7 B 7 4"]

    TruthTableList2 = ["3 8 F 7 9 8 0 8 E 0 B 3 7 6 B 6 9 A 2 7 B D 6 C 4 D 0 A A C 4 B "
                       "E 5 E A 2 F 4 C E 9 D 0 1 A 8 3 1 2 9 0 3 6 E B E E C 3 0 3 B D"]

    '''
        九元函数
    '''
    nineTrutable = []

    # tableStr1 = "978081AE7E1637A991FCED2D1FC58C7D82E8FE4B12E3A3A2E8AF4E66844A2A0C80E2E97E51BC8BDFF819461F8CA5D8F2F86ED910CAA8D33C3A248FD94D32445E"
    # tableStr  = "977A3F880FEB94D045FEF8DFD770F2016466FBE8FA95B6AFE37E2E40EA4844467C70396CBECFFCC1AAD8C7639E2888AAEC5A6BE90CB96000AC99258025303468"
    # tableStr = "E79B73C465BE543E76D27FB23980BAF661884656251B7E435437250B803D1E7276E675DA2FC893725392F6D5240DC45029C0FB6017D3E090DBE4BEB819589F46"
    # tableStr1 = "85320B0C14DB50F10774F7CB3750BA16416A7E61AE7FF4CF4F6F2601CE88467C34126DCD3EF97C4698E92FEBBB21A0AE64BB6DEA49395102A5B895D0347C6EA0"

    # tableStr = "464ABD01576F7321415DE062B3D77B210224AE7B35DD0A7BA8782AA7A6567B74"
    # tableStr = "38F79808E0B376B69A27BD6C4D0AAC4BE5EA2F4CE9D01A83129036EBEEC303BD"
    # tableStr = "5A1A6E4E143B1C6E7FB722496B67512F523CF3FC619F0D45504801AD5E85756C"
    tableStr1 = "679A37C7548A01256D9475C65BA6B86D7747232F75C61177382F39638065C8B9"
    # tableStr1 = "18CA9ED8BC4EC1AFE2F4C023FA63E78949455BC59DB873BE79409BAE4B289029 "
    #
    # tableStr = "FAD9A687CD2C806FA1B609B185446CBBC9068F3D51C3DE53803674607DF08BDAA5D3107C95AE1EE26356B11FA3BD664EC0511B6D7A746D152EE3AE50849BE6D8CD23B20B16153AA59237D9ED06E8FC1C3D4E72689E5717AA8D5BCEB7292C25ACB141674347DB28E67AC86F703DA7123259B9BD0AC8BC7344D57086DAFC2CE281"
    #
    # tableStr = "F5C60527E46C429E193A27156FEC77B2F2CD003C168AE778230E18BB8E2481BD5F53AF561BE4BAFB4D9864D21C74603142EFA5F2E79ED47B65B342C0CBB77AFD390F964568F479C8F7C5A380D1791ED4C1FD99717790524648008A2E894B54F39057B21BC7D31E52A39E37F6433E252E73867E50D542AAF111D0C4CE60694AB9"

    # tableStr = "FFEABDC8DEF6A580E7BCEF6C8937C004AD2F9BF1F8BB2CA1C5835A3FF4015571DCB218AB829BFF02EB809BCB48A0DD56E067D54A62CC4BFBBA21001733276A17E6F4DF195284C9CEC00C828FBEBA0119FC9B9140C28BE0DE74C09811E6A66778AC443C3BE6232199780DE1B1319FBA9EDEC91D525141166A1F4B0C7F3DDD522BF878EE30B6BA1782335DC521B1C7E1FDE44105F0905980FE8BF88A9D41075387AEF5C29A82036415E558818EE845A2BC2A65A115C3955746E97CD968792F7FC1CCA464705FB15B9FA93C4D0E1C0793D32F8401A7BC128B060B1797FA9ED8D3F9A2ACF5D716B2635D32136412177C6CDD02FF649F45A47EAF0FA7B2E3334959DE"

    # tableStr = "848E94522D64CD4D1C1C6D9A5EE2CBE7BDB0A9B1391DD266CDFD1608F175ADD48E499AAB278320430A2902484C0CD22D1FE314B613D6412A40438172DC08F38B954360287CD8378B5C81C1E5A6049E0BABD8F79711F6352EDFF4BFF1A2B709595641B8F4B964257C17E4E793DF02F79C9F418A1FC1A86AF608E5AE84EBB5C170D29C35B49644E7947B1AA73AB06F2FCED9B13E06F1F8ADCC7669AE60861310218970E37E116B2D6E13F8AE82F172F7ED19BE55318A45FFF97608607E042D676C368665B924C44435DA6D2CCAE627D5B1EC6E5635ACD0D3F459FAFB0DEF81D34A924525A83BD8ACFAA5E8DC2ED3DC4128BBC05323C812D19F57DE7427F1EC2AFE"

    # tableStr1 = "005562677D592D7A3BE632C34DA23BCC0F8BFD3C5A49B05A31F6C94C5E9AE4A0"

    resStr = ""
    for ele in tableStr1:
        resStr = resStr + ele + " "
    # print(resStr)
    tmpList = resStr.split(" ")
    tmpList.pop()
    binaryListTmp = hexToBinary(tmpList)
    binaryList = []
    for ele in binaryListTmp:
        for elem in ele:
            binaryList.append(elem)
    # print(binaryList)
    return binaryList

def isRotationSymmetric(varsNum, truthTable):
    oribitList = finalOribit(varsNum)
    print(len(oribitList))
    nineTable = AllTruthTableSelect(varsNum)
    shortTableOribitList = []
    for ele in oribitList:
        tmpList = []
        for i in range(len(nineTable)):
            if nineTable[i] in ele:
                tmpList.append(i)
        shortTableOribitList.append(copy.deepcopy(tmpList))

    TableOribitList = []
    for ele in shortTableOribitList:
        tmpList = []
        for elem in ele:
            tmpList.append(truthTable[elem])
        TableOribitList.append(copy.deepcopy(tmpList))

    '''
        判断是否为旋转对称布尔函数
    '''
    FlagList = []
    for ele in TableOribitList:
        if ele.count(0) == len(ele) or ele.count(1) == len(ele):
            FlagList.append(True)
        else:
            FlagList.append(False)


    '''
        此处可获得短表
    '''
    shortList = []
    for i in range(len(TableOribitList)):
        if TableOribitList[i].count(1) == len(TableOribitList[i]):
            shortList.append(i + 1)
    print(shortList)


    if FlagList.count(True) == len(TableOribitList):
        print("Rotation Symmetric Prove")
    else:
        print("The function is not Rotation Symmetric")




if __name__ == '__main__':
    start = time.time()
    varsNum = 8
    truthTable = functionTruthTable()
    print(truthTable)
    innerProduct = innerProductSelect(varsNum)
    isRotationSymmetric(varsNum, truthTable)
    print(truthTable.count(1))
    alltruthTable = AllTruthTableSelect(varsNum)
    indexDicList = trans(varsNum, truthTable, alltruthTable)
    nonlinearity = nonlinearityCompute(varsNum, truthTable, innerProduct)
    end = time.time()
    transparency = transparencyCompute(varsNum, truthTable, indexDicList)
    print("during time is ", (end - start) / 60)
    print(f"the nonlinearity = {nonlinearity}")
    print(f"the transparency = {transparency}")
    # #





    # varsNum = 9
    # oneNumList = [2, 4, 5, 9, 11, 12, 13, 14, 19, 20, 22, 23, 27, 28, 29, 31, 37, 38, 39, 43, 44, 45, 47, 50, 52, 53, 54, 56, 58, 59]
    # OribitList = finalOribit(varsNum)
    # dicIndexList = initRSBF(varsNum, oneNumList, OribitList)
    # truthTable = TruthTableSelect(varsNum, dicIndexList)
    # isRotationSymmetric(9, truthTable)
