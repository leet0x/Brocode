'''Using a dictionary to represent an instructor's grade book'''
grade_book = {"Susan": [92, 85, 100],
              "Eduardo": [83, 95, 79],
              "Azizi": [91, 89, 82],
              "Pantipa": [97, 91, 92]}
all_class_grades = []
for name, grades in grade_book.items():
    print(f"Average for {name} is {sum(grades) / len(grades):.2f}")
    all_class_grades.append(sum(grades) / len(grades))

print(f"{sum(all_class_grades) / len(grade_book):.2f}")