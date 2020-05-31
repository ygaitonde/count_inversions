#pseudocode
#sortAndCount(arr A, length n)
# if n = 1 return 0
# else 
#   x = sortAndCount(A[:n/2], n/2)
#   y = sortAndCount(A[n/2:], n/2)
#   z = mergeAndCountSplit(a,n)
# return x+y+z

def sortAndCount(a, n):
  if(n==1):
    return 0;
  else:
    x = sortAndCount(a[:n/2], n/2)
    y = sortAndCount(a[n/2:], n/2)
    z = mergeAndCountSplit(a,n)
    return x+y+z;


def mergeAndCountSplit:
  return 0;