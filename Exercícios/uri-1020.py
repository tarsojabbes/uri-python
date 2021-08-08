integer = int(input())

years = 0
months = 0
days = 0
lefting = 0

if integer >= 365:
    years += int(integer/365)
    lefting = lefting + integer % 365
    if lefting >= 30:
        months += int(lefting/30 - ((lefting % 30)/30))
        lefting = lefting % 30
    if lefting < 30:
        days += lefting
else:
    months += int(integer/30)
    lefting += integer % 30
    if lefting < 30:
        days += int(lefting)

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')
