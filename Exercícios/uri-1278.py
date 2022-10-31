result = ""

while True:
    n = int(input())
    if n == 0:
        break
    if result != "":
        result += "\n\n"

    word_list=[" ".join(input().split()) for i in range(n)]
    
    longest = len(word_list[0])
    for word in word_list:
        if len(word) > longest:
            longest = len(word)

    for i in range(len(word_list)):
        word_list[i] = f"{word_list[i]: >{longest}}"

    result += "\n".join(word_list)

print(result)
