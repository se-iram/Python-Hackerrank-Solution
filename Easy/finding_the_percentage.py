# =============== solution of problem ====================
def studen_average(student_marks, query_name):
    for key, value in student_marks.items():
        if key == query_name:
            average_score = sum(value) / len(value)
            print('{:.2f}'.format(average_score))


# ============= concepts need to understand to solve this problem ==========

# creating a dictionary 
my_dic = {
            'iram': [67, 68, 69],
            'kiran': [70, 89, 63],
            'junaid': [52, 34, 12]
          }

# for loop on dictionary
for key in my_dic.keys():
    print(key)      #accessing keys

for value in my_dic.values():
    print(value)   #accessing values

for key, value in my_dic.items():
    print(key, value)   #accessing both keys & values

# floating point number with two decimal places

# {:.2f} this is a formating string --- means we want to round and display the number with 2 decimal places.

# .format(average_score): This method inserts the value of average_score into the {:.2f} placeholder and formats it accordingly


