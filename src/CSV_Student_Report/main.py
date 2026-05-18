import csv

def average_calculator(*nums):
    avg = 0
    for num in nums:
        avg += int(num)
    return (avg / 4)

def grader(avg):
    if avg >=90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >=70:
        return "B+"
    elif avg >= 60:
        return "C"
    else:
        return "F"

grades = []
count = 0
with open("student_report.csv", mode='r') as file:
    data = csv.reader(file) 
    for row in data:
        if (count == 0):
            count+=1
            continue
        avg = average_calculator(row[2], row[3], row[4], row[5])
        grades.append({
            "Student_Name" : row[0],
            "Average": avg,
            "Grade": grader(avg)
        })

with open("Grades.csv", mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=grades[0].keys())
    writer.writeheader()
    writer.writerows(grades)

