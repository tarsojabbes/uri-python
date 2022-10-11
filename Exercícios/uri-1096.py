cont = 1
repeated_cont = 7

for i in range(1, 16):
    print(f"I={cont} J={repeated_cont}")
    
    repeated_cont -= 1
    if i % 3 == 0:
        cont += 2
        repeated_cont = 7
