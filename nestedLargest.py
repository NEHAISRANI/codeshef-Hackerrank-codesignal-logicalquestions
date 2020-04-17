a=[[17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10]]
i=0
while i<len(a):
  new1=a[i][0]
  j=1
  while j<len(a[i]):
    if a[i][j]>new1:
      new1=a[i][j]
    j=j+1
  print(new1)
  i=i+1