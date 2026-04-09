m = 3
n = 2
x = [[0]*n]*m
#a = [0]*2 (list elements are the reference to same object 0) and b = [a]*3 i.e, b = [a,a,a] (a is a reference and is stored for each element instead of the copy)
print(x) #[[0, 0], [0, 0], [0, 0]]

# x[0] = 1 #[1, [0, 0], [0, 0]] #here, assignment will change the reference of x[0] to a new address, but x[1] and x[2] will keep pointing to same mem address

x[0][0] = 1
print(x) #[[1, 0], [1, 0], [1, 0]]