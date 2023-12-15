import sys
from slownie import slownie

if __name__ == "__main__":
    print(sys.argv)
    n = int(sys.argv[1])
    print(slownie(n))
