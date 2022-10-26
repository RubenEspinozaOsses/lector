import camelot

file = 'files/carpeta.pdf'

tables = camelot.read_pdf(file, pages='all')

i = 0
for table in tables:
    name = 'table-' + str(i) + '.json'
    i += 1
    print(table.to_json('files/' + name))