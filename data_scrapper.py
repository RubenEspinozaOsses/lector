import json
import os
import shutil


folders = [file for file in os.listdir(os.path.join('files/carpetas_procesadas')) if not file.endswith('.pdf')]


def identify_folder_format():
    'Identify the format of the folders to correctly process the information'
    pass


def save_on_data_list(folder):
    files = [file for file in os.listdir(folder + '/tablas') if file.endswith('.json')]
    scrapped_data = []
    for file in files:
        as_json = json.load(open(folder + '/tablas/' + file))

        month = as_json[0]['0'].split('\n')[0] # obtiene los meses de las tablas, ['1'] obtiene numero de cuota(?)

        #8 es donde estan los header
        #9 es donde estan los valores
        headers = as_json[8]
        
        if len(headers) > 9:
            #tabla no vacia vacia

            valores = as_json[9]


            codigo = valores['5']
            glosa = valores['6']
            valor = valores['9']
            scrapped_data.append({'mes': month,'codigo': codigo, 'glosa': glosa, 'valor': valor})
    


    with open('files/final/final.json', 'r') as f:
        text = f.read()
        if text == '':
            data_list = []
        else:
            data_list = json.loads(text)


    for data in scrapped_data:
        data_list.append(data)

    with open('files/final/final.json', 'w') as w:
        w.write(json.dumps(data_list))


    #print(scrapped_data)

for folder in folders:
    
    folder_name = os.path.join('files/carpetas_procesadas/' + folder)
    save_on_data_list(folder_name)
    shutil.rmtree(os.path.join(folder_name))





