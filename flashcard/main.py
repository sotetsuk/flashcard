# -*- coding: utf-8 -*-

"""Simple flashcard in your terminal

Usage:
  flashcard [--hint=<hint_rate>] <flashcard>
  flashcard (-h | --help)
  flashcard --version

Options:
  --hint=<hint_rate>    Show hint. p = 1 will show every character and p=0 will hide all.
  -h --help             Show this screen.
  --version             Show version.
"""

from typing import Tuple
from termcolor import colored
import difflib
from random import random

from docopt import docopt

from flashcard.property import Flashcard
from flashcard.sources import fetch_google_spreadsheet


def run(flashcard: Flashcard, hint_rate=None):
    for i, card in enumerate(flashcard):
        assert len(card), "This flashcard is invalid: expect 2 columns but get {} at line {}".format(len(card), i)

    n = len(flashcard)
    num_collect = 0
    for i, card in enumerate(flashcard):
        problem = card[0]
        expected = card[1]

        print("# {:02d}".format(i + 1), problem)

        if hint_rate is not None:
            print(colored("hint", "blue"), hint(expected, hint_rate))

        ans = input(">>>> ")

        if expected == ans.strip():
            num_collect += 1
            print(colored('GOOD', 'green'), colored(expected, "green"))
        else:
            expected_with_mistake, ans_with_mistake = get_diff_with_color(expected, ans)
            print(colored('MISS', 'red'), expected_with_mistake)
            print('    ', ans_with_mistake)

        print("*" * 100)

    print("{}/{}".format(num_collect, n))


def get_diff_with_color(expected: str, ans: str) -> Tuple[str, str]:
    d = difflib.Differ()
    diff = d.compare(expected, ans)

    expected_with_mistake = ""
    ans_with_mistake = ""
    for e in diff:
        if e.startswith("+"):
            ans_with_mistake += colored(e[-1], "red")
        elif e.startswith("-"):
            expected_with_mistake += colored(e[-1], "green")
        else:
            expected_with_mistake += e[-1]
            ans_with_mistake += e[-1]

    return expected_with_mistake, ans_with_mistake


def hint(expected: str, hint_rate=0.5) -> str:
    ret = ""
    for c in expected:
        if c == " ":
            ret += c
        elif random() > hint_rate:
            ret += "*"
        else:
            ret += c

    return ret


def main():
    args = docopt(__doc__, version='flashcard 0.0.3')
    if args['<flashcard>'].startswith("https://docs.google.com/spreadsheets/"):
        flashcard = fetch_google_spreadsheet(args['<flashcard>'])
    else:
        print("<flashcard> should be URL of Google Spreadsheet (other sources are TBA)")
        exit(1)

    hint_rate = None
    if args['--hint'] is not None:
        hint_rate = float(args['--hint'])
        assert 0.0 <= hint_rate <= 1.0, "hint rate should satisfy 0.0 <= hint_rate <= 1.0"

    run(flashcard, hint_rate)

if __name__ == '__main__':
    main()
