from functools import reduce

answer = -1

def find_max_and(and_value, size, values, min_size, i):
    global answer

    if (size < min_size) and (i < len(values)):
        new_and_value = and_value & values[i]

        if new_and_value > answer:
            find_max_and(and_value, size, values, min_size, i + 1),
            find_max_and(new_and_value, size + 1, values, min_size, i + 1)
        else:
            find_max_and(and_value, size, values, min_size, i + 1)

    if (size == min_size) and (and_value > answer):
        answer = and_value


n_tests = int(input())

for i in range(n_tests):
    n_values, min_size = list(map(int, input().split()))
    values = list(map(int, input().split()))

    values.sort(reverse=True)

    answer = reduce(lambda x, y: x & y, values[0 : min_size])
    find_max_and(-1, 0, values, min_size, 0)

    print(answer)