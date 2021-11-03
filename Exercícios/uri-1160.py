test_cases = int(input())

while test_cases > 0:
    data = input().split()
    population_a, population_b, growth_a, growth_b = data

    population_a = int(population_a)
    population_b = int(population_b)
    growth_a = float(growth_a)
    growth_b = float(growth_b)
    years = 0

    while (population_a <= population_b):
        current_population_a = int(population_a * (growth_a/100))
        current_population_b = int(population_b * (growth_b/100))
        population_a += current_population_a
        population_b += current_population_b
        years += 1

        if years > 100:
            break

    if years > 100:
        print("Mais de 1 seculo.")
    else:
        print(f'{years} anos.')

    test_cases -= 1
