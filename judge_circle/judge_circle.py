def judge_circle_naive(moves: str) -> bool:
    x = [0 for i in range(len(moves))]
    y = [0 for i in range(len(moves))]
    for i in range(len(moves)):
        if moves[i] == 'R':
            x[i] += 1
        elif moves[i] == 'L':
            x[i] -= 1
        elif moves[i] == 'U':
            y[i] += 1
        elif moves[i] == 'D':
            y[i] -= 1
    return sum(x) == sum(y) == 0


def judge_circle_concise(moves: str) -> bool:
    x =0
    y=0
    for move in moves:
        if move == 'R':
            x+= 1
        elif move == 'L':
            x-= 1
        elif move == 'U':
            y+= 1
        elif move == 'D':
            y -= 1
    return x==0 & y==0