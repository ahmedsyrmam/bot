import requests
from json import *
from vipp import checkvip
def igg(user,id,usertele):
	vip=checkvip(id)
	he = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ar',
	'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
	'x-asbd-id': '198387',
	'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': '0',
	}
	urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
	try:
		re =requests.get(urlg,headers=he).json()
		bio = re["data"]["user"]["biography"]
		followers = re["data"]["user"]["edge_followed_by"]["count"]
		following = re["data"]["user"]["edge_follow"]["count"]
		name = re["data"]["user"]["full_name"]
		iid = re["data"]["user"]["id"]
		img = re["data"]["user"]["profile_pic_url"]
		posts = re["data"]["user"]["edge_owner_to_timeline_media"]["count"]
		return f"""
		<strong>NAME => {name}\nID => <code>{iid}</code>\nFOLLOWERS => {followers}\nFOLLOWING => {following}\nBIO => {bio}\nPOSTS => {posts}\nIMAGE => <a href="{img}">Click View</a>\nChecked By @{usertele} (<code>{id}</code>)\nUser Subscribe => [{vip}]</strong>"""
	except requests.exceptions.RequestException as e:
		return "Error User"

