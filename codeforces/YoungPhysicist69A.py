# youngphysicist.py
t = input()
x,y,z = 0,0,0

for _ in range(int(t)):
   lst = list(map(int,input().split(" ")))
   x += lst[0]
   y += lst[1]
   z += lst[2]

print("YES" if x==0 and y==0 and z==0 else "NO")
