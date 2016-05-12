.PHONY: clean build

clean: 
	rm -rf build
	rm -rf dist
	rm -rf flashcard.egg-info

build:
	python setup.py install

test:
    python -m unittest -v flashcard/tests/*.py

install_requirements:
    pip install -r requirements.txt