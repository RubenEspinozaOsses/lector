import camelot
import os
import shutil


files = [file for file in os.listdir(os.path.join('files/carpetas_por_procesar')) if file.endswith('.pdf')]



def save_tables_to_json(file, nombre_carpeta):
    source = 'files/carpetas_procesadas/'
    
    lattice = camelot.read_pdf('files/carpetas_por_procesar/'+file, pages='all', flavor='lattice', split_text=True)
    stream = camelot.read_pdf('files/carpetas_por_procesar/'+file, pages='1', flavor='stream', split_text=True)
    
    
    i = 0
    for table in stream:
        name = '1stpage-' + str(i) + '.json'
        i += 1
        table.to_json(source + nombre_carpeta + '/tablas/' + name)
    for table in lattice:
        name = 'lattice-' + str(i) + '.json'
        i += 1
        table.to_json(source + nombre_carpeta + '/tablas/' + name)

def move_original_f(file):
    shutil.move('files/carpetas_por_procesar/' + file, 'files/carpetas_procesadas/')

def move_to_failed(file):
    shutil.move('files/carpetas_por_procesar/' + file, 'files/carpetas_fallidas/')
    exit(1)

def create_folder_correct(nombre_carpeta):
    source = 'files/carpetas_procesadas/'
    os.mkdir(source + nombre_carpeta)
    os.mkdir(source + nombre_carpeta + '/tablas')

for file in files:
    nombre_carpeta = file.split('.')[0]
    if (nombre_carpeta not in os.listdir('files/carpetas_procesadas')):
        try:
            create_folder_correct(nombre_carpeta)
            save_tables_to_json(file, nombre_carpeta)
            move_original_f(file)
        except:
            move_to_failed(file)
    else:
        print(f'Carpeta con este nombre ya existente, intente cambiar el nombre o confirme que no se haya procesado con anterioridad. En caso de error por favor borre la carpeta con el nombre {nombre_carpeta}')
    

