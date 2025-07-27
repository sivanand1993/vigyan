# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
s = [2, 1, 3, 5, 2, 5, 7, 78, 9, 9, 5, 53, 32, 2, 3, 5, 6778, 8]
print(len(s))
L = [s[0]]
for i in range(len(s) - 1):
    print(L)
    if s[i + 1] >= L[0]:
        L.insert(0, s[i + 1])
    elif s[i + 1] <= L[-1]:
        L.append(s[i + 1])
    else:
        l, r = 1, len(L) - 2
        while l < r:
            if s[i + 1] >= L[l]:
                L.insert(l, s[i + 1])
                break
            elif s[i + 1] <= L[r]:
                L.insert(r + 1, s[i + 1])
                break
            l = l + 1
            r = r - 1
s.sort(reverse=True)
print(L)



