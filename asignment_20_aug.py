SAMPLE_RECORDS = [
    ("Student A", 82, 90),
    ("Student B", 45, 38),
    ("Student C", 65, 72),
]

def compute_average(mark1, mark2, bonus=0):
    # TODO: add mark1, mark2, and bonus, divide by 2, and round to 2 decimal places
    total = mark1 + mark2 + bonus
    average = total / 2
    return round(average, 2)    
    

def compute_grade(average):
    # TODO: map the average to a letter grade using the boundaries above
    grade = ""

    if 40 > average >= 0:
        grade = "F"
    elif 50 > average:
        grade = "D"
    elif 60 > average:
        grade = "C"
    elif 70 > average:
        grade = "B"
    elif 80 > average:
        grade = "A"
    else:
        grade = "First Class"

    return grade
    

def evaluate_students(records, bonus=0):
    # TODO: loop over records, call compute_average and compute_grade for each,
    # and build a list of {"name": ..., "average": ..., "grade": ...} dictionaries

    results = []

    for record in records:
        name, mark1, mark2 = record

        average = compute_average(mark1, mark2, bonus)
        grade = compute_grade(average)

        students_result = {
            "Name": name,
            "Average": average,
            "Grade": grade
        }

        results.append(students_result)

    sorted_results = sorted(
    results,
    key=lambda student: student["Average"],
    reverse=True
)

    for rank, student in enumerate(sorted_results, start=1):
        student["Rank"] = rank

    return sorted_results

if __name__ == "__main__":
  
    sorted_results = evaluate_students(SAMPLE_RECORDS)

    for record in sorted_results:
        print(record)

