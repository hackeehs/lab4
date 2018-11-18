def enter_matrix():
    a = []
    print("Введите матрицу А 3x3: ")
    for i in range(3):
        a.append([int(j) for j in input().split()])
    b = []
    print("Введите матрицу B 3x1: ")
    for i in range(3):
        b.append([int(j) for j in input().split()])
    print("Введите матрицу C 1x3: ")
    c = [int(s) for s in input().split()]
    return a, b, c

def stability():
    matrix_tuple = enter_matrix()

    a = matrix_tuple[0]

    alpha_d = -1 * (a[2][2] + a[1][1] + a[0][0])
    betta_d = (a[1][1] * a[2][2] + a[0][0] * a[2][2])
    gamma_d = -1 * (a[0][0] * a[2][2] * a[1][1] - a[0][2] * a[1][0] * a[2][1] - a[0][1] * a[1][2] * a[2][0])

    if alpha_d > 0 and betta_d > 0 and gamma_d > 0:
        print("Система устойчива")
    else:
        print("Система неустойчива")

stability()
