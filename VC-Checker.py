from requests import post
print("""
██╗   ██╗ ██████╗               ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║   ██║██╔════╝              ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║   ██║██║         █████╗    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
╚██╗ ██╔╝██║         ╚════╝    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
 ╚████╔╝ ╚██████╗              ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
  ╚═══╝   ╚═════╝               ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     

                           By @TweakPY - @vv1ck
""")
card_number=input("[?] Enter Card Number : ")#'5313640057574778'
cvc=input("[?] Enter cvc : ")#'853'
exp_month=input("[?] Enter exp month : ")#'11'
exp_year=input("[?] Enter exp year : ")#'24'==2024 
r=post("https://api.stripe.com/v1/tokens",headers={'Host': 'api.stripe.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://js.stripe.com/v3/controller-862a80dbaa554971d8cf5c0ce836dc66.html','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://js.stripe.com','Content-Length': '358','Te': 'trailers'},data=f'card[number]={card_number}&card[cvc]={cvc}&card[exp_month]={exp_month}&card[exp_year]={exp_year}&key=pk_live_sq77vLTlEPpJkEH9xXlzk5dx00ZYPskAJn')
if 'Your card number is incorrect.' in r.text:print("[!] this Card is Fake , Card number is incorrect !")
elif 'The card number is not a valid credit card number.' in r.text:print("[!] this Card is Fake , Card Number is not valid !")
elif "Your card is not supported." in r.text:print("[!] this Card is unknown , Card is not supported -!")
elif "Your card's security code is invalid." in r.text:print("[!] this Card is Fake , Card security code is invalid !")    
elif "invalid_expiry_month" in r.text:print("[!] this Card is Fake , Card expiration month is invalid !")
elif "invalid_expiry_year" in r.text:print("[!] this Card is Fake , Card expiration year is invalid !")
elif 'invalid_number' in r.text:
	try:ermsg=r.json()['error']['message']
	except:ermsg='unknown'
	print("[!] invalid data !!")
	print(f"[!] Error: {ermsg}")
elif 'brand' in r.text:
	rj=r.json()['card'];rjc=r.json()
	print(f'''
{'-'*30}
[-/+] May be Live - useable\n
[+] Card Brand: [{rj['brand']}]
[+] Country: [{rj['country']}]
[+] security code check: [{rj['cvc_check']}]
[+] client ip: [{rjc['client_ip']}]
[+] used: [{rjc['used']}]''')
else:
	try:ermsg=r.json()['error']['message']
	except:ermsg='unknown'
	print(f'[!] Error : {ermsg}')

## checker is based on stripe api if the api fucked up , thats not from me . ##