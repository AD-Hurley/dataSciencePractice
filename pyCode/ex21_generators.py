def squares():
    a = 1
    while True:
        yield a**2
        a+=1

for i in squares():
    print(i)
    if i > 100:
        break
