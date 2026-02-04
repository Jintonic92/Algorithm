# from collections import Count 
all_list = []
grade_num = {'A+' : 4.5
            , 'A0' : 4.0
            , 'B+' : 3.5
            , 'B0' : 3.0
            , 'C+' : 2.5 
            , 'C0' : 2.0
            , 'D+' : 1.5
            , 'D0' : 1.0 
            , 'F' : 0.0 
             }
for _ in range(20):
  course, credit, grade = input().split() 
  if grade == 'P':
    continue
  all_list.append([float(credit), grade_num[grade]]) # float처리 에러 방지 

numerator = 0.0
denominator = 0.0

for idx in range(len(all_list)):
  # print(all_list[idx][0] * all_list[idx][1])
  numerator += all_list[idx][0] * all_list[idx][1]
  denominator += all_list[idx][0]

print(f"{numerator/denominator:.6f}")
