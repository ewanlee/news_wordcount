import sys

def map():
	for line in sys.stdin:
	    words = line.strip().split()
	    for word in words:
	        value = 1
	        print "%s\t%d" % (word, value)

if __name__ == '__main__':
    map()
