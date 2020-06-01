#pseudocode
#sortAndCount(arr A, length n)
# if n = 1 return 0
# else 
#   x = sortAndCount([A:n/2], n/2)
#   y = sortAndCount(A[n/2:], n/2)
#   z = mergeAndCountSplit(a,n)
# return x+y+z
def sortAndCount(a):
  n = len(a)
  left = a[:n//2]
  right = a[n//2:]
  if(n==1):
    return 0;
  else:
    x = sortAndCount(left)
    y = sortAndCount(right)
    z = mergeAndCountSplit(a, left, right)
    return x+y+z;


def mergeAndCountSplit(a, left, right):
  #add logic if left len != right len
  count = 0
  i = 0
  j = 0
  k=0
  while(i<len(left) and j<len(right)):
    if(left[i] < right[j]):
      a[k] = left[i]
      i+=1
      k+=1
    if(left[i] > right[j]): 
      a[k] = right[j]
      count+=len(left)-i
      j+=1
      k+=1
  if(a[k-1] == left[i-1]):
    while(k<len(a)):
      a[k] = right[j]
      k+=1
      j+=1
  if(a[k-1] == right[j-1]):
    while(k<len(a)):
      a[k] = left[i]
      k+=1
      i+=1
  return count

a = [8,7,6,5,4,3,2,1]
print(sortAndCount(a))
print(a)