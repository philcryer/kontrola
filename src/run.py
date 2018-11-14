#!/usr/bin/env python

import re

shakes = open("wssnt10.txt", "r")

for line in shakes:
    if re.match("(.*)(L|l)ove(.*)", line):
        print line,
