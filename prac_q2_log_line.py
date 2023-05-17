from sys import stdin
import re

def clean_lines(lines):
    results = []
    multiline = ""
    startline = None

    for index, line in enumerate(lines, start=1):
        parsed_line = line.strip().split("//")[0]
        if "logger.debug" in line and ";" not in parsed_line:
            multiline += parsed_line
            startline = index
            continue
        if multiline:
            multiline += parsed_line
            results.append((startline, multiline))
            multiline = ""
        elif "logger.debug" in parsed_line:
            results.append((index, parsed_line))
    return results

data = clean_lines([line for line in stdin])
for lineNum, line in data:
    pattern = r'\((.*)\)'
    match = re.search(pattern, line)

    if match:
        pattern2 = r'(["\'])(?:(?=(\\?))\2.)*?\1'
        new_string = re.sub(pattern2, '', match.group(1))
        if "() ->" in new_string:
            continue
        if "()" in new_string or "+" in new_string:
            print(lineNum)