# twinespacer
A python script that uses graphviz to layout a Twine 2 story into something ideally nice looking.
This is by no means a perfect system and something well worth fiddling about, especially with the layout engine and `spacing` variable in the python script

## Use

`python twinespacer.py originalTwineStory newTwineStory layoutStyle`

The layout style is optional, and matches the engines from graphviz, will default to the dot engine if none is provided.

**back up your twine files before using this program, I am a bad python programmer and may destroy your story**

## Installation

- Python 2.7 (3 should be fine though)
- BeautifulSoup: `pip install beautifulsoup4`
- graphviz: (on macOS the easiest way is to use brew, no idea on anything else)
- graphviz python library: `pip install graphviz`

Once you've got all these installed, running the script should work
