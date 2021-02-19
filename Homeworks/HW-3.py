def prime_first(f):
   sum=0
   for x in range(2,f):
    if f%x==0:
     sum+=1
   if sum==0:
    return (f)
   else:
     return (" ") 
def prime_second(s):
   sum=0
   for x in range(2,s):
    if s%x==0:
     sum+=1
   if sum==0:
    return (s)
   else:
     return (" ")       

for i in range(2,1000):
  if i<=500:
    first=prime_first(i)
    print(first)
  if i>500:
    second=prime_second(i)
    print(second)  
