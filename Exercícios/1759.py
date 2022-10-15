r = int(input())
ho = ""

for i in range(0, r, 1):
    if (ho == ""):
        ho = "Ho"
    else:
        ho += " Ho"

if (ho != ""):
    ho += "!"
    
print(ho)