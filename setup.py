from setuptools import setup, find_packages

setup(
    name='flashcard',
    version='0.0.1',
    description='Simple flashcard in your terminal.',
    author='sotetsuk',
    install_requires=['docopt'],
    packages=find_packages(),
    entry_points={
        'console_scripts': 'flashcard = flashcard.main:main'
    }
)
