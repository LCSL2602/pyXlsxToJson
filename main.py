from to_json import ToJson
from get_file import File
import sys

if __name__ == '__main__':
    file = File.File(sys.argv[1])
    req = ToJson.toJson(file)
    req.create_json()


