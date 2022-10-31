days = int(input())

age = days // 365
months = days % 365 // 30
rest_days = days % 365 % 30

print(f"{age} ano(s)\n{months} mes(es)\n{rest_days} dia(s)")
