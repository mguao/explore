#!/usr/bin/env python

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

def processMultiple(listofservers):
    for server in listofservers:
        print server


def main():
    ''' create the parse object '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="input file", type=argparse.FileType('r'))
    parser.add_argument("-s", "--server", help="FQDN of the server")
    parser.add_argument("-m", "--multiple", nargs='+', help="multiple servers, space delim")
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.file:
        processFile(args.file)

    if args.server:
        processServer(args.server)
    
    if args.multiple:
        processMultiple(args.multiple)

if __name__ == "__main__":
    main()

