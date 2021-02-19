names=[]
for i in range(5):
  names.append(input("Enter name and surname: "))
grades=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in range(5):
  for j in range(1):
    grades[i][j]=float(input("Enter student's midterm grade: "))
    grades[i][j+1]=float(input("Enter student's final grade: "))
    grades[i][j+2]=float(input("Enter student's homework grade: "))
info={}
for i in range(5):
  info[names[i]]=grades[i]    
print("Information of grades",info)

averages=[]
for i in range(5):
  for j in range(1):
   averages.append((info[names[i]][j]+  info[names[i]][j+1]+  info[names[i]][j+2])/3)   

avg_info={}
for i in range(5):
  avg_info[names[i]]=averages[i]
print ("Students' averages" ,avg_info)
avg_sort=sorted(avg_info.values())
print("Order of averages: ",avg_sort)
score=(max(avg_sort))
for k,v in avg_info.items():
 if v == score:
   print("Congratulations!! You have the highest average :" + k)
