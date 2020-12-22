
def upperBound(varsNum, nonlinearity):
    second = pow(pow(2, varsNum) - 2 * nonlinearity, 2) / (pow(2, varsNum) * (pow(2, varsNum)  - 1))
    thrid = 1 / (pow(2, varsNum) - 1)
    return 1 - second + thrid

if __name__ == '__main__':
    print(upperBound(9, 241))

