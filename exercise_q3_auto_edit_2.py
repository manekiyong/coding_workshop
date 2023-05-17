import sys
import re

def process_lines(line):
    sline = line.strip()
    if not re.match(r'^\s*//.*[;{]\s*$', line):
        print(line)

def main():
    count = 0
    for i, line in enumerate(sys.stdin):
        process_lines(line.replace("\n", ""))
        
if __name__ == "__main__":
    main()