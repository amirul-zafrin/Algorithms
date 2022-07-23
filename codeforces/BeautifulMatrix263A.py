x = 0
y = 0

for _ in range(5):
    x += 1
    inp = input()
    if "1" in inp:
        lst = list(map(int, inp.split(" ")))
        y = lst.index(1)
        break

print(abs(x - 3) + abs(y - 2))

        

