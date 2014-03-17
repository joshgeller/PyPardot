import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="PyPardot",
    version="0.1",
    author="Josh Geller",
    author_email="joshualgeller@gmail.com",
    description=("API wrapper for Pardot marketing automation software."),
    keywords="pardot",
    url="https://github.com/joshgeller/PyPardot",
    packages=['pypardot', 'pypardot.objects'],
    long_description=read('README.md'),
)