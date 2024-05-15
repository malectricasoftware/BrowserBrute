import argparse
def parser():
	parser = argparse.ArgumentParser(description="browser brute args")
	subparse=parser.add_subparsers(dest="command")

	npparser=subparse.add_parser("brute")
	npparser.add_argument("-b","--browser",required=True, choices=["chrome","firefox"])
	npparser.add_argument("-u","--url",required=True)
	npparser.add_argument("-un","--username",required=True)
	npparser.add_argument("-uf","--userfield",required=True)
	npparser.add_argument("-pf","--passwordfield",required=True)
	npparser.add_argument("-fn","--formnumber",required=True)
	npparser.add_argument("-wl","--wordlist",required=True)
	npparser.add_argument("-tu","--targeturl")
	npparser.add_argument("-mp","--makepreset",action="store_true")
	npparser.add_argument("-pn","--presetname")

	pparser=subparse.add_parser("preset")
	pparser.add_argument("-pn","--presetname",required=True)
	pparser.add_argument("-un","--username",required=True)
	pparser.add_argument("-wl","--wordlist",required=True)

	args = parser.parse_args()
	return args