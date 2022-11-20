import requests
from vipp import checkvip
def check_sk(key,usertele,id):
    vip = checkvip(id)
    data = 'card[number]=4512238502012742&card[exp_month]=12&card[exp_year]=2022&card[cvc]=354'
    first = requests.post('https://api.stripe.com/v1/tokens', data = data, auth = (key, ' '))
    status = first.status_code
    f_json = first.json()
    if 'error'in f_json:
        if 'type' in f_json['error']:
            type = f_json['error']['type']
        else:
            type = ''
    else:
        type = ''
    if status == 200 or type == 'card_error':
        try:
        	gkey = key[17]
        	jkey = key[90]
        	lkey = key.split(gkey)[0]
        	ikey = key.split(jkey)[1]
        	key = lkey+'xxxxxxxxxxxxxxxx'+ikey
        except:
        	key = key
        r_text = f"""<strong>LIVE KEY ✅

KEY: <code>{key}</code>
Response: Your card was declined
Checked By @{usertele} (<code>{id}</code>)
User Subscribe => [{vip}]</strong>"""
        
    else:
        if 'error' in first.json():
            if 'code' in first.json()['error']:
                r_res = first.json()['error']['code'].replace('_',' ').strip()
            else:
                r_res = 'INVALID API KEY'
        else:
            r_res = 'INVALID API KEY'
            
        r_text = f'''<strong>DEAD KEY ❌

KEY: <code>{key}</code>
Response: INVALID API KEY
Checked By @{usertele} (<code>{id}</code>)
User Subscribe => [{vip}]</strong>'''
    return r_text