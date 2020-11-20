from math import sin, pi, floor
import sys

sys.setrecursionlimit(3000)

def x_sequence(a, g1, k1, y):
    return g1 * sin(k1 * pi * a * y)

def y_sequence(b, c, g2, k2, x, y):
    return g2 * sin(k2 * pi * (b * y - c * x * y))

def sequence_gen(Length, x0, y0, x_lst, y_lst):
     if Length == 0:
         return
     x = x_sequence(1, 2, 6, x0)
     y = y_sequence(1.98, 1.0, 2, 6, x0, y0)
     x_lst.append(x)
     y_lst.append(y)
     Length -= 1
     sequence_gen(Length, x, y, x_lst, y_lst)

def sequence_mul_lst(lst1, lst2):
    resLst = []
    if len(lst1) != len(lst2):
        return -1
    for i in range(len(lst1)):
        resLst.append(lst1[i] * lst2[i])
    return resLst

def sequence_add_lst(lst1, lst2):
    resLst = []
    if len(lst1) != len(lst2):
        return -1
    for i in range(len(lst1)):
        resLst.append(lst1[i] + lst2[i])
    return resLst

def sequence_mod(lst, base):
    resLst = []
    for ele in lst:
        resLst.append(ele % base)
    return resLst

def sequence_sub(lst, base):
    if base == 0:
        return lst
    resLst = []
    for ele in lst:
        resLst.append(ele - base)
    return resLst

def sequence_mul(lst, base):
    resLst = []
    for ele in lst:
        resLst.append(ele * base)
    return resLst

def sequence_div(lst, base):
    if base == 0:
        return -1
    resLst = []
    for ele in lst:
        resLst.append(ele / base)
    return resLst

def sequence_floor(lst):
    resLst = []
    for ele in lst:
        resLst.append(floor(ele))
    return resLst

def sequnce_XOR(lst1, lst2):
    resLst = []
    for i in range(len(lst1)):
        resLst.append(lst1[i] ^ lst2[i])
    return resLst

def CPNG_ALG(x_lst, y_lst):
    s = sequence_add_lst(sequence_add_lst(x_lst, y_lst), sequence_mul_lst(x_lst, y_lst))
    T_tmp = sequence_floor(sequence_mul(sequence_div(sequence_sub(s, min(s)), max(s) - min(s)), pow(10, 10)))
    T = sequence_mod(T_tmp, 256)
    return T

def random_gen(x, step):
    lst1 = []
    lst2 = []
    sequence_gen(pow(2, 11), x, x, lst1, lst2)
    T1 = CPNG_ALG(lst1, lst2)
    lst3 = []
    lst4 = []
    sequence_gen(pow(2, 11), x + step, x + step, lst3, lst4)
    T2 = CPNG_ALG(lst3, lst4)
    res = sequnce_XOR(T1, T2)
    return res

if __name__ == '__main__':
    res = random_gen(0.1, 0.00011)
    print(type(res))





