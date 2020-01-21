def zeros(n):
    for i in range(1, n):
        n *= i
    x = str(n)

    return x.count("0")
  
print(zeros(30))