import csv
import sys
import os

def load_csv_data():
    filename = input("Enter CSV file name (grades.csv): ")

    if not os.path.exists(filename):
        print("Error: File '{0}' not found.".format(filename))
        sys.exit(1)

    assignments = []

    try:
         with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                    })
            return assignments
    except Exception as e:
        print("Error detected while reading: {0}".format(e))
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")

# Grade Validation

    for item in data:
         if not (0 <= item['score'] <= 100):
             print("Invalid score for {0}: {1}".format(item['assignment'], item['score']))
             sys.exit(1)
    print("All score valid (0-100).")
 
# Weight Validation

    total_weight = sum(item['weight'] for item in data)
    formative_weight = sum(item['weight'] for item in data if item['group'] == 'Formative')
    summative_weight = sum(item['weight'] for item in data if item['group'] == 'Summative')

    if total_weight != 100:
         print("Invalid total weight: {0} (must be 100)".format(total_weight))
         sys.exit(1)
    if formative_weight != 60:
         print("Invalid formative weight: {0} (must be 60)".format(formative_weight))
         sys.exit(1)
    if summative_weight != 40:
         print("Invalid summative weight: {0} (must be 40)".format(summative_weight))
         sys.exit(1)

    print("Weights are valid: Total=100, Formative=60, Summative=40.")

# GPA Calculation

    formative_score = sum(item['score'] * item['weight'] / 100 for item in data if item['group'] == 'Formative')
    summative_score = sum(item['score'] * item['weight'] / 100 for item in data if item['group'] == 'Summative')

    total_grade = formative_score + summative_score
    gpa = (total_grade / 100) * 5.0

    print("Formative Score: {0:.2f}/60".format(formative_score))
    print("Summative Score: {0:.2f}/40".format(summative_score))
    print("Total Grade: {0:.2f}/100".format(total_grade))
    print("GPA: {0:.2f}/5.0".format(gpa))

# Final Decision (Pass/Fail)

    formative_percent = (formative_score / formative_weight) * 100
    summative_percent = (summative_score / summative_weight) * 100

    print("Formative %: {0:.2f}%".format(formative_percent))
    print("Summative %: {0:.2f}%".format(summative_percent))

    if formative_percent >= 50 and summative_percent >= 50:
         status = "PASSED"
    else:
         status = "FAILED"

    print("\nFinal Status: {0}".format(status))

# Resubmission Logic

    failed_formatives = [item for item in data if item['group'] == 'Formative' and item['score'] < 50]

    resubmission_list = []
    if failed_formatives:
         highest_weight = failed_formatives[0]['weight']
         for item in failed_formatives:
             if item['weight'] > highest_weight:
                  highest_weight = item['weight']

         resubmission_list = [item for item in failed_formatives if item['weight'] == highest_weight]

    print("\n--- Resubmissions ---")
    if resubmission_list:
            print("Eligible for resubmission (highest weight among failed formatives):")
            for item in resubmission_list:
                 print(" -  {0} (Score: {1}, Weight: {2})".format(item['assignment'], item['score'], item['weight']))
    else:
        print("No resumission needed.")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
