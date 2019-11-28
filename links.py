#!/usr/bin/python

'''A simple script for inserting links to the SVG tree.
Works on a premise that the tree boxes never equal rgb(0%,0%,0%).
Insert filenames as needed (two files: a list with hyperlinks and the SVG file).
No error handling, so use with care.'''

import re

pattern=re.compile("rgb\([^0]")

hyperlink="<a xlink:href=\"\">"

with open('hyper.txt', 'r') as hyper_input:
    hyper_file=hyper_input.readlines()

with open('hyper.txt', 'w') as hyper_output:
    for line in hyper_file:
        line=hyperlink[:15] + line[0:len(line)-1] + hyperlink[15:] + '\n'
        hyper_output.write(line)

with open('testing/scipy.org/www/constants.svg', 'r') as input_file, open('hyper.txt', 'r') as hyper_input:
    svg_file=input_file.readlines()
    hyper_file=hyper_input.readlines()

with open('testing/scipy.org/www/constants.svg', 'w') as output_file:
    counter = 0
    for line in svg_file:
        if pattern.search(line):
            line=hyper_file[counter]+line+'</a>'+'\n'
            print(line)
            counter += 1
        output_file.write(line)
