import json
import argparse

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

def save_schema(inp,output=None):
    output_file_name="output.json"
    if out:
        output_file_name=output
    with open(inp,"r") as source:
        json_data =  json.loads(source.read())
    json_schema=generate_schema(json_data)
    with open(output_file_name,"w") as dest:
        dest.write(json.dumps(json_schema,index=2))

schema_parser = argparse.ArgumentParser(prog='main.py',description='Generate schema from existing json file')
schema_parser.add_argument('-f','--file', help="JSON file path",action="store")
schema_parser.add_argument('-d','--destination',help="Destination file path",action="store")

args = schema_parser.parse_args()
if args.file: 
    save_schema(inp=args.file)
elif args.file and args.destination:
    save_schema(args.file,args.destination)
else:
    schema_parser.print_help()
