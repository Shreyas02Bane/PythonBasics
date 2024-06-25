"""
Python provides a built-in Range function
Actually range does not create a sequence of integers
It creates a generator which creates integer in sequence

Range object is immutable
Indexing and Slicing can also be applied to range object

range(n) = 0,1,....,n-1
range(m,n) = m,m+1,....,n-1
range(m,n,p) = m,m+p,m+2p,....,n-p
"""

x = range(5)

print(x)
print(type(x))
print(x[4])