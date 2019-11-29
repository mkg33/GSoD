#!/usr/bin/python

'''A simple script for inserting links to the SVG tree.
Works on a premise that the tree boxes never equal rgb(0%,0%,0%).
Insert filenames as needed (two files: a list with hyperlinks and the SVG file).
Prepare the hyperlinks in a hierarchical manner (i.e., according to the box hierarchy).
For instance, if you have 3 category boxes, the links will be inserted from left to right.
And for subcategories, they will be inserted top to bottom.
See the sample_links.svg file with number markings (1-33).
No error handling, so use with care.'''

import re

pattern=re.compile("rgb\([^0]")

hyperlink="<a xlink:href=\"\">"

with open('hyper.txt', 'r') as hyper_input:
    hyper_file=hyper_input.readlines()

with open('hyper.txt', 'w') as hyper_output:
    for line in hyper_file:
        if not line.startswith('--'):
            line=hyperlink[:15] + line[0:len(line)-1] + hyperlink[15:] + '\n'
            hyper_output.write(line)
        else:
            hyper_output.write(line)

with open('testing/scipy.org/www/constants.svg', 'r') as input_file, open('hyper.txt', 'r') as hyper_input:
    svg_file=input_file.readlines()
    hyper_file=hyper_input.readlines()

with open('testing/scipy.org/www/constants.svg', 'w') as output_file:
    counter = 0
    for line in svg_file:
        if pattern.search(line):
            if hyper_file[counter][0:2]!="--":
                line=hyper_file[counter]+line+'</a>'+'\n'
            print(line)
            counter += 1
        output_file.write(line)
