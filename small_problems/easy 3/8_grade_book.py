def get_grade(score1, score2, score3):
    scores = [score1, score2, score3]
    average = sum(scores) / 3
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80: 
        return 'C'
    elif 60 <= average < 70: 
        return 'D'
    else:
        return 'F' 

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True