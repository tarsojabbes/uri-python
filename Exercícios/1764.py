def find_set(item, sets):
    if sets[item] != item:
        sets[item] = find_set(sets[item], sets)

    return sets[item]


def join_sets(item1, item2, sets):
    set1, set2 = find_set(item1, sets), find_set(item2, sets)

    if set1 != set2:
        sets[set2] = set1


while True:
    n_cities, n_roads = map(int, input().split())
    if (n_cities + n_roads) == 0:
        break

    roads = []
    for i in range(n_roads):
        city1, city2, distance = map(int, input().split())
        roads.append((distance, city1, city2))

    city_sets = [i for i in range(n_cities)]
    roads = sorted(roads, reverse=True)

    total_distance = 0
    while roads:
        distance, city1, city2 = roads.pop()
        set1 = find_set(city1, city_sets)
        set2 = find_set(city2, city_sets)

        if (set1 != set2):
            join_sets(city1, city2, city_sets)
            total_distance += distance

    print(total_distance)