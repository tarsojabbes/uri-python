def my_eval(string):
    idx = string.index('+')
    a = int(string[:idx])
    b = int(string[idx + 1:])

    return a + b


def resolve(entrada):
    if entrada == 'P=NP': return 'skipped'
    else: return my_eval(entrada)


n_entradas = int(input())

for i in range(n_entradas):
    entrada = input()
    print(resolve(entrada))
