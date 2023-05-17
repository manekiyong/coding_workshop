import sys

def normalize_angle(angle):
    while angle < 0:
        angle += 360
    while angle >= 360:
        angle -= 360
    return angle

def sector_check(A, B, C):
    A = normalize_angle(A)
    B = normalize_angle(B)
    C = normalize_angle(C)
    if B == C:
        return "TRUE"

    if B < C:
        if A >= B and A <=C:
            return "TRUE"
        else:
            return "FALSE"
    else:
        if A >= B or A <= C:
            return "TRUE"
        else:
            return "FALSE"
        
def main():
    count = 0
    for i, line in enumerate(sys.stdin):
        line = line.strip()
        count+=1
        if count == 1000000:
            return
        A, B, C = map(int, line.split())
        print(sector_check(A, B, C))
    return
        
if __name__ == "__main__":
    main()