thonimport json

def save_to_file(data, filename="output.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)