from collections import deque

#decimal to binary
n = 33
bin = deque()

while(n >= 1):
    bin.appendleft(n%2)
    n = n//2
for i in bin:
    print(i, end="")
    
print()

#OR
n = 33
b = ""
while n > 0:
    b = str(n % 2) + b
    n //= 2
print(b)
