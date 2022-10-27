import json
import sys

searched = []
found = []


def buscar_codigo(codigo):
    data_list = json.loads(open('files/final/final.json', 'r').read())
    
    found = [el for el in data_list if el['codigo'] == codigo]
    
    return found

def append(arr):
    for el in arr:
        found.append(el)



args = sys.argv
for i in range(1,len(args)):
    if args[i] not in searched:
        searched.append(args[i])
        append(buscar_codigo(args[i]))





print(found)
        




