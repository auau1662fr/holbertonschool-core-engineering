#!/usr/bin/env python3
result = "".join(c for c in "abcdefghijklmnopqrstuvwxyz" if c not in "qe")
print("{}".format(result), end="")
