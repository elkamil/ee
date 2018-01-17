__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from variables import folder_tmp, Input_file
import os


def MergeSplittedCSV(filename1, filename2, filename3):
    filenames = [filename1, filename2, filename3]
    open(folder_tmp+Input_file, 'w').close()
    with open(folder_tmp+Input_file, 'w') as mergedfile:
        for fname in filenames:
                with open(fname) as infile:
                    mergedfile.write(infile.read())
                os.remove(fname)
