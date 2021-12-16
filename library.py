def large(arr): #max() 
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
            max_ = ele
    return max_

def in_dec_num_syst(x, syst): #перевод в десятичную систему счисления
    summa = 0
    x = str(x)
    for i in range(len(x)):
        summa += int(x[i]) * syst ** (len(x) - i - 1)
    return summa

def from_dec_num_syst(x, syst): #перевод из десятичной системы счисления
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

def matrix_x_matrix(m1, m2): #Умножение двух матриц (для 10 класса)
    r = []
    m = []
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            sums = 0
            for k in range(len(m2)):
                sums += (m1[i][k] * m2[k][j])
            r.append(sums)
        m.append(r)
        r = []
    return m
