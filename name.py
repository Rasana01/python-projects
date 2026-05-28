import sys

if len(sys.argv) < 2:
    sys.exit("too few argumments")
    
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)