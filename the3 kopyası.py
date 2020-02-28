import copy
import sys


def readmap(file):
    f = open(file, "r")
    board_state = []
    for line in f:
        myline = []
        for i in line:
            if i == "-":
                myline += [0]
            if i == "*":
                myline += [1]
        board_state += [myline]

    return board_state
    f.close()


def list_of_ne(map):
    all_neighbours_points = []
    if len(map) == 1:
	return [[[0,0],[]]]
    for i in range(len(map)):
        for n in range(len(map[0])):
            if i == 0 and n == 0:
                neighbour = [map[0][1], map[1][1], map[1][0]]
            elif i == 0 and n == len(map[0]) - 1:
                neighbour = [map[0][-2], map[1][-1], map[1][-2]]
            elif i == len(map) - 1 and n == 0:
                neighbour = [map[-1][1], map[-2][0], map[-2][1]]
            elif i == len(map) - 1 and n == len(map[0]) - 1:
                neighbour = [map[-1][-2], map[-2][-1], map[-2][-2]]
            elif i == 0 and n != 0 and n != len(map[0]) - 1:
                neighbour = [map[1][n], map[1][n - 1], map[1][n + 1], map[0][n - 1], map[0][n + 1]]
            elif n == 0 and i != 0 and i != len(map) - 1:
                neighbour = [map[i - 1][0], map[i + 1][0], map[i - 1][1], map[i][1], map[i + 1][1]]
            elif i == len(map) - 1 and n != 0 and n != len(map[0]) - 1:
                neighbour = [map[-1][n - 1], map[-1][n + 1], map[-2][n - 1], map[-2][n], map[-2][n + 1]]
            elif n == len(map[i]) - 1 and i != len(map) - 1 and i != 0:
                neighbour = [map[i - 1][-1], map[i + 1][-1], map[i - 1][-2], map[i][-2], map[i + 1][-2]]
            elif i != 0 and n != 0 and i != len(map) - 1 and n != len(map[0]) - 1:
                neighbour = [map[i - 1][n - 1], map[i - 1][n], map[i - 1][n + 1], map[i][n - 1], map[i][n + 1],
                             map[i + 1][n - 1], map[i + 1][n], map[i + 1][n + 1]]
            all_neighbours_points += [[[i, n], neighbour]]
    return all_neighbours_points


def readrules(file):
    f = open(file, "r")
    rule = []
    for line in f:
        source = line[0]
        cond = line[1]
        num = int(line[2])
        lastdig = line[3]
        if cond == "=":
            rule += [[1, source, num, lastdig]]
        elif cond == "<":
            rule += [[2, source, num, lastdig]]
        elif cond == ">":
            rule += [[3, source, num, lastdig]]
    return rule
    f.close()


def exerules(rules, board, generation):
    new_board = copy.deepcopy(board)
    r_board = copy.deepcopy(board)
    while generation > 0:
        neighbourhood = list_of_ne(r_board)
        for r in rules:
            h = int(r[0])
            source = r[1]
            num = int(r[2])
            lastdig = r[3]
            for i in neighbourhood:
                point = i[0]
                x = point[0]
                y = point[1]
                neighbours = i[1]
                if h == 1:
                    if source == "-":
                        if r_board[x][y] == 0:
                            if neighbours.count(1) == num:
                                if lastdig == "*":
                                    new_board[x][y] = 1
                    elif source == "*":
                        if r_board[x][y] == 1:
                            if neighbours.count(1) == num:
                                if lastdig == "-":
                                    new_board[x][y] = 0
                elif h == 2:
                    if source == "-":
                        if r_board[x][y] == 0:
                            if neighbours.count(1) < num:
                                if lastdig == "*":
                                    new_board[x][y] = 1
                    elif source == "*":
                        if r_board[x][y] == 1:
                            if neighbours.count(1) < num:
                                if lastdig == "-":
                                    new_board[x][y] = 0
                elif h == 3:
                    if source == "-":
                        if r_board[x][y] == 0:
                            if neighbours.count(1) > num:
                                if lastdig == "*":
                                    new_board[x][y] = 1
                    elif source == "*":
                        if r_board[x][y] == 1:
                            if neighbours.count(1) > num:
                                if lastdig == "-":
                                    new_board[x][y] = 0
        r_board = copy.deepcopy(new_board)
        generation -= 1
    return new_board


def printmap(board_state):
    for row in board_state:
        resultline = ""
        for i in row:
            if i == 0:
                resultline += "-"
            if i == 1:
                resultline += "*"
        print resultline


w = sys.argv[1]  # map_path
t = sys.argv[2]  # rules_path
z = sys.argv[3]  # number of generations


mymap = readmap(w)
ruleList = readrules(t)
res = exerules(ruleList, mymap, int(z))
printmap(res)
