def printnames(i,n):
  if(i>n):
    return
  print("Clutch")
  return printnames(i+1,n)
  
  
printnames(1,3)


def print1ton(i,n):
  if i<1:
    return
  print(i, end =" ")
  return print1ton(i-1,n)



print1ton(int(input("enter  the number")),int(input("enter the number"))) 
  
  
n = int(input("enter the number to print "))

for i in range(1,n+1):
  print(i , end =" ")
  
  
  
def printnames(i,n):
  if(i<1):
    return
  printnames(i-1,n)
  print(i, end=" ")

printnames(4,4)