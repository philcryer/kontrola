import fnmatch
import os

images = ['*.j2', '*.md', '*.txt']
matches = []

for root, dirnames, filenames in os.walk("/home/pccryer1/devel"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))
