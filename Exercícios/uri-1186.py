def solve(mat, op):
    res = 0
    count = 0
    for i in range(11, -1, -1):
        for j in range(12):
            if 11 - i < j:
                count += 1
                res += mat[i][j]
    return res if op == 'S' else res / count
            

def main():
    op = input()
    mat = [[float(input()) for j in range(12)] for i in range(12)]
    ans = solve(mat, op)
    print(f"{ans:.1f}")


if __name__ == "__main__":
    main()

