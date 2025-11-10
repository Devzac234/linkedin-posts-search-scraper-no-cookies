thonimport json
from extractors.utils import save_to_file

class Exporter:
    def export_to_json(self, data):
        save_to_file(data)
        print("Data exported to output.json")