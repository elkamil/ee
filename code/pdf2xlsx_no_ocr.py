# -*- coding: utf-8 -*-
import time
from split_pdf_file import split_pdf
from variables import folder_tmp, split_pdf_1, split_pdf_2, split_pdf_3, pdf_folder
from ocr2pdf import OCRPDF
from merge_csv import MergeSplittedCSV
from csv_remove_blank_lines import RemoveBlankLines
from csv2xlsx import CSV2XLSX
from clear_tmp import clear_tmp_files
from ocr2csv import OCR2CSV
from sendEmail import sendemail


def start(filename, wybor):
    print(time.strftime("%H:%M:%S"))
    #split_pdf(pdf_folder+filename)
    # processes = []
    # filename_split = [split_pdf_1, split_pdf_2, split_pdf_3]
    # for i in range(3):
     #    splited_pdf = filename_split[i]
      #   processes.append(OCRPDF(folder_tmp+splited_pdf, i))
    # for p in processes:
     #    p.start()
    # for p in processes:
     #    p.join()
    # MergeSplittedCSV(folder_tmp+"result"+str(1)+".txt",
     #                 folder_tmp+"result"+str(2)+".txt",
      #                folder_tmp+"result"+str(3)+".txt")
    # RemoveBlankLines()
    OCR2CSV(wybor)
    # xlsx_f = CSV2XLSX(filename, wybor)
    xlsx_f = CSV2XLSX(filename,wybor)
    # sendemail(filename, xlsx_f)
    # clear_tmp_files(filename)
    print(time.strftime("%H:%M:%S"))
    return xlsx_f


start('LM_wolny_rynek_pierwotny.pdf', 1)