from to_json import ToJson
from get_file import File

file = File.File('./assets/Tellus_Load_Aggregator.xlsx')
req = ToJson.toJson(file)

if __name__ == '__main__':
    req.create_json()


