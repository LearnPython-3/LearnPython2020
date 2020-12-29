a = [1,2,3,4,5,6,7,8,9,10]

for i in a:
    print(i)

b = 0
while b < 10:
    b += 1

for i in a:
    if b >= 16:
        break
    b += i

print(b)
