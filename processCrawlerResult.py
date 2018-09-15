import os.path
from collections import namedtuple

UNIXPerm = namedtuple('UNIXPerm', ('perms', 'user', 'group'))

def readInCrawlResult(filename):
    if not os.path.exists(filename): return 
    directories = {}
    f = open(filename, 'r')
    for line in f.readlines():
    	line = line.strip('\n')
    	path, perm, user, group = line.split('\t')
    	directories[path] = UNIXPerm(perm, user, group)
    return directories

if __name__ == '__main__':
	print readInCrawlResult('/Users/manw/Documents/Projects/OSCrawler/DownloadsCrawl.txt')