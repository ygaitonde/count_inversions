#pseudocode
#sortAndCount(arr A, length n)
# if n = 1 return 0
# else 
#   x = sortAndCount(A[:n/2], n/2)
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
    z = mergeAndCountSplit(left, right)
    return x+y+z;


def mergeAndCountSplit(left, right):
  return 0;

a = [6,5,4,3,2,1]
print(sortAndCount(a))