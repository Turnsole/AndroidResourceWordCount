import argparse
import re
import sys

regex = re.compile(r'<string .*>(.*?)<\/string>')

def scrape_line(line):
    matched = re.findall(regex, line)

    if matched is None or len(matched) == 0: 
        return 0
    else: 
        return len(matched[0].split())

def main(sys_args):
    parser = argparse.ArgumentParser(description='Generate word count for an Android string resource file.')
    parser.add_argument('pathToFile', metavar='pathToFile', nargs=1, help='path to file (ex: /user/project/res/values/strings.xml)')
    args = parser.parse_args(sys_args)

    input_file = open(args.pathToFile[0], 'r')
    count_lines = 0
    count_words = 0 
    for line in input_file:
        count_lines += 1
        count_words += scrape_line(line)

    print 'Parsed {} lines and found {:,} words.'.format(count_lines, count_words)

if __name__ == "__main__":
    main(sys.argv[1:]) 
