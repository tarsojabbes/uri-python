# Uri 1245: Botas Perdidas

def main():
    
    while 1:
        
        try:

            n = int(input())
            pares = [[0,0] for _ in range(61)]
            for _ in range(n):
                m, l = input().split()
                i = int(m)

                if l == "E":
                    # Pe esquerdo
                    pares[i][0] += 1
                else:
                    # Pe direito
                    pares[i][1] += 1

            resp = 0
            for p in pares:
                resp += min(p)
            
            print(resp)

        except EOFError:
            break

if __name__ == "__main__":
    main()
