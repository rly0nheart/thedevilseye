# thedevilseye

An osint tool that uses Ahmia.fi to get hidden Tor services and descriptions that match with the users query.

![Screenshot from 2024-07-27 17-16-00](https://github.com/user-attachments/assets/1b177134-0381-4bc5-8f42-3375e3cbd8d2)

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
usage: thedevilseye [-h] [-e EXPORT] [-v] query

thedevilseye — by Richard Mwewa | https://gravatar.com/rly0nheart

positional arguments:
  query                 search query

options:
  -h, --help            show this help message and exit
  -e EXPORT, --export EXPORT
                        a comma-separated list of file types to export the output to (supported: csv,html,json,xml)
  -v, --version         show program's version number and exit

An OSINT tool that uses Ahmia.fi to get hidden Tor services and descriptions that match with the user's query.
```
