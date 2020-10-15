#!/Users/tony/anaconda3/bin/python3


n = 10
L = [i for i in range(n)]

print(L)

A = []

# for e in L:
#     A.append(e*2)

A = [e * 2 for e in L]

print(L)
print(A)