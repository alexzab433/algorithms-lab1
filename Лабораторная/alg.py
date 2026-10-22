def binary_search(arr,target,lo,hi):
    end=hi
    while lo<hi:
        mid=(lo+hi)//2
        if arr[mid]<target:
            lo=mid+1
        else:
            hi=mid
    if lo==end:
        return -1
    return lo
def two_pointers(a,b):
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            i+=1
        elif a[i]>b[j]:
            j+=1
        else:
            return True
    return False
def binary(a,b):
    if len(a)>len(b):
        a,b=b,a
    for x in a:
        pos=binary_search(b,x,0,len(b))
        if pos==-1:
            return False
        if b[pos]==x:
            return True
    return False
def exp(a,b):
    if len(a)>len(b):
        a,b=b,a
    n=len(b)
    j=0
    for x in a:
        step=1
        while j+step<n and b[j+step]<x:
            step*=2
        lo=j+step//2
        hi=min(j+step+1,n)
        j=binary_search(b,x,lo,hi)
        if j==-1:
            return False
        if b[j]==x:
            return True
    return False
def double_binary(a,b):
    if len(a)>len(b):
        a,b=b,a
    def rec(alo,ahi,blo,bhi):
        if alo>=ahi or blo>=bhi:
            return False
        mid=(alo+ahi)//2
        x=a[mid]
        pos=binary_search(b,x,blo,bhi)
        if pos==-1:
            pos=bhi
        if pos<bhi and b[pos]==x:
            return True
        return rec(alo,mid,blo,pos) or rec(mid+1,ahi,pos,bhi)
    return rec(0,len(a),0,len(b))
