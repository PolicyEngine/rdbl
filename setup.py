from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='rdbl',
    version='0.1.0',
    author='Nikhil Woodruff',
    author_email='nikhil.woodruff@outlook.com',
    packages=['rdbl'],
    scripts=[],
    url='https://github.com/nikhilwoodruff/rdbl',
    license='',
    description='A lightweight package to format numbers for readability.',
    long_description=long_description,
    install_requires=[],
)