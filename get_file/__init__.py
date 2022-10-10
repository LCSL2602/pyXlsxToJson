import openpyxl
from pathlib import Path


class get_file:
    def __init__(self, name_sheet: str):
        self.__name_sheet = name_sheet

    def get_sheet(self, sheet_name=None) -> openpyxl.Workbook:
        xls_file = Path(f'{self.__name_sheet}')
        wb_obj: openpyxl.Workbook = openpyxl.load_workbook(xls_file)
        if sheet_name is None:
            sheet: openpyxl.Workbook = wb_obj.active
        else:
            sheet: openpyxl.Workbook = wb_obj[sheet_name]
        return sheet
