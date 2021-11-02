![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/thedevilseye?ystyle=flat)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/thedevilseye/badge)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/thedevilseye)
![PyPI](https://img.shields.io/pypi/v/thedevilseye)
[![Downloads](https://static.pepy.tech/personalized-badge/thedevilseye?period=total&units=international_system&left_color=black&right_color=orange&left_text=pypi+downloads)](https://pepy.tech/project/thedevilseye)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/thedevilseye)

**The Devil's Eye**

*Darkweb OSINT tool, that extracts information (.onion links, descriptions) from the darkweb without requiring a Tor network*

> **Note**: *Tor* is not required to use this tool.

# Installation & Usage
**Clone from Github**:
```
git clone https://github.com/rlyonheart/thedevilseye.git
```

```
cd thedevilseye
```

```
pip install -r requirements
```

```
python devilseye QUERY
```

**Install from Pypi**:
```
pip install thedevilseye
```

```
devilseye QUERY
```

**Update to latest version**:
```
python -m pip install --upgrade thedevilseye
```


# Optional Arguments
| Flag           | Or            |MetaVar|                 Usage|
| ------------- |:-------------:|:----------------------:|:---------:|
| <code>-o</code>      | <code>--outfile</code>      |   **FILENAME** |  *write output to a specified file*  |
| <code>-p</code> | <code>--page</code>  |  **NUMBER**  |  *page number. default is 1*  |
| <code>-r</code> | <code>--raw</code>  |    |  *return output in raw json format*  |
| <code>-v</code> | <code>--verbosity</code>  |    |  *run thedevilseye in verbose mode*  |


> **Note**: If your search query contains spaces, put it inside " " symbols.

# About author
* [About.me](https://about.me/rlyonheart)

# Contact author
* [Github](https://github.com/rlyonheart)

* [Twitter](https://twitter.com/rly0nheart)

