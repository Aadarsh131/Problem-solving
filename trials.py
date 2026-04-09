def f(x,lst=[]):
    lst.append(x)
    return lst
  
print(f(1),f(2,[]), f(3))
print(f(2), f(3))