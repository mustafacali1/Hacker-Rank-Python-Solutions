"""
Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers i<n , print i^2.
"""

n = int(input('Please type a number: '))

if 0 <= n:
    for x in range(0,n):
        print(x**2)
else:
    print("The number should be positive..!")