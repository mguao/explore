import argparse

def processServer(server):
    print server

def processFile(file):
    f = file.readlines()
    for i in f:
        print i.strip()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="input file", type=argparse.FileType('r'))
    parser.add_argument("-s", "--server", help="FQDN of the server")
    args = parser.parse_args()

    if args.file:
        processFile(args.file)

    if args.server:
        processServer(args.server)

if __name__ == "__main__":
    main()

