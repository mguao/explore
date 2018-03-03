#!/usr/bin/env python

#import the argparse module
import argparse
import sys

def processServer(server):
    ''' define a function to process a single argument given'''
    print server

def processFile(file):
    ''' define a function to handle a list in a file'''
    f = file.readlines()
    for i in f:
        print i.strip()


def main():
    ''' create the parse object '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="input file", type=argparse.FileType('r'))
    parser.add_argument("-s", "--server", help="FQDN of the server")
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.file:
        processFile(args.file)

    if args.server:
        processServer(args.server)

if __name__ == "__main__":
    main()

