import camelot
import os
import shutil


files = [file for file in os.listdir(os.path.join('files/carpetas_por_procesar')) if file.endswith('.pdf')]



def save_tables_to_json(file, nombre_carpeta):
    source = 'files/carpetas_procesadas/'
    
    tables = camelot.read_pdf('files/carpetas_por_procesar/'+file, pages='all')
    
    i = 0
    for table in tables:
        name = 'table-' + str(i) + '.json'
        i += 1
        table.to_json(source + nombre_carpeta + '/tablas/' + name)

def move_original_f(file):
    shutil.move('files/carpetas_por_procesar/' + file, 'files/carpetas_procesadas/')

def create_folder_correct(nombre_carpeta):
    source = 'files/carpetas_procesadas/'
    os.mkdir(source + nombre_carpeta)
    os.mkdir(source + nombre_carpeta + '/tablas')

for file in files:
    nombre_carpeta = file.split('.')[0]
    if (nombre_carpeta not in os.listdir('files/carpetas_procesadas')):
        create_folder_correct(nombre_carpeta)
        save_tables_to_json(file, nombre_carpeta)
        move_original_f(file)
    else:
        print(f'Carpeta con este nombre ya existente, intente cambiar el nombre o confirme que no se haya procesado con anterioridad. En caso de error por favor borre la carpeta con el nombre {nombre_carpeta}')
    

#file = 'files/carpeta.pdf'
#
#
#tables = camelot.read_pdf(file, pages='all')
#
#i = 0
#for table in tables:
#    name = 'table-' + str(i) + '.json'
#    i += 1
#    print(table.to_json('files/' + name))