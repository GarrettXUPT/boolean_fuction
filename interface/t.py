import matplotlib.pyplot as plt


def figure1():
    x_data = ['n = 400','n = 500','n = 600','n = 700','n = 800']
    y1_data = [33.91, 43.037, 52.619, 62.41, 70.836]
    y2_data = [13512.718, 28093.517, 55298.47,97193.756,159190.287]
    y3_data = [167927.372, 264634.147, 377979.489, 513340.065, 670820.937]
    y4_data = [8800.428, 13900.749, 20300.31, 27800.004, 36500.882]
    y5_data = [11574.687, 22764.303, 39072.307, 61935.196, 92610.783]


    plt.plot(x_data,y1_data,  marker='*', label = "KeyGen")
    plt.plot(x_data, y2_data, marker='s',  label = "ProGen")
    plt.plot(x_data, y3_data,  marker='v',label = "Compute")
    plt.plot(x_data, y4_data,   marker='+',label = "Verify")
    plt.plot(x_data, y5_data,   marker='p',label = "Solve")
    plt.legend()
    plt.xlabel("the size of Matrix")
    plt.ylabel("cost time")

    plt.show()

def figure2():
    x_data = ['n = 400','n = 500','n = 600','n = 700','n = 800']
    y3_data = [162927.372, 259334.147, 372179.489, 508540.065, 665420.937]
    print(y3_data)
    y5_data = [13512.718 + 11574.687, 28093.517 + 22764.303, 55298.47 + 39072.307, 97193.756 + 61935.196, 159190.287 + 92610.783]
    print(y5_data)
    plt.plot(x_data, y5_data, marker = 'x', label = "EncAndDec")
    plt.plot(x_data, y3_data, marker = 'o', label = "QR")
    plt.legend()
    plt.xlabel("the size of Matrix")
    plt.ylabel("cost time")
    plt.show()

if __name__ == '__main__':
    figure1()
    figure2()
