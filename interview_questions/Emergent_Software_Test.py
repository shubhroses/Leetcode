def version_compare(version1, version2):
    v1 = version1.split(".")
    v2 = version2.split(".")

    n = len(v1)
    m = len(v2)

    v1 = [int(i) for i in v1]
    v2 = [int(i) for i in v2]

    if n > m:
        for i in range(m, n):
            v2.append(0)
    elif m > n:
        for i in range(n, m):
            v1.append(0)
        
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            return 1
        elif v2[i] > v1[i]:
            return -1
    return 0

version1 = "1.0.3"
version2 = "1.0.3"

print(version_compare(version1, version2))