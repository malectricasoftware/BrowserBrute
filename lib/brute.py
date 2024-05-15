from selenium import webdriver
from selenium.webdriver.common.by import By
import lib.presets
import time

def brute(args):
	if args.command == "preset":
		args=lib.presets.load_preset(args)

	if args.browser == "firefox":
		driver = webdriver.Firefox()
	else:
		driver = webdriver.Chrome()
	if args.command == "brute":
		if args.makepreset:
				lib.presets.make_preset(args.presetname,args.browser,str(args.url),args.userfield,args.passwordfield,args.formnumber,args.targeturl)

	with open(args.wordlist,"r") as wlist:

		for line in wlist:
			driver.get(args.url)
			ufield=driver.find_element(By.CSS_SELECTOR, f'[name="{args.userfield}"]')
			ufield.send_keys(args.username)
			pfield=driver.find_element(By.CSS_SELECTOR, f'[name="{args.passwordfield}"]')
			pfield.send_keys(line.replace("\n",""))
			forms=driver.find_elements(By.TAG_NAME,"form")
			form=forms[int(args.formnumber)]
			form.submit()
			time.sleep(1)
			if driver.current_url.startswith(args.targeturl):
				print(f"{args.username} : {line}")
				break
