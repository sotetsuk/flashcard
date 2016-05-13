.PHONY: clean build test

clean: 
	rm -rf build
	rm -rf dist
	rm -rf flashcard.egg-info

build:
	python setup.py install

test:
	python -m unittest -v flashcard/tests/*.py

pypi:
	python setup.py register
	python setup.py sdist bdist bdist_egg upload
