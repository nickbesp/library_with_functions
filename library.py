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
    if num == 2:
        return True
    if num == 1:
        return False
    if num % 2 != 0:
        k = 0
        for i in range (1, int(num ** 0.5) + 1):
            if num % i == 0:
                k += 2
        if k == 2:
            return True
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

#Транспонирование матриц
def transpos(matrix):
    #Создание пустой матрицы jxi (изначально у нас ixj)
    result = list()
    for i in range(len(matrix[0])):
        row = list()
        for j in range(len(matrix)):
            row.append(0)
        result.append(row)
        
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result

#Определитель матрицы
def det(matrix):

    if len(matrix) != len(matrix[0]):
        raise ValueError('The number of the rows of the matrix should be equal with the number of the columns!')

    if len(matrix) == 2:
        return minor(matrix)
    
    #Правило Лапласа
    summ = 0
    for j in range(len(matrix)):
        elem = matrix[0][j]
        summ += elem * adding(matrix, 0, j)

    return summ

#Алгоритмическое дополнение элемента матрицы
def adding(matrix, i, j):
    if len(matrix) == 2:
        return(minor(matrix) * (-1)**(i + j))

    #Создание матрицы на порядок меньше, для которой будет считаться минор
    new_mat = list()
    for q in range(len(matrix[0])):
        if q == i:
            continue
        row = list()
        for w in range(len(matrix)):
            if w == j:
                continue
            row.append(matrix[q][w])
        new_mat.append(row)

    return det(new_mat) * (-1)**(i + j)

#Минор к элементу матрицы 2x2
def minor(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def branch(self):
        if self.a > 0:
            return 'up'
        else:
            return 'down'
        
    def x_sect(self):
        dis = self.b**2 - 4*self.a*self.c
        if dis < 0:
            return 0
        if dis == 0:
            return 1
        
        x1 = (-self.b + dis**0.5) / (2*self.a)
        x2 = (-self.b - dis**0.5) / (2*self.a)
        if x1 == x2:
            return 1
        else:
            return 2
    
    def y_sect(self):
        return (0, self.c)
    
    def sections(self):
        dis = self.b**2 - 4*self.a*self.c
        if dis < 0:
            return None
        if dis == 0:
            x = (-self.b) / (2*self.a)
            return (x, 0.0)
        
        x1 = (-self.b + dis**0.5) / (2*self.a)
        x2 = (-self.b - dis**0.5) / (2*self.a)
        return ((min(x1, x2), 0.0), (max(x1, x2), 0.0))  
    
    def top(self):
        x = (-self.b) / (2*self.a)
        y = self.a * x ** 2 + self.b * x + self.c
        return (x, y)

#Крестики-нолики
from random import randint

class Board:
    def __init__(self, height=3, width=3):
        self.height = height
        self.width = width
        self.cells = [[''] for j in range(self.width) for i in range(self.height)]

    def put(self, x, y, symb):
        self.cells[x][y] = symb

    def check(self, x, y):
        return self.cells[x][y] == ''

    def __str__(self):
        for i in range(self.height):
            print(*self.cells[i])

    def checker(self, symb):
        pass

class Player:
    def __init__(self, symbol):
        self.symb = symbol

    def coordinates(other):
        x, y = map(int, input('Куда вы бы хотели сходить? \n').split())
        while not other.check(x, y):
            print('Данная клетка занята...')
            x, y = map(int, input('Куда вы бы хотели сходить? \n').split())
        else:
            return (x, y)

class Bot(Player):
    def __init__(self, symbol):
        self.symb = symbol

    def choose(self, other):
        x = randint(0, other.width)
        y = randint(0, other.height)
        while not other.check(x, y):
            print('Бот думает...')
            x = randint(0, other.width)
            y = randint(0, other.height)
        else:
            return (x, y)


if __name__ == "__main__":
    symbol = input('Выберите знак, которым будете играть: \n')
    while symbol == '' or len(symbol) != 1:
        print('Символ должен быть длиной в один символ...')
        symbol = input('Выберите знак, которым будете играть: \n')

    #width, height = map(int, input('Назовите размерность поля: \n').split())
    width = 3
    height = 3
    board = Board(height, width)
    player = Player(symbol)

    if symbol != 'X':
        symbol1 = 'X'
    else:
        symbol1 = 'O'

    bot = Bot(symbol1)

    win = False
    while not win:
        coor = player.coordinates(board)
        board.put(coor[0], coor[1])
        #win = 
