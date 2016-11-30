import random 

def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    a = [] 
    b = []
    for i in range(0, len(values), n):  #проходимся от первого элемента к последнему с шагом n с первого элемента по n, добавляем в список b получившиеся списки по 3 элемента мы добаляем в список а получается спикок, в котором списки
        for j in range(i, i + n):     
            b.append(values[j])         #
        a.append(b[i:i + n])            #получается спикок, в котором списки
    return a

def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return values(pos[0])


def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '5', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    col = []
    col = [row[pos[1]] for row in values]  #проходимся по элементам в списке и выводим вторую координату, то есть столбец
    return col 


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos """
    first = (0, 1, 2)
    second = (3, 4, )
    third = (6, 7, 8)
    a = []                                  #создаем пустой список
    if pos[0] in first:                     #смотрим, в каком диапозоне находится первая координата
        if pos[1] in first:                 #смотрим, в каком диапозоне находится вторая координата
            for i in first:                 #затем проходимся по этому диапозону 
                for j in first:             #то есть все [i][j]
                    a.append(values[i][j])  #добавляем каждое значение в пустой список a
        return a
        if pos[1] in second:
            for i in first:
                for j in second:
                    a.append(values[i][j])
        return a
        if pos [1] in third:
            for i in first:
                for j in third:
                    a.append(values[i][j])
        return a
    if pos[0] in second:
        if pos[1] in first:
            for i in second:
                for j in first:
                    a.append(values[i][j])
        return a
        if pos[1] in second:
            for i in second:
                for j in second:
                    a.append(values[i][j])
        return a
        if pos [1] in third:
            for i in second:
                for j in third:
                    a.append(values[i][j])
        return a
    if pos[0] in third:
        if pos[1] in first:
            for i in third:
                for j in first:
                    a.append(values[i][j])
        return a
        if pos[1] in second:
            for i in third:
                for j in second:
                    a.append(values[i][j])
        return a
        if pos [1] in third:
            for i in third:
                for j in third:
                    a.append(values[i][j])
        return [a]
                




def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):              
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j)
    return False

def find_possible_values(grid, pos):
    possible_values = []
    col = get_col(grid, pos)
    row = get_row(grid, pos)
    block = get_block(grid, pos)
    val = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    for i in val:
        if (i not in row) and (i not in col) and (i not in block):
            possible_values.append(i)
    return possible_values

def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    """
    if find_empty_positions(grid) == False:                                  #если нет свободных мест 
        return True
    else:
        empty_position = find_empty_positions(grid)                          #свободная позиция есть и она empty_position
        for possible_values in find_possible_values(grid, empty_position):   #находим возможные значения 
            grid[empty_position[0]][empty_position[1]] = possible_values     #в эти свободные позиции записываем возможное значение
            if solve(grid):                                                  #если в дальнейшем возможно решить, то решаем 
                return True
            grid[empty_position[0]][empty_position[1]] = '.'             #если нет, то ставим точки на эти места и затем подставляем другое возможное значение 
    return False 





def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            in_col = get_col(grid, (i, j)).count(grid[i][j])
            in_row = get_row(grid, (i, j)).count(grid[i][j])
            in_block = list_transform(get_block(grid, (i, j))).count(grid[i][j])
            if (in_col + in_row + in_block) > 3:
                return False
    return True

a = read_sudoku('puzzle1.txt')
display(a)
solve(a)1