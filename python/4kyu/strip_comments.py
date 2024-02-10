#!/usr/bin/python3


# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
def strip_comments(strng, markers):
    lines = strng.splitlines()
    returnfeed = []
    for line in lines:
        currentline = line
        for marker in markers:
            currentline = currentline.split(marker)[0].rstrip()
        returnfeed.append(currentline)
    return "\n".join(returnfeed)
