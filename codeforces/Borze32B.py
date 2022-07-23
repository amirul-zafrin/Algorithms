inp = input()
code = {"--": "2", "-.": "1", ".": "0"}
for k, v in code.items():
    inp = inp.replace(k, v)

print(inp)
