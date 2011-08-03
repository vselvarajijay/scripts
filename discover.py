#!/usr/bin/python
#A file system search tool with Regular expressions

import argparse, os


def discover(path, query):
        pass
def discover(path, query, outputFile):
	output = open(outputFile,'w')
       	for(path, dirs, files) in os.walk(path):
		path = path.split('/')
		if query in path[len(path)-1]:
			output.write("/".join(path+['\n']))
		for file in files:
			if query in file:
				output.write("/".join(path+[file]+['\n']))


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Search file system')
	parser.add_argument('path', help='Folder to search')
	parser.add_argument('query', help='Search filter')
	parser.add_argument('-o','--output', help='Output the parsed results')
	
	args = parser.parse_args()
	
	path = args.path
	output = args.output
	query = args.query

	if output <> 'None':
		discover(path, query, output)
	else:
		discover(path, query) 
	
	
