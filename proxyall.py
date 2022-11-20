from requests import *
def socks4():
	prox= get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	return prox
def socks5():
	prox= get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	return prox
def http():
	prox = get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=100000&country=all&ssl=all&anonymity=all").text
	return prox
def https():
	prox = get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=100000&country=all&ssl=all&anonymity=all").text
	return prox
