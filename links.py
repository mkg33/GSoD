#!/usr/bin/python

'''A simple script for inserting links to the SVG tree.
Works on a premise that the tree boxes never equal rgb(0%,0%,0%).
Insert filenames as needed (two files: a list with hyperlinks and the SVG file).
Prepare the hyperlinks in a hierarchical manner (i.e., according to the box hierarchy).
For instance, if you have 3 category boxes, the links will be inserted from left to right.
And for subcategories, they will be inserted top to bottom.
See the sample_links.svg file with number markings (1-33).'''

import re, sys

pattern=re.compile('rgb\([^0]')

hyperlink='<a class=\"reference internal\" href=\"\">'

hyperlink_path=input('Enter the hyperlink path: ')

svg_path=input('Enter the SVG path: ')

try:
    with open(hyperlink_path, 'r') as hyper_input:
        hyper_file=hyper_input.readlines()
except OSError as e:
    print('Something went wrong: %s\nexiting...' % e.strerror)
    sys.exit()
else:
    hyper_input.close()

try:
    with open(hyperlink_path, 'w') as hyper_output:
        for line in hyper_file:
            if not line.startswith('--'):
                line=hyperlink[:36] + line[0:len(line)-1] + hyperlink[36:] + '\n'
                hyper_output.write(line)
            else:
                hyper_output.write(line)
except OSError as e:
    print('Something went wrong: %s\nexiting...' % e.strerror)
    sys.exit()
else:
    hyper_output.close()

try:
    with open(svg_path, 'r') as input_file, open(hyperlink_path, 'r') as hyper_input:
        svg_file=input_file.readlines()
        hyper_file=hyper_input.readlines()
except OSError as e:
    print('Something went wrong: %s\nexiting...' % e.strerror)
    sys.exit()
else:
    input_file.close()
    hyper_input.close()

try:
    with open(svg_path, 'w') as output_file:
        counter = 0
        for line in svg_file:
            if pattern.search(line):
                if hyper_file[counter][0:2]!="--":
                    line=hyper_file[counter]+line+'</a>'+'\n'
                print(line)
                counter += 1
            output_file.write(line)
except OSError as e:
    print('Something went wrong: %s\nexiting...' % e.strerror)
    sys.exit()
else:
    print('Success!')
    output_file.close()
