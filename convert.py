#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description='Decode HEX String')
parser.add_argument('string', metavar='string',type=str,nargs=1, help='red value in decimal')
args = vars(parser.parse_args())
print(args['string'][0])
print("".join([chr(int(x,16)) for x in args['string'][0].split()]))
