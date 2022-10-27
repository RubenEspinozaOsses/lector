import os
import sys

args = sys.argv.pop(0)
args = ' '.join(sys.argv)


os.system('python3 creador_tablas.py')
os.system('python3 data_scrapper.py')
os.system('python3 lector_datos.py ' + args)