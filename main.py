n = int(input("Enter the range: "))
num =1
for i in range(n):
  for j in range(i):
    print(num,end="")
    num += 1
  print()