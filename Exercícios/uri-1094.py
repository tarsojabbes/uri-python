number_of_experiments = int(input())
times = 0
quantity_rabbits = 0
quantity_mices = 0
quantity_frogs = 0


while times < number_of_experiments:
    data = input().split()
    if data[1] == 'C':
        quantity_rabbits += int(data[0])
    elif data[1] == 'S':
        quantity_frogs += int(data[0])
    elif data[1] == 'R':
        quantity_mices += int(data[0])
    times += 1

total = quantity_frogs + quantity_mices + quantity_rabbits

percentage_rabbits = (quantity_rabbits/total)*100
percentage_mices = (quantity_mices/total)*100
percentage_frogs = (quantity_frogs/total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {quantity_rabbits}')
print(f'Total de ratos: {quantity_mices}')
print(f'Total de sapos: {quantity_frogs}')
print(f'Percentual de coelhos: {percentage_rabbits:.2f} %')
print(f'Percentual de ratos: {percentage_mices:.2f} %')
print(f'Percentual de sapos: {percentage_frogs:.2f} %')
