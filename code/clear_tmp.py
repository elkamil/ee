import os
from variables import folder_tmp, files

__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"


def clear_tmp_files(filename):
    for f in files:
        os.remove(folder_tmp+f)
