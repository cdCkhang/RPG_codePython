import json
import json as js

file_paths = {0: 'items_generator/res/bonus_stats_Physical.json',
              1: 'items_generator/res/bonus_stats_Magic.json',
              2: 'items_generator/res/bonus_stats_Defense.json',
              3: 'items_generator/res/bonus_stats_Hybrid.json'}


class JsonResourceHandler:
    @classmethod
    def import_data(cls, file_path):
        try:
            with open(file_path, 'r') as JsonReader:
                data = js.load(JsonReader)
            return data
        except FileNotFoundError | FileExistsError:
            print(f'File {file_path} not found.')
            return None
        except json.JSONDecodeError:
            print(f'Error decoding file {file_path}.')
            return None
