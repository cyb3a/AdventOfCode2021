import numpy as np

numbers = list(map(int, [line.strip() for line in open('input/04.txt')][0].split(',')))
bingo = list(map(int, ' '.join([line.strip() for line in open('input/04.txt')][1:]).replace('  ', ' ').split()))
bingo_boards = dict()
score = dict()

enumeration = 0
for i in range(0, len(bingo), 25):
    bingo_boards[enumeration] = np.array(bingo[i:i + 25]).reshape((5, 5))
    score[enumeration] = np.ones((5, 5))
    enumeration += 1


def calculate_score(board, score, number):
    for i, row in enumerate(score):
        for j, col in enumerate(row):
            if score[i][j] == 0:
                board[i][j] = 0
    return sum(board.ravel()) * number


def find_winner():
    for num in numbers:
        for board_index in bingo_boards.keys():
            for i, row in enumerate(bingo_boards[board_index]):
                for j, col in enumerate(row):
                    if col == num:
                        score[board_index][i][j] = 0
                        sum_rows = sum(score[board_index][i])
                        sum_columns = score[board_index][0][j] + score[board_index][1][j] + \
                                      score[board_index][2][j] + score[board_index][3][j] + \
                                      score[board_index][4][j]
                        if sum_rows == 0 or sum_columns == 0:
                            return calculate_score(bingo_boards[board_index], score[board_index], num)


print(find_winner())
