def maxi(mass): #максимальное число в массиве 
    max_ = mass[0]
    for elem in mass:
        if elem > max_:
            max_ = elem
    return max_

def in_dec_num_syst(x, syst): #перевод в десятичную систему счисления (теперь работает с системами больше 10)
    summa = 0
    x = str(x)
    x1 = list()
    for i in range(len(x)):
        x1.append(x[i])
    for i in range(len(x1)):
        if x1[i] == 'A':
            x1[i] = 10
        elif x1[i] == 'B':
            x1[i] = 11
        elif x1[i] == 'c':
            x1[i] = 12
        elif x1[i] == 'D':
            x1[i] = 13
        elif x1[i] == 'E':
            x1[i] = 14
        elif x1[i] == 'F':
            x1[i] = 15
    for i in range(len(x1)):
        summa += int(x1[i]) * syst ** (len(x1) - i - 1)
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

def multip_matrix(m1, m2): #умножение двух матриц (для 10 класса) m1 * m2
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

def fibonacci(amount): #возвращает массив с amount числами из ряда Фибоначчи
    ch = 0
    c = 1
    a = 0
    A = []
    for i in range(amount):
        a = ch
        ch += c
        c = a
        A.append(ch)
    return A

def prost(num): #проверка числа на простоту, возвращает boolean
    if num % 2 != 0:
        k = 0
        for i in range (1, num+1):
            if num % i == 0:
                k += 1
        if k == 2:
            return True
        else:
            return False
    elif num == 2:
        return True
    else:
        return False
  
def mini(mass): #минимальное число в массиве 
    min_ = mass[0]
    for elem in mass:
        if elem < min_:
            min_ = elem
    return min_

def stand_dev(mass): #стандартное отклонение массива (гугли ; ) )
    s = 0
    s1 = 0
    dev = 0
    l = len(mass)
    for i in range(l):
        s += mass[i]
    s = s / l
    for i in range(l):
        s1 += (mass[i] - s) ** 2
    s1 = s1 / (l - 1)
    dev = s1 ** (0.5)
    return dev

def sumMat(mat1, mat2): #Сложение двух матриц
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrixes' sizes should be equal!")
    
    result = list()
    for i in range(len(a)):
        row = list()
        for j in range(len(a)):
            row.append(a[i][j] + b[i][j])
        result.append(row)
        
    return result

def multMatNum(matrix, num): #Умножение матрицы на число
    result = list()
    for i in range(len(matrix)):
        row = list()
        for j in range(len(matrix)):
            row.append(matrix[i][j] * num)
        result.append(row)
    return result
