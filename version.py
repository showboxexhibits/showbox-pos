import json
def get_version():
    with open('version.json', 'r') as f:
        data = json.load(f)
    return data['current_version']['number']
