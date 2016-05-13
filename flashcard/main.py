# -*- coding: utf-8 -*-

"""Simple flashcard in your terminal

Usage:
  flashcard <flashcard>
  flashcard (-h | --help)
  flashcard --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt

from flashcard.property import Flashcard
from flashcard.sources import fetch_google_spreadsheet


def run(flashcard: Flashcard):
    for i, card in enumerate(flashcard):
        assert len(card), "This flashcard is invalid: expect 2 columns but get {} at line {}".format(len(card), i)

    n = len(flashcard)
    num_collect = 0
    for i, card in enumerate(flashcard):
        problem = card[0]
        expected = card[1]

        print("{:03d}".format(i + 1), problem)
        ans = input(">>> ")

        if expected == ans.strip():
            num_collect += 1
            print('[o]', expected)
        else:
            print('[x]', expected)

    print("{}/{}".format(num_collect, n))


def main():
    args = docopt(__doc__, version='flashcard 0.0.2')
    if args['<flashcard>'].startswith("https://docs.google.com/spreadsheets/"):
        flashcard = fetch_google_spreadsheet(args['<flashcard>'])
    else:
        print("<flashcard> should be URL of Google Spreadsheet (other sources are TBA)")
        exit(1)

    run(flashcard)

if __name__ == '__main__':
    main()
