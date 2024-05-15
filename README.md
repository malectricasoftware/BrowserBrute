# BrowserBrute
Online bruteforcing tool based on selenium

# useage
## brute mode
```
usage: browserbrute.py brute [-h] -b {chrome,firefox} -u URL -un USERNAME -uf USERFIELD -pf
                             PASSWORDFIELD [-fn FORMNUMBER] [-btn BUTTON] -wl WORDLIST -tu
                             TARGETURL [-mp] [-pn PRESETNAME]

options:
  -h, --help            show this help message and exit
  -b {chrome,firefox}, --browser {chrome,firefox}
  -u URL, --url URL
  -un USERNAME, --username USERNAME
  -uf USERFIELD, --userfield USERFIELD
  -pf PASSWORDFIELD, --passwordfield PASSWORDFIELD
  -fn FORMNUMBER, --formnumber FORMNUMBER
  -btn BUTTON, --button BUTTON
  -wl WORDLIST, --wordlist WORDLIST
  -tu TARGETURL, --targeturl TARGETURL
  -mp, --makepreset
  -pn PRESETNAME, --presetname PRESETNAME
```
 
## preset mode 
```
usage: browserbrute.py preset [-h] -pn PRESETNAME -un USERNAME -wl WORDLIST

options:
  -h, --help            show this help message and exit
  -pn PRESETNAME, --presetname PRESETNAME
  -un USERNAME, --username USERNAME
  -wl WORDLIST, --wordlist WORDLIST
``` 
