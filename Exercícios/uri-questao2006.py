tea_type = int(input())
answers = input().split(' ')

correct_answers = 0

for i in range(len(answers)):
    if (int(answers[i]) == tea_type):
        correct_answers += 1
        
print(correct_answers)
