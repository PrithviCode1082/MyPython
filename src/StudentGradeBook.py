students = {
    "Max": [56, 78, 91, 64],
    "Chloe": [92, 88, 95, 91],
    "Dustin": [40, 52, 35, 48],
    "Eleven": [100, 100, 99, 100],
    "Lucas": [75, 82, 79, 85],
    "Nancy": [89, 91, 87, 90],
    "Steve": [62, 55, 70, 68],
    "Robin": [94, 92, 96, 93],
    "Will": [77, 72, 80, 74],
    "Jonathan": [68, 70, 65, 72]
}

def getGrade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B+'
    elif avg >= 60:
        return 'B'
    elif avg >= 50:
        return 'C'
    return 'F'
    

def getNewReports():
    topperName = ""
    topperAvg = 0
    topperGrade = ''
    for k, v in students.items():
        avg = sum(v) / len(v)
        grade = getGrade(avg)
        if avg > topperAvg:
            topperName = k
            topperAvg = avg
            topperGrade = grade
    print(f"{topperName} is First! Avg: {topperAvg} with {topperGrade} Grade!")

def addStudent():
    studentName = input("Enter the student's name: ")
    scores = [0, 0, 0, 0]
    for i in range(0, 4):
        scores[i] = int(input(f"Enter the score of Subject {i+1}: "))
    
    students[studentName] = scores

getNewReports()

