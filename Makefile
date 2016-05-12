.PHONY: clean build

clean: 
	rm -rf build
	rm -rf dist
	rm -rf flashcard.egg-info

build:
	python setup.py install
