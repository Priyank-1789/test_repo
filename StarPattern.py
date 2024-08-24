"""#1 SQUARE PATTERN

n = int(input("enter number of rows :"))
for i in range(0,n):
  for j in range(0,n):
     print("*",end=" ")
  print()


# 2 LEFT TRIANGLE STAR PATTERN

n = int(input("enter number of rows :"))
for i in range(0,n):
   for j in range(0,i+1):
      print("*",end=" ")
   print()


# 3 LEFT DOWNWARD TRIANGLE PATTEN

n = int(input("enter number of rows: "))
for i in range(0,n):
   for j in range(i,n):
      print("*",end=" ")
   print()


# 4 RIGHT TRIANGLE STAR PATTERN


n = int(input("enter number of rows: "))
for i in range(0,n):
   for j in range(i,n-1):
      print(" ",end=" ")
   for j in range(0,i+1):
      print("*",end=" ")
   print()


# 5 RIGHT DOWNWARD TRIANGLE STAR PATTERN

n = int(input("enter number of rows: "))
for i in range(0,n):
   for j in range(0,i):
      print(" ",end=" ")
   for j in range(i,n):
      print("*",end=" ")
   print()

# PYRAMID

n = int(input("enter number of rows: "))
for i in range(0,n):
   for j in range(i,n-1):
      print(" ",end=" ")
   for j in range(0,i+1):
      print("*",end=" ")
   for j in range(0,i):
      print("*",end=" ")
   print()


# 7 REVERSE PYRAMID

n = int(input("enter number of rows: "))
for i in range(0,n):
   for j in range(0,i):
      print(" ",end=" ")
   for j in range(i,n):
      print("*",end=" ")
   for j in range(i,n-1):
      print("*",end=" ")
   print()

# 8 DAIMOND STAR PATTERN

n = int(input("enter number of rows :"))
for i in range(0,n):
   for j in range(i,n-1):
      print(" ",end=" ")
   for j in range(0,i):
      print("*",end=" ")
   for j in range(0,i+1):
      print("*",end=" ")
   print()
for i in range(0,n-1): # note this
   for j in range(0,i+1):
      print(" ",end=" ")
   for j in range(i,n-1):
      print("*",end=" ")
   for j in range(i,n-2):
      print("*",end=" ")
   print()

# 9 HOURGLASS STAR PATTERN

n = int(input("enter number of rows : "))
for i in range(0,n):
   for j in range(0,i):
      print(" ",end=" ")
   for j in range(i,n):
      print("*",end=" ")
   for j in range(i,n-1):
      print("*",end=" ")
   print()
for i in range(0,n-1):
   for j in range(i,n-2):
      print(" ",end=" ")
   for j in range(0,i+1):
      print("*",end=" ")
   for j in range(0,i+2):
      print("*",end=" ")
   print()

# 10 RIGHT PASCAL STAR PATTERN

n = int(input("enter number of rows: "))
for i in range(0,n):
   for j in range(0,i+1):
      print("*",end=" ")
   print()
for i in range(0,n-1):
   for j in range(i,n-1):
      print("*",end=" ")
   print()

# 11 LEFT PASCAL STAR PATTERN

n = int(input("enter the number of rows : "))
for i in range(0,n):
   for j in range(i,n-1):
      print(" ",end=" ")
   for j in range(0,i+1):
      print("*",end=" ")
   print()
for i in range(0,n-1):
   for j in range(0,i+1):
      print(" ",end=" ")
   for j in range(i,n-1):
      print("*",end=" ")
   print()"""


# 12 BUTTERFLY PATTERN
# SEE IT ON REPLIT

n = int(input("enter the number of rows:" ))
for i in range(0,n):
   for j in range(0,i+1):
      print("*",end=" ")
   for j in range(i,n-1):
      print("-",end=" ")
   for j in range(i,n-2):
      print("&",end=" ")
   for j in range(1,i):
      print("*",end=" ")
   print()

