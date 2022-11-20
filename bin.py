import requests
from vipp import checkvip
def bin(bin,id,usertele):
	try:
		gbin = bin
		x1=gbin[0]
		x2=gbin[1]
		x3=gbin[2]
		x4=gbin[3]
		x5=gbin[4]
		x6=gbin[5]
		bin=x1+x2+x3+x4+x5+x6
	except:pass
	try:
		gbin = bin.split('|')[0]
		x1=gbin[0]
		x2=gbin[1]
		x3=gbin[2]
		x4=gbin[3]
		x5=gbin[4]
		x6=gbin[5]
		bin=x1+x2+x3+x4+x5+x6
	except:
		pass
	url="https://lookup.binlist.net/"+bin
	r = requests.get(url).json()
	try:
		scheme = r["scheme"]
	except:
		scheme = 'None'
	try:
		type = r['type']
	except:
		type='None'
	try:
		country = r["country"]["name"]
		emoji = r["country"]['emoji']
	except:
		country='None'
		emoji='None'
	try:
		bank = r['bank']['name']
	except:
		bank = 'None'
	try:
		url = r['bank']['url']
	except:
		url = 'None'
	try:
		phone = r['bank']['phone']
	except:
		phone = 'None'
	idd = int(open('vip.txt','r').read())
	id= int(id)
	if id == idd:
		vip='Premium'
	else:
		vip='Free User'
	tele=f"""
<strong>
    BIN INFO
BIN: <code>{bin}</code>
Brand: {scheme}
Type: {type}
Bank Name: {bank}
Bank Url: {url}
Bank Phone: {phone}
Country: {country} {emoji}
━━━━━━━━━━━━━
Checked By @{usertele} (<code>{id}</code>)
User Subscribe => [{vip}]</strong>"""
	return tele
	
def bincc(bin,id,usertele):
	try:
		gbin = bin
		x1=gbin[0]
		x2=gbin[1]
		x3=gbin[2]
		x4=gbin[3]
		x5=gbin[4]
		x6=gbin[5]
		bin=x1+x2+x3+x4+x5+x6
	except:pass
	try:
		gbin = bin.split('|')[0]
		x1=gbin[0]
		x2=gbin[1]
		x3=gbin[2]
		x4=gbin[3]
		x5=gbin[4]
		x6=gbin[5]
		bin=x1+x2+x3+x4+x5+x6
	except:
		pass
	url="https://lookup.binlist.net/"+bin
	r = requests.get(url).json()
	try:
		scheme = r["scheme"]
	except:
		scheme = 'None'
	try:
		type = r['type']
	except:
		type='None'
	try:
		country = r["country"]["name"]
		emoji = r["country"]['emoji']
	except:
		country='None'
		emoji='None'
	try:
		bank = r['bank']['name']
	except:
		bank = 'None'
	try:
		url = r['bank']['url']
	except:
		url = 'None'
	try:
		phone = r['bank']['phone']
	except:
		phone = 'None'
	vip = checkvip(id)
	tele=f"""
BIN INFO:
			BIN => <code>{bin}</code>
			Brand => {scheme}
			Type => {type}
			Bank Name => {bank}
			Bank Url => {url}
			Bank Phone => {phone}
			Country => {country} {emoji}
━━━━━━━━━━━━━
<strong>Checked By @{usertele} (<code>{id}</code>)
User Subscribe => [{vip}]</strong>"""
	return tele