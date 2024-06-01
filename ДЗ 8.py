import tabula

myfile = 'Премии.pdf'
tabula.convert_into(myfile,'Премии_итог.csv')
print('OK')