import sys
import cowsay

if len(sys.argv) < 2:
    sys.exit("Not enough arguments")

for arg in sys.argv[1:]:
    cowsay.cow("hello: " + arg)
