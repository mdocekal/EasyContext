# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages


def is_requirement(line):
    return not (line.strip() == "" or line.strip().startswith("#"))


with open('README.md') as readme_file:
    README = readme_file.read()

with open("requirements.txt") as f:
    REQUIREMENTS = [line.strip() for line in f if is_requirement(line)]


setup_args = dict(
    name='easycontext',
    version='1.0.1',
    description="Memory optimization and training recipes to extrapolate language models' context length to 1 million tokens, with minimal hardware.",
    long_description_content_type="text/markdown",
    long_description=README,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://github.com/jzhang38/EasyContext',
    python_requires='>=3.9',
    install_requires=REQUIREMENTS
)

if __name__ == '__main__':
    setup(**setup_args)
