def judge(s, r):
    if (s == r):
        return "De novo!"
    elif ((s == "pedra" and r in ["tesoura", "lagarto"]) or (s == "papel" and r in ["pedra", "Spock"]) or (s == "tesoura" and r in ["papel", "lagarto"]) or (s == "lagarto" and r in ["Spock", "papel"]) or (s == "Spock" and r in ["tesoura", "pedra"])):
        return "Bazinga!"
    else:
        return "Raj trapaceou!"

n = int(input())

for i in range(n):
    sheldon, raj = input().split()
    
    result = judge(sheldon, raj)
    print(f"Caso #{i+1}: {result}")