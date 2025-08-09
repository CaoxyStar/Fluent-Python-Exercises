import json

data = {
    'name': 'Curry',
    'number': 30,
    'team': 'Golden State',
}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['name'], data['number'], data['team'])