import sys
args = sys.argv[1:]
f = open('test1.txt','a')
for i in args:
    data = '%s\n' % i
    f.write(data)
f.close()