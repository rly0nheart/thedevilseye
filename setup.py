import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="thedevilseye",
    version="2022.1.5.1",
    author="Richard Mwewa",
    author_email="rly0nheart@duck.com",
    packages=["thedevilseye"],
    description="Darkweb osint tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rly0nheart/thedevilseye",
    license="GNU General Public License v3 (GPLv3)",
    install_requires=["rich", "selenium"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
        ],
    entry_points={
        "console_scripts": [
            "thedevilseye=thedevilseye.main:main",
        ]
    },
)
