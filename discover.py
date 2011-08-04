#!/usr/bin/python
#A file system search tool with Regular expressions

import argparse, os, re


def discoverFile(path, fileName, comparer):
	if comparer(fileName):
		print "/".join(path+[fileName])

def discover(path, query, comparer):
	for(path, dirs, files) in os.walk(path):
		path = path.split('/')
		if comparer(path[len(path)-1]):
			print "/".join(path)

		df = lambda x: discoverFile(path,x,comparer)	
		map(df,files) 

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Search file system')
	parser.add_argument('path', help='Folder to search')
	parser.add_argument('query', help='Search filter')
	args = parser.parse_args()

	comparer = lambda x: re.search(re.compile(args.query), x)

	discover(args.path, args.query, comparer)
	
