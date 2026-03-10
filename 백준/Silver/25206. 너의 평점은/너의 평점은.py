grade_list = {"A+" : 4.5 , "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, 'D+' : 1.5, "D0" : 1.0, "F" : 0.0}

a_list = []
for _ in range(20):
  course, credit, grade = input().split()
  if grade == 'P':
    continue
  
  a_list.append([float(credit), float(grade_list[grade])])

sum_cred = 0.0
sum_grad = 0.0

for cred, grad in a_list:
  sum_grad += cred * grad
  sum_cred += cred

print(f"{sum_grad/sum_cred:.6f}")