# Tests

## urltest.py
This is to make sure that no wonky url's freak the website out.

To test on the website run `python3 urltest.py localhost:1337 blns.txt`
It will tack each line of the text file on to the end of the url and try to connect to it.

It ignores lines that start with "#".

Feel free to change the website and file.
