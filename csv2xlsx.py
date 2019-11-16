__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from variables import folder_tmp, csv_file
from shutil import copyfile
from choose_method import choose_method
from csv_record_separator import NumeryLiniiDoPodzialu
import pandas as pd

# lokale mieszkalne


def CSV2XLSX(filename, wybor):
    numery_linii_do_podzialu = NumeryLiniiDoPodzialu()
    choose = choose_method(wybor)
    done_folder = choose[3]
    backup_folder = choose[2]

    xlsx_file = filename+".xlsx"
    engine = 'xlsxwriter'
    print("..Konwersja CSV na Excel...")
    writer = pd.ExcelWriter(done_folder+xlsx_file, engine=engine)
    read_file = pd.read_csv(folder_tmp+csv_file, sep=';', encoding='utf-8')
    read_file.to_excel(writer, sheet_name=filename[:25], index=False)
    workbook = writer.book
    worksheet = writer.sheets[filename[:25]]
    # format1 = workbook.add_format({'num_format': '#,##0.00'})
    # worksheet.set_column('M:M', 18, format1)
    format2 = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
    worksheet.conditional_format(choose[4], {'type': 'text',
                                 'criteria': 'containing', 'value': 'Udzi', 'format': format2})
    # worksheet.write_formula('AA2',   '=IF(OR(U6="do 1930",U6="1931-1940",U6="1941-1950",U6="1951-1960"),"Murowana (cegła - pustak)",IF(OR(U6="1961-1970",U6="1971-1980",U6="1981-1990"),"Prefabrykowana",IF(OR(U6="1991-2000",U6>2001),"Mieszana",IF(U6="","",""))))')
    if wybor == 1:
        for row in range(2, len(numery_linii_do_podzialu)+2):
            worksheet.write_formula('AA{0}'.format(row), '=IF(OR(U{0}="do 1930",U{0}="1931-1940",U{0}="1941-1950",U{0}="1951-1960"),"Murowana (cegła - pustak)",IF(OR(U{0}="1961-1970",U{0}="1971-1980",U{0}="1981-1990"),"Prefabrykowana",IF(OR(U{0}="1991-2000",U{0}>2001),"Mieszana",IF(U{0}="","",""))))'.format(row))
            worksheet.write_formula('AY{0}'.format(row), '=IF(OR(U{0}="do 1930",U{0}="1931-1940",U{0}="1941-1950",U{0}="1951-1960"),"Przeciętny",IF(OR(U{0}="1961-1970",U{0}="1971-1980",U{0}="1981-1990"),"Dobry",IF(OR(U{0}="1991-2000",U{0}>2001),"Bardzo dobry",IF(U{0}="","",""))))'.format(row))
    elif wybor == 3:
        for row in range(2, len(numery_linii_do_podzialu)+2):
            worksheet.write_formula('U{0}'.format(row), '=IF(OR(V{0}="do 1930",V{0}="1931-1940",V{0}="1941-1950",V{0}="1951-1960"),"Murowana (cegła - pustak)",IF(OR(V{0}="1961-1970",V{0}="1971-1980",V{0}="1981-1990"),"Prefabrykowana",IF(OR(V{0}="1991-2000",V{0}>2001),"Mieszana",IF(V{0}="","",""))))'.format(row))
            worksheet.write_formula('AL{0}'.format(row), '=IF(OR(V{0}="do 1930",V{0}="1931-1940",V{0}="1941-1950",V{0}="1951-1960"),"Przeciętny",IF(OR(V{0}="1961-1970",V{0}="1971-1980",V{0}="1981-1990"),"Dobry",IF(OR(V{0}="1991-2000",V{0}>2001),"Bardzo dobry",IF(V{0}="","",""))))'.format(row))
    elif wybor == 5:
        for row in range(2, len(numery_linii_do_podzialu)+2):
            worksheet.write_formula('AA{0}'.format(row), '=IF(OR(S{0}="do 1930",S{0}="1931-1940",S{0}="1941-1950",S{0}="1951-1960"),"Murowana (cegła - pustak)",IF(OR(S{0}="1961-1970",S{0}="1971-1980",S{0}="1981-1990"),"Prefabrykowana",IF(OR(S{0}="1991-2000",S{0}>2001),"Mieszana",IF(S{0}="","",""))))'.format(row))
            worksheet.write_formula('AU{0}'.format(row), '=IF(OR(S{0}="do 1930",S{0}="1931-1940",S{0}="1941-1950",S{0}="1951-1960"),"Przeciętny",IF(OR(S{0}="1961-1970",S{0}="1971-1980",S{0}="1981-1990"),"Dobry",IF(OR(S{0}="1991-2000",S{0}>2001),"Bardzo dobry",IF(S{0}="","",""))))'.format(row))

    writer.save()
    copyfile(done_folder+xlsx_file, backup_folder+xlsx_file)
    return(done_folder+xlsx_file)
