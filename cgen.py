import random
def cc_gen(cc, mes = 'x', ano = 'x', cvv = 'x',amount = 'x',): 
    if amount != 'x':
        amount = int(amount)
    else:
        amount = 15
    genrated = 0
    ccs = []
    while(genrated < amount):
        genrated += 1
        s="0123456789"
        l = list(s)
        random.shuffle(l)
        result = ''.join(l)
        result = cc + result
        if cc[0] == "3":
            ccgen = result[0:15]
        else:
            ccgen = result[0:16]
        if mes == 'x':
            mesgen = random.randint(1,12)
            if len(str(mesgen)) == 1:
                mesgen = "0" + str(mesgen)
        else:
            mesgen = mes
        if ano == 'x':
            anogen = random.randint(2021,2029)
        else:
            anogen = ano
        if cvv == 'x':
            if cc[0] == "3":
                cvvgen = random.randint(1000,9999) 
            else:
                cvvgen = random.randint(100,999)
        else:
            cvvgen = cvv   
        # if not x: continue
        lista = "<code>" + str(ccgen) +"|" + str(mesgen) + "|"+ str(anogen) + "|" + str(cvvgen) + "</code>"
        ccs.append(lista)
    return ccs