a = int(input("What is a?"))
b = int(input("What is b?"))
c = int(input("What is c?"))
d = int(input("What is d?"))


def readfile2(filename): return open(filename, 'rt').read()


sentence = readfile2("rosalind_ini3.txt")

print(sentence[a:(b + 1)], sentence[c:(d + 1)])

# solution from u/axelwilhelm
infile = open('rosalind_ini3.txt')
string1 = infile.readline()
string2 = infile.readline()
string2 = string2.split(' ')
a = int(string2[0])
b = int(string2[1])
c = int(string2[2])
d = int(string2[3])
print(string1[a:b + 1], string1[c:d + 1])
