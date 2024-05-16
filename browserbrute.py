#imports
import lib.brute
import lib.parse
import lib.banner

#parse arguments
args=lib.parse.parser()

#print banner
lib.banner.banner()

#online bruteforce passing in args
lib.brute.brute(args)
