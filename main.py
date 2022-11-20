import requests,telebot,random
from telebot import types
from bin import bin,bincc
from sk import check_sk
from gen import gg
from ig import igg
from vipp import addvip
from cchk import cchk
from proxyall import *
from vipp import checkvip
from random_user import geninfo
from mchk import new_func,get_response_mchk
tok = "5404235427:AAE_F_I-OlrinUPtgZG2A9JIfPWRiSptUTw"
bot=telebot.TeleBot(tok)
@bot.message_handler(commands=['start'])
def run(message):
	key = types.InlineKeyboardMarkup()
	b2=types.InlineKeyboardButton(text='help', callback_data='package')
	key.row_width = 1
	key.add(b2)
	first_name = message.from_user.first_name
	bot.send_message(message.chat.id,text=f"<strong>Hi, {first_name}! My name is Brav. Click the Help button below. 👇</strong>",parse_mode='html',reply_markup=key)
@bot.message_handler(func= lambda m: True)
def mess(message):
	user = message.from_user.username
	id = message.from_user.id
	text = message.text
	vip=checkvip(id)
	if '/cly' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/csp' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/cdy' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/cho' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/cso' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/cri' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/cdy' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/aup' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/cyp' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/so' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/bri' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/ad' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/sho' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/str' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/ctr' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	
	if '/cap' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/cpp' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/cp' in text:
		if vip in 'Premium':
			print('Ok')
		else:
			bot.reply_to(message,text=f"<strong>@{user}, this gate is available only for subscribers.</strong>",parse_mode='html')
	if '/socks4' == text:
		se = socks4()
		js = open("socks4.txt","w").write(se)
		jgs = open("socks4.txt","r")
		bot.send_document(message.chat.id,jgs,caption=f"<strong>Type: socks4\nCount: 700\nChecked By @{user} (<code>{id}</code>)\nUser Subscribe => [{vip}]</strong>",parse_mode="html")
	if '/socks5' == text:
		se = socks5()
		js = open("socks5.txt","w").write(se)
		jgs = open("socks5.txt","r")
		bot.send_document(message.chat.id,jgs,caption=f"<strong>Type: socks5\nCount: 700\nChecked By @{user} (<code>{id}</code>)\nUser Subscribe => [{vip}]</strong>",parse_mode="html")
	if '/https' == text:
		se = https()
		js = open("Https.txt","w").write(se)
		jgs = open("Https.txt","r")
		bot.send_document(message.chat.id,jgs,caption=f"<strong>Type: https\nCount: 700\nChecked By @{user} (<code>{id}</code>)\nUser Subscribe => [{vip}]</strong>",parse_mode="html")
	if '/http' == text:
		se = http()
		js = open("Http.txt","w").write(se)
		jgs = open("Http.txt","r")
		bot.send_document(message.chat.id,jgs,caption=f"<strong>Type: http\nCount: 700\nChecked By @{user} (<code>{id}</code>)\nUser Subscribe => [{vip}]</strong>",parse_mode="html")
	if '/addvip' in text:
		if 5384214726 == id:
			idadd = text.split(' ')[1]
			add1 = addvip(idadd)
			bot.reply_to(message,f"<strong>{add1}️</strong>",parse_mode="html")
		else:
			bot.reply_to(message,f"<strong>Your Not Admin Bot️</strong>",parse_mode="html")
	if '/status' in text:
		bot.reply_to(message,"<strong>Online => ✅\nBot: @Pravebotcheckbot ♻️</strong>",parse_mode="html")
	if '/sk' in text or '.sk' in text:
		try:
			sk = text.split(' ')[1]
			send = check_sk(sk,user,id)
			bot.reply_to(message,send,parse_mode="html")
		except:
			bot.reply_to(message,"<strong>Sk Error Format</strong>",parse_mode="html")
	if '/bin' in text or '.bin' in text:
		try:
			bi = text.split(' ')[1]
		except:
			bot.reply_to(message,"<strong>NOT BIN</strong>",parse_mode="html")
		try:
			send= (bin(bi,id,user))
			bot.reply_to(message,send,parse_mode="html")
		except:
			pass
	elif '/gen' in text:
		for i in range(1):
			cc = text.split(' ')[1]
			send = gg(cc,id,user)
			if 'Generator' in send:
				bot.reply_to(message,send,parse_mode="html")
			else:
				pass
		
	elif '/ig' in text or '/infoig' in text:
		usernameig = text.split(' ')[1]
		send = igg(usernameig,id,user)
		bot.reply_to(message,send,parse_mode="html")
	elif '/cch' in text or '/cch' in text:
		card = text.split(' ')[1]
		try:
			chh = cchk(card,id,user)
			bininfo = bincc(card,id,user)
			bot.reply_to(message,f"""
			<strong>
			INPUT: <code>{card}</code>
			Reponse: <code> {chh} </code>	
			Gateway: Stripe Auth  (CH){bininfo}
			</strong>
			""",parse_mode="html")
		except:
			bot.reply_to(message,"<strong>Error Try Again 30ś</strong>",parse_mode="html")
	elif '/fack' in text or '/fackinfo' in text:
		try:
			send = geninfo(id,user)
			bot.reply_to(message,send,parse_mode="html")
		except:
			bot.reply_to(message,"<strong>Error Try Again 30ś</strong>",parse_mode="html")
	elif '/chfree' in text or '/chfree' in text:
		card = text.split(' ')[1]
		bininfo = bincc(card,id,user)
		for i in range(1):
			cc = card.split('|')[0]
			exp=card.split('|')[1]
			try:
				exy=card.split('|')[2].split('0')[1]
			except:
				exy=card.split('|')[2]
			ccv = card.split('|')[3]
			getresonse = new_func(cc,ccv,exp,exy)
			ms1 = (get_response_mchk(getresonse))
			try:
				mess = str(ms1[0]).split('-')[1]
			except:
				mess = ms1[0]
			logo = ms1[1]
			code = ms1[2]
			bot.reply_to(message,f"""
			<strong>
			INPUT: <code>{card}</code>
			Charging Card $Auth
			Result Charge:<code>{logo}</code>
			Reponse: <code> {mess} </code>
			Reponse Code: <code> {code} </code>	
			Gateway: STRIPE Gateway v1 (CH){bininfo}
			</strong>
			""",parse_mode="html")
		
		
	else:
		pass
@bot.callback_query_handler(func=lambda call: True)
def qery(call):
	if call.data == 'package':
	  package(call.message)
	if call.data == 'vip':
	  vip(call.message)
	if call.data == 'start':
	  wordkey(call.message)
	if call.data == '﻿AuthGates':
		autthgates(call.message)
	if call.data == 'Back':
	  back(call.message)
	#---------------gates------------
	if call.data == 'Stripe':
	  Stripe(call.message)
	if call.data == 'Shopify':
	  Shopify(call.message)
	if call.data == 'paypal':
		paypal(call.message)
	if call.data == 'Braintree':
	  Braintree(call.message)
	if call.data == 'Square':
	  Square(call.message)
	if call.data == 'CyberSource':
	  CyberSource(call.message)
	if call.data == 'adyan':
	  paypal(call.message)
	if call.data == 'payseb':
		payseb(call.message)
	if call.data == 'lyra':
	  lyra(call.message)
	
	#-------------charge---------
	if call.data == 'aStripe':
	  aStripe(call.message)
	if call.data == 'aShopify':
	  aShopify(call.message)
	if call.data == 'a3dScuore':
		adScuore(call.message)
	if call.data == 'aBraintree':
	  aBraintree(call.message)
	if call.data == 'aSquare':
	  aSquare(call.message)
	if call.data == 'apaypal':
	  apaypal(call.message)
	if call.data == 'a3dScuore':
		adScuore(call.message)
	if call.data == 'aCyberSource':
	  aCyberSource(call.message)
	if call.data == 'ChargeGates':
	  chragegates(call.message)


def wordkey(message):
	key = types.InlineKeyboardMarkup()
	b3=types.InlineKeyboardButton(text='↩️', callback_data='package')
	key.row_width = 2
	key.add(b3)
	wkey="""
	<strong>
	List Key => Free	
	
	Key => /cch => Check Strip Auth
	
	Key => /chfree => Check Strip Auth
	
	Key => /fack & /fackinfo = Fack Info
	
	Key => /gen Genrate cc with bin
	
	Key => /sk Key Check Sk 
	  
	Key => /bin & .bin Check Bin Info
	
	Key => /ig & /iginfo Get Info Ig
	
	Key => /http proxies  https
	
	Key => /https proxies  https
	
	Key => /socks4 proxies socks4
	
	Key => /socks5 proxies socks5
	
	Key => /status Check Bot Online 
 
	</strong>"""
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=wkey,parse_mode="html",reply_markup=key)
def back(message):
	key = types.InlineKeyboardMarkup()
	b2=types.InlineKeyboardButton(text='help', callback_data='package')
	key.row_width = 1
	key.add(b2)
	mk = message.from_user.id
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"<strong>Hi, Is Barv! My name is Brav. Click the Help button below. 👇</strong>",parse_mode='html',reply_markup=key)

def vip(message):
	id = message.from_user.id
	if 'Premium' in 'Premium':
		key = types.InlineKeyboardMarkup()
		b2=types.InlineKeyboardButton(text='﻿Auth Gates', callback_data='﻿AuthGates')
		b20=types.InlineKeyboardButton(text='Back', callback_data='Back')
		key.row_width = 1
		key.add(b2,b20)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"<strong>Welcome Vip\nYour Vip\nID ({id}) </strong>",parse_mode="html",reply_markup=key)
	else:
		key = types.InlineKeyboardMarkup()
		b2=types.InlineKeyboardButton(text='Back', callback_data='Back')
		key.row_width = 2
		key.add(b2)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>Subscribe Bot Price ⬇️\n\n7Day => 10$\n\n30Day => 30$\n\nSoruce => 250$\n\nSubscibe => @AO_SaLah</strong>",parse_mode="html",reply_markup=key)
def autthgates(message):
	id = message.from_user.id
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='package')
	astrip=types.InlineKeyboardButton(text='Stripe', callback_data='aStripe')
	asho=types.InlineKeyboardButton(text='Shopify', callback_data='aShopify')
	
	aBraintree=types.InlineKeyboardButton(text='Braintree', callback_data='aBraintree')
	aSquare=types.InlineKeyboardButton(text='Square', callback_data='aSquare')
	apaypal=types.InlineKeyboardButton(text='PayPal Pro', callback_data='apaypal')
	aCyberSource=types.InlineKeyboardButton(text='CyberSource', callback_data='aCyberSource')
	key.row_width = 1
	key.add(aBraintree)
	key.row_width = 2
	key.add(asho,apaypal)
	key.row_width = 1
	key.add(aCyberSource)
	key.row_width = 2
	key.add(astrip,aSquare)
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿Auth Gates
↳ only verifies if the card is valid and active, but does not charge it.

Format: [command] XXXXXXXXXXXXXXXX|MM|YYYY|CVV
Example: /ch 4647331155846215|11|2024|630</strong>""",parse_mode="html",reply_markup=key)

def package(message):
	key = types.InlineKeyboardMarkup()
	b2=types.InlineKeyboardButton(text='Auth Gates', callback_data='﻿AuthGates')
	b1=types.InlineKeyboardButton(text='Chrage Gates', callback_data='ChargeGates')
	b0=types.InlineKeyboardButton(text='Free Comands', callback_data='start')
	b00=types.InlineKeyboardButton(text='↩️', callback_data='Back')
	key.row_width = 2
	key.add(b2,b1)
	key.row_width = 1
	key.add(b0)
	key.row_width = 1
	key.add(b00)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>🤖 Bot Status ⇾ Operational ✅
   
To use <a href="https://telegram.dog/Pravebotcheckbot">Brav</a> in your group, you must set it as admin.</strong>""",parse_mode="html",reply_markup=key)
def chragegates(message):
	id = message.from_user.id
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='package')
	strip=types.InlineKeyboardButton(text='Stripe', callback_data='Stripe')
	sho=types.InlineKeyboardButton(text='Shopify', callback_data='Shopify')
	
	Braintree=types.InlineKeyboardButton(text='Braintree', callback_data='Braintree')
	Square=types.InlineKeyboardButton(text='Square', callback_data='Square')
	paypal=types.InlineKeyboardButton(text='PayPal Pro', callback_data='paypal')
	CyberSource=types.InlineKeyboardButton(text='CyberSource', callback_data='CyberSource')
	Adyan=types.InlineKeyboardButton(text='Adyan', callback_data='adyan')
	payseb=types.InlineKeyboardButton(text='payseb', callback_data='payseb')
	lyra=types.InlineKeyboardButton(text='Lyra', callback_data='lyra')
	key.row_width = 1
	key.add(Braintree)
	key.row_width = 2
	key.add(sho,paypal)
	key.row_width = 1
	key.add(CyberSource)
	key.row_width = 2
	key.add(strip,Square)
	key.row_width = 1
	key.add(lyra)
	key.row_width = 2
	key.add(Adyan,payseb)
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿Charge Gates
↳ will charge the card with specific amount.

For custom amount charge, type the amount after the space at the end of the CC.

Example 1: /cst 4647331155846215|11|2024|630
Example 2: /cpp 4647331155846215|11|2024|630 20
Charge amount in Example 2 is $15</strong>""",parse_mode="html",reply_markup=key)
def aStripe(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='﻿AuthGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/str
  ↳ ON ✅ </strong>""",parse_mode="html",reply_markup=key)
def apaypal(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='﻿AuthGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/aup
  ↳ OFF ⚠️ </strong>""",parse_mode="html",reply_markup=key)
def aCyberSource(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='﻿AuthGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/cyp
  ↳ OFF ⚠️ </strong>""",parse_mode="html",reply_markup=key)
 
def aSquare(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='﻿AuthGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/so
  ↳ OFF ⚠️ </strong>""",parse_mode="html",reply_markup=key)
def aBraintree(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='﻿AuthGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/bri
  ↳ ON ✅ </strong>""",parse_mode="html",reply_markup=key)
def adScuore(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='﻿AuthGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/ad
  ↳ OFF ⚠️ </strong>""",parse_mode="html",reply_markup=key)
def aShopify(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='﻿AuthGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/sho
  ↳ ON ✅ </strong>""",parse_mode="html",reply_markup=key)
 #-------======Chargefounc========-----
def Stripe(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='ChargeGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/ctr
  ↳ ON ✅ 
  ↳ $1 Charge</strong>""",parse_mode="html",reply_markup=key)
def paypal(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='ChargeGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/cap
  ↳ OFF ⚠️ 
  ↳ $10 Charge</strong>""",parse_mode="html",reply_markup=key)
def CyberSource(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='ChargeGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/cp
  ↳ OFF ⚠️ 
  ↳ $20 Charge</strong>""",parse_mode="html",reply_markup=key)
 
def Square(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='ChargeGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/cso
  ↳ OFF ⚠️ 
  ↳ $25 Charge</strong>""",parse_mode="html",reply_markup=key)
def Braintree(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='ChargeGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/cri
  ↳ ON ✅ 
  ↳ $12 Charge</strong>""",parse_mode="html",reply_markup=key)
def adyan(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='ChargeGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/cdy
  ↳ OFF ⚠️ 
  ↳ $5 Charge</strong>""",parse_mode="html",reply_markup=key)
def Shopify(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='ChargeGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/cho
  ↳ ON ✅ 
  ↳ $15 Charge</strong>""",parse_mode="html",reply_markup=key)
def lyra(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='ChargeGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/cly
  ↳ ON ✅ 
  ↳ $20 Charge</strong>""",parse_mode="html",reply_markup=key)
def payseb(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='↩️', callback_data='ChargeGates')
	key.row_width = 1
	key.add(back)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""<strong>﻿/csp
  ↳ ON ✅ 
  ↳ $50 Charge
  </strong>""",parse_mode="html",reply_markup=key)
bot.polling(True)