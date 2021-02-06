# 1
number1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in number1:
    print("    [", i, "]")
    for j in number2:
        print(i, " * ", j, " : ", i * j)
    print("----------------")
# 2
i = 2
while i <= 12:
    num = 1
    print("    [", i, "]")
    while num <= 12:
        print(i, " * ", num, ": ", i * num)
        num += 1
    print("-------------")
    i += 1


# 3
score = int(input("Enter your score:"))
if score <= 100 and score >= 0:
    if score >= 80 and score <= 100:
        print("grade: A")
    elif score >= 75 and score <= 79:
        print("grade: B+")
    elif score >= 70 and score <= 74:
        print("grade: B")
    elif score >= 65 and score <= 69:
        print("grade: c+")
    elif score >= 60 and score <= 64:
        print("grade: c")
    elif score >= 55 and score <= 59:
        print("grade: D+")
    elif score >= 50 and score <= 54:
        print("grade: D")
    else:
        print("grade: F")
else:
    print("sorry grade 0 - 100")
