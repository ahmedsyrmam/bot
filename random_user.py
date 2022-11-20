import requests
from vipp import checkvip
def geninfo(id,usertele):
	vip = checkvip(id)
	u="https://randomuser.me/api/"
	r = requests.get(u).json()
	rs = r['results'][0]
	gender = rs['gender']
	title = rs['name']['title']
	first = rs['name']['first']
	last = rs['name']['last']
	lo = rs['location']
	streetnumber = lo['street']['number']
	streetname = lo['street']['name']
	city = lo['city']
	state = lo['state']
	country = lo['country']
	postcode = lo['postcode']
	offset = lo['timezone']['offset']
	description = lo['timezone']['description']
	email = rs['email']
	login = rs['login']
	uuid=login['uuid']
	username=login['username']
	password = login["password"]
	salt=login['salt']
	dob=rs['dob']
	date=dob['date']
	age=dob['age']
	phone=rs['phone']
	cell = rs['cell']
	idname=rs['id']['name']
	image = rs['picture']['large']
	return f"""
	<strong>
	Title => <code>{title}</code>
	Gender => <code>{gender}</code>
	Name => <code>{first} {last}</code>
	StreetNumber => <code>{streetnumber}</code>
	StreetName => <code>{streetname}</code>
	State => <code>{state}</code>
	Country => <code>{city}</code>
	PostCode => <code>{postcode}</code>
	Email => <code>{email}</code>
	UserName => <code>{username}</code>
	PassWord => <code>{password}</code>
	Description => <code>{description}</code>
	Offset => <code>{offset}</code>
	Uuid => <code>{uuid}</code>
	Salt => <code>{salt}</code>
	Date => <code>{date}</code>
	Age => <code>{age}</code>
	Phone => <code>{phone}</code>
	Cell => <code>{cell}</code>
	IdName => <code>{idname}</code>
	Image => <a href="{image}">Click Vew</a>
	Checked By @{usertele} (<code>{id}</code>)
	User Subscribe => [{vip}]
	</strong>
	"""
