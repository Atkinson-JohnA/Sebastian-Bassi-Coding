import sys
import argparse



msg = """What this program does XXXXXXX""" 

parser = argparse.ArgumentParser(msg)
parser.add_argument('-o', '--Outfile', help='Ouput file', required=True)
parser.add_argument('-i', '--Inputfile', dest='var2', help='Input file', required=True)

args = parser.parse_args()

def split_by_chromosome(x):
    print(x)
    return None


if __name__ == "__main__":
    split_by_chromosome(args.var2)
    sys.exit(0)
	
