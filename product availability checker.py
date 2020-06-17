# Program to check availability of product on shopping sites 
# Note delete the print function to not print the availability of the product because it does not matter

import requests
from bs4 import BeautifulSoup
import time
import webbrowser

def checkavailability(website_name , url):
	'''
	in case you want to use headers enter the user-agent of your web browser (as a string 
	in headers dictionary, as a value for key User-Agent below) which you can get by searching on google from your browser 
	and add headers=headers argument in requests.get function below
	'''	
	headers= { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97'}
	page = requests.get (url, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	if website_name=='amazon':
		avail = soup.find(id="priceblock_ourprice")
		if avail != None :
			print ("product is available")

			webbrowser.open(url)

		else :
			print ("product is not available")

	elif website_name=='flipkart':
		avail = soup.find(id="pincodeInputId")
		if avail != None :

			print ("product is available")
			
			webbrowser.open(url)
	
		else :
			print ("product is not available")
'''
 to call checkavailability function pass two argument first with 
 website name (like 'amazon'and 'filpkart') and second with the url of the product 
'''
while True :
	checkavailability('amazon','https://www.amazon.in/boAt-Rockerz-380-Headphones-Integrated/dp/B07TTN6HNL#:~:text=boAt%20Rockerz%20380%20Wireless%20Bluetooth%20Headphones%20with%20HD%20Sound%2C%2040mm,of%205%20stars%20570%20ratings')
	time.sleep(60)
	checkavailability('flipkart','https://www.flipkart.com/intex-infrared-digital-thermometer-thermo-safe/p/itm68dc16da057a1?pid=DTHFS8YJ4EYYDHMF&lid=LSTDTHFS8YJ4EYYDHMFLMKWLY&marketplace=FLIPKART&srno=b_1_3&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_3_3.dealCard.OMU_Deals%2Bof%2Bthe%2BDay_L35Z828DL637_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_3_NA_view-all_2&fm=neo%2Fmerchandising&iid=610046c1-824f-4284-8df5-f1c740cfa78f.DTHFS8YJ4EYYDHMF.SEARCH&ppt=browse&ppn=browse&ssid=l3qae10k340000001592327381425')
	time.sleep(60)  
