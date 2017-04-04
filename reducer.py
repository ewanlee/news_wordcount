import sys
from itertools import groupby

def fromstdin():
    for line in sys.stdin:
        word, count = line.rstrip('\n').split('\t')
        yield (word, count)

def reduce():
    for word, group in groupby(self.fromstdin(), key=lambda x: x[0]):
        count = sum([1 for i in group])
        print '%s\t%s' % (word, str(count))


if __name__ == '__main__':
    reduce()
