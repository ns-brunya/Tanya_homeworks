grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=list(students)
print(type(grades[1]))
print(grades[1])
print(type(students))
AverageGrades=[]
for i in grades:
    Igrade_len=len(i)
    Igrade_sum=sum(i)
    Average=Igrade_sum/Igrade_len
    AverageGrades.append(Average)
    Answer = dict(zip(students, AverageGrades))
print(Answer)

