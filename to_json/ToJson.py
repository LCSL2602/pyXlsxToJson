import json

from get_file import File


def create_dict(row: tuple, headers: list[str]) -> dict:
    index: int = 0
    item: dict = {}
    while index < len(headers):
        item[headers[index]] = row[index].value
        index += 1

    return item


class toJson:
    def __init__(self, file: File.File):
        self.file = file

    def create_list(self) -> list[dict]:
        list_dic: list[dict] = []
        sheet = self.file.get_sheet()
        headers = self.file.get_header()
        index = 2
        while index <= sheet.max_row:
            item = create_dict(sheet[index], headers)
            list_dic.append(item)
            index += 1
        return list_dic

    def create_json(self):
        data = {
            "data": self.create_list()
        }
        with open('./assets/data.json', 'w') as file:
            file.write(json.dumps(data, indent=4))
