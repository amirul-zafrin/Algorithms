l, t = map(int,input().split(" "))
queue = list(input())

for _ in range(t):
    q = queue.copy()
    for i in range(l-1):
        if queue[i] == "B" and queue[i+1] == "G":
            q[i], q[i+1] = "G","B"
    queue = q

print("".join(queue))
