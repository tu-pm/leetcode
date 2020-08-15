def atoi(str):
    start, end = -1, len(str) + 1
    for i in range(len(str)):
        if str[i].isspace():
            continue
        if str[i].isdigit() or str[i] == '-' or str[i] == '+':
            start = i
        break

    if start == -1:
        return 0

    for j in range(start+1, len(str)):
        if not str[j].isdigit():
            end = j
            break

    try:
        val = int(str[start:end])
        val = max(val, -2 << 30)
        val = min(val, (2 << 30) - 1)
        return val
    except:
        return 0

x = atoi("  -123")
print(x)
