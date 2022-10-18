def eh_ma_sorte(num):
    for i in range(len(num) - 1):
        if num[i] == '1' and num[i + 1] == '3':
            return f'{num} es de Mala Suerte'

    return f'{num} NO es de Mala Suerte'


num = input()
print(eh_ma_sorte(num))
