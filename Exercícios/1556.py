def find_all_sequences(sequence, answers, letters, n_letters, i):
    if i == n_letters:
        answers.add(sequence)
    else:
        extended = sequence + letters[i]
        if extended not in answers:
            find_all_sequences(extended, answers, letters, n_letters, i +  1)

        find_all_sequences(sequence, answers, letters, n_letters, i + 1)


while True:
    try:
        letters = list(input())
        answers, n_letters = set(), len(letters)

        find_all_sequences('', answers, letters, n_letters, 0)
        answers.remove('')

        for i in sorted(answers):
            print(i)
        print()

    except EOFError:
        break