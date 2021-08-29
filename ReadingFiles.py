# Lendo arquivos como se eles fossem uma sequência de linhas
arquivo = open('texto.txt')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)

# Contando o numero de caracteres do arquivo
inp = arquivo.read()
print("Tamanho", len(inp))
