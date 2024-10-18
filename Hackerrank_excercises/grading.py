def gradingStudents(grades):
    grades_count = len(grades)

    for i in grades:
        return i + 5 - i % 5 if i % 5 >=3 and i >= 38 else i
    
    # for i in range(grades_count):
        # if grades[i] > 37:
        #     n=1
        #     new_grade = grades[i]
        #     while n <3:
        #         if new_grade %5 != 0:
        #             new_grade += 1
        #             n+=1
        #         elif new_grade % 5 == 0:
        #             grades[i] == new_grade
        #             return grades[i]
        #         else:
        #             return grades[i]
        #     print(grades[i])
        #     if new_grade - grades[i] < 3 and new_grade %5 == 0:
        #         grades[i] = new_grade
        #     else:
        #         return grades[i]
        # else:
        #     return grades[i]
        # print(grades[i])
        # if grades[i] > 37:
        #     pass
        # else:
        #     pass
        # return [(i+5-i% 5 if i% 5 >= 3 and i >= 38 else i) for i in grades]
        
        # if grades[i] % 5 >= 2 and grades[i] > 37:
        #     return grades[i]+5 - grades[i]% 5

        


            
        
    
grades = [73, 67, 38, 33]

print(gradingStudents(grades))