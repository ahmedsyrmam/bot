from cgen import cc_gen
import re
from vipp import checkvip
def gg(m,id,usertele):
    vip = checkvip(id)
    cards = ''
    text = m
    if len(text) < 6:
        return "Invaid bin"
    input = re.findall(r"[0-9]+", text)
    if len(input) == 0:
        return ''
    if len(input) == 1:
        cc = input[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    elif len(input[0]) < 6 or len(input[0]) > 16:
        return ''
    if len(input) == 2:
        cc = input[0]
        mes = input[1]
        ano = 'x'
        cvv = 'x'
    if len(input) == 3:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = 'x'
    if len(input) == 4:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]
    
    else:
        ccs = cc_gen(cc,mes,ano,cvv)
        cards = '\n'.join(ccs)
        return f"""<strong><b>Card Generator</b>:
<b>Bin</b>: <code>{cc}</code>
<b>Cards</b>: 
{cards}
Checked By @{usertele} (<code>{id}</code>)
User Subscribe => [{vip}]</strong>"""
