def maxi(mass): #максимальное число в массиве 
    max_ = mass[0]
    for elem in mass:
        if elem > max_:
            max_ = elem
    return max_

def in_dec_numsyst(x, syst): #перевод в десятичную систему счисления
    summa = 0
    x = str(x)
    for i in range(len(x)):
        summa += int(x[i]) * syst ** (len(x) - i - 1)
    return summa

def from_dec_numsyst(x, syst): #перевод из десятичной системы счисления
    s = ''
    while x // syst != 0:
        s += str(x % syst)
        x = x // syst
    s += str(x)
    return s[::-1]

def amount_words(s): #количество слов в строке :)
    k = 0
    s = ' ' + s
    for i in range(len(s) - 1):
        if s[i] == ' ' and s[i + 1] != ' ':
            k += 1
    return k

def matrix_x_matrix(m1, m2): #умножение двух матриц (для 10 класса) m1 * m2
    err = 'Error! This version does not work with matrices in which the number of rows of the first does not match the number of columns of the second! Try to find another algorithm or write your own.'
    r = []
    m = []
    if len(m1) == len(m2[0]):
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                sums = 0
                for k in range(len(m2)):
                    sums += (m1[i][k] * m2[k][j])
                r.append(sums)
            m.append(r)
            r = []
        return m
    else:
        return err

def amount_num_in_matrix(mat, num): #количество чисел num в двумерном массиве mat
    k = 0
    n = len(mat)
    for i in range(n):
        for j in range(len(mat[i])): 
            if mat[i][j] == num:
                k += 1   
    return k    
