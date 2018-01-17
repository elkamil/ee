__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from csv_record_separator import NumeryLiniiDoPodzialu
from csv_rows_count import Ilosc_Wierszy
from choose_method import choose_method
from variables import folder_tmp, csv_file, result_no_blank_lines
from itertools import islice
from tqdm import tqdm
import csv

from csv2xlsx import CSV2XLSX


def OCR2CSV(wybor):
    print("...Tworzenie pliku CSV z OCR...")
    numery_linii_do_podzialu = NumeryLiniiDoPodzialu()
    pbar_ocr2csv = tqdm(total=len(numery_linii_do_podzialu))
    ilosc_el = Ilosc_Wierszy()
    choose = choose_method(wybor)
    header_csv = choose[0]
    if_statements = choose[1]

    i = 0
    finito = open(folder_tmp+csv_file, 'w', newline='')
    writer = csv.DictWriter(finito, fieldnames=header_csv, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writeheader()
    while i < len(numery_linii_do_podzialu):
        with open(folder_tmp+result_no_blank_lines, 'r') as dane3:
            if i+1 < len(numery_linii_do_podzialu):
                line = ''.join(islice(dane3, numery_linii_do_podzialu[i]-1, numery_linii_do_podzialu[i+1]-1))
                z = if_statements(line)
                writer = csv.writer(finito, delimiter=';', quoting=csv.QUOTE_ALL)
                writer.writerows(z)
            else:
                line = ''.join(islice(dane3, numery_linii_do_podzialu[i]-1, ilosc_el))
                z = if_statements(line)
                writer = csv.writer(finito, delimiter=';', quoting=csv.QUOTE_ALL)
                writer.writerows(z)
        i += 1
        pbar_ocr2csv.update(1)
    finito.close()
    pbar_ocr2csv.close()
#    CSV2XLSX('budy', wybor)


# OCR2CSV(4)
