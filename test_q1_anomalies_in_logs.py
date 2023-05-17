import sys

logged_in = {}
for i, line in enumerate(sys.stdin, start=1):
    line = line.strip()
    activity, person, time = line.split()

    if activity=='logout':
        if person not in logged_in:
            print(i, line)
            continue
        else:
            logged_in.pop(person)
    if activity=='login':
        if person in logged_in:
            print(i, line)
            continue
        else:
            logged_in[person]=time