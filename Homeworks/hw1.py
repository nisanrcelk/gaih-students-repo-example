import random
matrix=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
 for j in range(3):
  check=False
  while (check==False):
   sum=0
   number =random.randint(2,100)
   for x in range(2,number):
    if number%x==0:
     sum+=1
    if sum==0:
     matrix[i][j]=number
     check=True
    else: 
      check=False
for i in range(3):
  print(matrix[i])     