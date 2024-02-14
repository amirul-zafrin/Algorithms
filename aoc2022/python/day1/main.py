import heapq

def top_3_max(inp: str):
    heap = []
    heapq.heapify(heap)
    with open(inp, 'r') as f:
        s = 0
        for line in f:
            if line == "\n":
                heap.append(s)
                s = 0
            else:
                s += int(line)
    heap.append(s)
    return heapq.nlargest(3, heap)

if __name__ == "__main__":
    top3 = top_3_max("input.txt")
    print(f"NO1: {top3[0]}")
    print(f"TOP3: {top3}")
