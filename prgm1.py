import sys
fp = open(sys.argv[1])
data=fp.read()
words=data.split()
print("no of word",len(words))