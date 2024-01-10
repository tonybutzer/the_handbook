import sys

print(sys.argv[1])
infile = sys.argv[1]

r = open(infile, "r")
f= open("a.dot","w+")

f.write("digraph G {\n")
cnt=0
for line in r:
    n = "n%s" % cnt
    wline = line.rstrip()
    wline = n + "[label=\"" + str(wline) + "\"]\n"
    f.write(wline)
    cnt = cnt + 1

f.write("}\n")
