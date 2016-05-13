[![Build Status](https://travis-ci.org/sotetsuk/flashcard.svg?branch=master)](https://travis-ci.org/sotetsuk/flashcard)
[![Coverage Status](https://coveralls.io/repos/github/sotetsuk/flashcard/badge.svg?branch=master)](https://coveralls.io/github/sotetsuk/flashcard?branch=master)
[![python3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://github.com/sotetsuk/flashcard)
[![PyPI version](https://badge.fury.io/py/flashcard.svg)](https://badge.fury.io/py/flashcard)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](https://github.com/sotetsuk/flashcard)

# flashcard
Simple flashcard in your terminal

## Example

### 1. Prepare flashcard in Google Spreadsheet: [example](https://docs.google.com/spreadsheets/d/1X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g/edit?usp=sharing)

<img src="./img/spreadsheet.png" width="400px">

### 2. Copy the url and learn the flashcard!

```sh
$ flashcard --hint 0.5 https://docs.google.com/spreadsheets/d/1X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g/edit?usp=sharing
```


<img src="./img/example.png" width="600px">

## Features

- Making flashcard from (shared) Google Spreadsheet
- Colorful diff feedback
- Hinting option for begginers

## Requirements

- Python 3.5 or later
- docopt
- requests

## Installing

```sh
$ pip install flashcard
```


### Building
You can build from source codes: 

```sh
$ make build
```

## License
MIT License
