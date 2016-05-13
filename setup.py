from setuptools import setup, find_packages

setup(
    name='flashcard',
    version="0.0.2",
    description='Simple flashcard in your terminal.',
    author='sotetsuk',
    url='https://github.com/sotetsuk/flashcard',
    author_email='sotetsu.koyamada@gmail.com',
    license='MIT',
    install_requires=["docopt>=0.6.2", "requests>=2.10.0"],
    packages=find_packages(),
    entry_points={
        'console_scripts': 'flashcard = flashcard.main:main'
    },
    classifiers=[
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License"
    ],
    test_suite='test'
)
