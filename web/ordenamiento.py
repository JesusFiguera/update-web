def ordenar(lista):
    for anterior in range(len(lista)-1,0,-1):
        for i in range(anterior):
            if lista[i]['tiempo'] > lista[i+1]['tiempo']:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista

def edit_time(user):
    for i in range(len(user)):
        if len(user[i]['tiempo']) == 2:
            user[i]['tiempo'] = '0'+':'+'0'+user[i]['tiempo'][1]
        elif len(user[i]['tiempo']) == 3:
            user[i]['tiempo'] = user[i]['tiempo'][0]+':'+user[i]['tiempo'][1]+user[i]['tiempo'][2]
    return user