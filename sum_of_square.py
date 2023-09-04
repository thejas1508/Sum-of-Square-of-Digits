#SUM OF SQUARE OF DIGITS
Storage = 0
anumber = int(input("Enter the Number:"))
while anumber > 0:
  Remainder = anumber % 10
  Storage = Storage + Remainder**2
  anumber = anumber // 10 
print(Storage)
