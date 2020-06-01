#pseudocode
#sortAndCount(arr A, length n)
# if n = 1 return 0
# else 
#   x = sortAndCount([A:n/2], n/2)
#   y = sortAndCount(A[n/2:], n/2)
#   z = mergeAndCountSplit(a,n)
# return x+y+z
invCount = 0

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
  #add logic if left != right
  count, i, j = 0;
  while(i<len(left) or j<len(right)):
    if(left[i] > right[i]):
      a[i] = left[i]
    else: 
      a[i] = right[i]
    return count

a = [6,5,4,3,2,1]
sortAndCount(a)