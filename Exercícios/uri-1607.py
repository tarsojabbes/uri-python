def solve(string1, string2):
    count = 0 
    for c1, c2 in zip(string1, string2):
        x, y = ord(c1), ord(c2)
        if x <= y:
            count += y - x 
        else:
            count += ord('z') - x + 1 + y - ord('a')
    return count


def main():
    t = int(input())
    
    while t:
        a, b = input().split()
        print(solve(a, b))
        t -= 1


if __name__ == "__main__":
    main()

