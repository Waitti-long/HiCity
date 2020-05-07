import sys


def read(file):
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
    for i in lines:
        i = i.replace("\n", "")
        i = i.replace("==", ">=")
        print("\"" + i + "\"", end=",")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error: need argv: file")
    else:
        read(sys.argv[1])
