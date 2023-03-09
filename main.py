import json

def array_type(schema, json_property):
    try:
        if isinstance(json_property[0], str):
            schema['type'] = 'enum'
    except:
        return

def add_padding(schema, json_property):
    
    schema['tags'] = ''
    schema['description'] = ''
    schema['required'] = False
def generate_schema(json_property):
    schema = {}
    if isinstance(json_property, dict):
        schema['type'] = 'object'
        schema['properties'] = {}
        for key, value in json_property.items():
            schema['properties'][key] = generate_schema(value)
    elif isinstance(json_property, list):
        schema['type'] = 'array'
        array_type(schema, json_property)
        schema['items'] = []
        for item in json_property:
            schema['items'].append(generate_schema(item))
    elif isinstance(json_property, str):
        schema['type'] = 'string'
        add_padding(schema, json_property)
    elif isinstance(json_property, int):
        schema['type'] = 'integer'
        add_padding(schema, json_property)
    elif isinstance(json_property, float):
        schema['type'] = 'number'
        add_padding(schema, json_property)
    elif isinstance(json_property, bool):
        schema['type'] = 'boolean'
        add_padding(schema, json_property)
    elif json_property is None:
        schema['type'] = 'null'
    return schema

with open('./data/data_2.json') as testdata:
    testdata = json.loads(testdata.read())
json_schema = generate_schema(testdata['message'])
print(json.dumps(json_schema, indent=2))

