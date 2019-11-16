from lokale_mieszkalne.variables import header_csv as lm_header
from lokale_uslugowe.variables import header_csv as lu_header
from grunty.variables import header_csv as grunty_header
from budynki.variables import header_csv as budynki_header
from mp.variables import header_csv as mp_header
from lokale_mieszkalne.merge import if_statements as lm_statements
from lokale_uslugowe.merge import if_statements as lu_statements
from grunty.merge import if_statements as grunty_statements
from budynki.merge import if_statements as budynki_statements
from mp.merge import if_statements as mp_statements
from variables import static_folder

__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"


def choose_method(wybor):
    if wybor == 1:
        header_csv = lm_header
        if_statements = lm_statements
        done_folder = static_folder + "lokale_mieszkalne/"
        backup_folder = static_folder + "backup/lokale_mieszkalne/"
        opis_column = "Z2:Z100000"
    elif wybor == 2:
        header_csv = grunty_header
        if_statements = grunty_statements
        done_folder = static_folder + "grunty/"
        backup_folder = static_folder + "backup/grunty/"
        opis_column = "S2:S100000"
    elif wybor == 3:
        done_folder = static_folder + "budynki/"
        if_statements = budynki_statements
        backup_folder = static_folder + "backup/budynki/"
        header_csv = budynki_header
        opis_column = "T2:T100000"
    elif wybor == 4:
        done_folder = static_folder + "mp/"
        if_statements = mp_statements
        backup_folder = static_folder + "backup/mp/"
        header_csv = mp_header
        opis_column = "R2:R100000"
    elif wybor == 5:
        done_folder = static_folder + "lokale_uslugowe/"
        if_statements = lu_statements
        backup_folder = static_folder + "backup/lokale_uslugowe/"
        header_csv = lu_header
        opis_column = "Z2:Z100000"
    return header_csv, if_statements, backup_folder, done_folder, opis_column
