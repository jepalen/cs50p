import argparse

parser = argparse.ArgumentParser(description="Wowf like a dog")
parser.add_argument("-n",help="Number of times to wowf", type=int, default=1)
parser.add_argument("-s", help="Speed of dog", type=int, default=1)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("wowf")

for _ in range(int(args.s)):
    print("more speed!!", end=" ")
    