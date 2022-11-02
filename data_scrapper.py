import json
import os
import shutil
import PyPDF2


folders = [file for file in os.listdir(os.path.join('files/carpetas_procesadas')) if not file.endswith('.pdf')]


def identify_folder_format(folder):
    file_name = folder + '.pdf'

    pdf_file = open(file_name, 'rb')

    reader = PyPDF2.PdfFileReader(pdf_file)

    first_page = reader.getPage(0)

    text = first_page.extractText()

    if 'TAMAÑO EMPRESA' in text:
        return 0
    elif 'PERSONALIZADA' in text:
        return 1
    elif 'SOLICITAR CRÉDITOS' in text:
        return 2
    elif 'ACREDITAR RENTA' in text:
        return 3
    else:
        return 39

    
    

def save_on_data_list(folder):
    files = [file for file in os.listdir(folder + '/tablas') if file.endswith('.json')]
    scrapped_data = []
    doc_format = identify_folder_format(folder)
    print(doc_format)
    for file in files:
        
        as_json = json.load(open(folder + '/tablas/' + file))

        if doc_format == 3:
            year = as_json[1]['0'].split('\n')[0].split('Año Tributario')[1]
            
            print(year)
        #month = as_json[0]['0'].split('\n')[0] # obtiene los meses de las tablas, ['1'] obtiene numero de cuota(?)

        #8 es donde estan los header
        #9 es donde estan los valores
        headers = as_json[8]
        
        if len(headers) > 9:
            #tabla no vacia vacia

            valores = as_json[9]


            codigo = valores['5']
            glosa = valores['6']
            valor = valores['9']
            scrapped_data.append({'mes': 'month','codigo': codigo, 'glosa': glosa, 'valor': valor})
    


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
    #shutil.rmtree(os.path.join(folder_name))





