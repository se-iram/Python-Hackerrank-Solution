#is where you prepare your tools
def sort_students(names_scores):
    grades = [student[1] for student in names_scores]
    sorted_grades = sorted(set(grades))
    if len(sorted_grades) >= 2:
        second_lowest = sorted_grades[1]
    else:
        second_lowest = sorted_grades[0]
    names_second_lowest = [student[0] for student in names_scores if student[1] == second_lowest]               
    names_second_lowest = (sorted(names_second_lowest))
    for name in names_second_lowest:
        print(name) 
    

# Execution 
if __name__ == '__main__':
    names_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores.append([name, score])
    
    #use your tool
    sort_students(names_scores)