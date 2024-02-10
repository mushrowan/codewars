#!/usr/bin/python3

# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).
#
# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.


def ips_between(start, end):
    return sum(
        [256**i * int(field) for i, field in enumerate(reversed(end.split(".")))]
    ) - sum([256**i * int(field) for i, field in enumerate(reversed(start.split(".")))])
