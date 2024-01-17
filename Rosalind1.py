a = int(input("What is the length of side a?"))
b = int(input("What is the length of side b?"))
c = (a ** 2) + (b ** 2)
print(c)


# solution from u/ArniDexian
def readfile(filename): return open(filename, 'rt').read().split()


vals = readfile('rosalind_ini2.txt')
res = sum(map(lambda a: int(a) ** 2, vals))
print(res)
