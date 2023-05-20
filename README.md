
An osint tool that uses Ahmia.fi to get Tor hidden services and descriptions that match with the users query.

![2023-05-20_01-12](https://github.com/rly0nheart/thedevilseye/assets/74001397/dca2fc47-7ed2-4402-ae3b-b49cfdda6cb9)

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![GitHub](https://img.shields.io/github/license/rly0nheart/thedevilseye?style=flat&logo=github)
![PyPI](https://img.shields.io/pypi/v/thedevilseye?style=flat&logo=pypi)
[![Downloads](https://static.pepy.tech/personalized-badge/thedevilseye?period=total&units=international_system&left_color=black&right_color=orange&left_text=pypi+downloads&logo=pypi)](https://pepy.tech/project/thedevilseye)
![GitHub repo size](https://img.shields.io/github/repo-size/rly0nheart/thedevilseye?style=flat&logo=github)
[![Upload Python Package](https://github.com/rly0nheart/thedevilseye/actions/workflows/python-publish.yml/badge.svg)](https://github.com/rly0nheart/thedevilseye/actions/workflows/python-publish.yml)


# Installation
## Github
```
pip install git+https://github.com/rly0nheart/thedevilseye
```
## PyPI
```
pip install thedevilseye
```
# Usage
```
thedevilseye --help
```
```
usage: thedevilseye [-h] [-c COUNT] [-d] query

thedevilseye — by Richard Mwewa | https://about.me/rly0nheart

positional arguments:
  query                 search query

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        number of results to return (default 10)
  -d, --debug           enable debug mode

thedevilseye is an osint tool that uses Ahmia.fi to get Tor hidden services and descriptions that match with the user's query.
```
