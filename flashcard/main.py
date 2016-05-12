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


def main():
    args = docopt(__doc__, version='flash 0.0.1')
    print(args)

if __name__ == '__main__':
    main()
