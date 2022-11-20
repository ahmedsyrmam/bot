import requests
def checkvip(id):
	url=f"https://Iid.moahmedsalah.repl.co/check/?id={id}"
	r = requests.get(url)
	return r.text
def addvip(id):
	url=f"https://Iid.moahmedsalah.repl.co/add/?id={id}"
	r = requests.get(url)
	return r.text