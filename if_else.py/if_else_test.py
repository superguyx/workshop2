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
