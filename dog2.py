tC = int(input())
for t in range(tC):
    n,k = [int(i) for i in input().split()]
    dogs = set()
    diffs = []
    for j in range(n):
        dogs.add(int(input()))

    dogs = sorted(list(dogs))
    for j in range(len(dogs)-1):
        diffs.append(dogs[j+1] - dogs[j])

    diffs = sorted(diffs)
    dogs = list(dogs)
    if k == 1:
        print(dogs[-1] - dogs[0])
    else:
        print(sum(diffs[:len(dogs)-k]))