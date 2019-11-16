__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from multiprocessing import Process
from count_pages import Ilosc_Stron_PDF
from threads_ocr import ThreadOCR


def OCRPDF(filename, i):
    ilosc_stron = Ilosc_Stron_PDF(filename)
    p = Process(target=ThreadOCR, args=[filename, ilosc_stron, i+1])
    return p
