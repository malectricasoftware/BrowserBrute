import lib.brute
import lib.parse
import lib.banner

args=lib.parse.parser()
lib.banner.banner()

lib.brute.brute(args)