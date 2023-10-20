objects = [1, 2, 1, 2, 3]
ans = 0
matches = 0
for i in range(len(objects)):
    for j in range(i + 1, len(objects)):
        if objects[j] is objects[i]:
            matches += 1
    if matches == 0:
        ans += 1
    matches = 0
print(ans)