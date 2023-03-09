# JSON schema generator

### usage

```bash
python3 main.py -f PATH/TO/JSON 

```

You can as well set destination file using `-d`
```bash 
python3 main.py -f PATH/TO/JSON -d DESTINATION/FILE

```

Using the API
```python
from main import generate_schema

JSON = {'name' :'Abdulmumin', 'age' :1000}
JSON_schema = generate_schema(JSON) 

print(JSON_schema) 
# output
#    {
#      'type': 'object',
#      'properties': {
#      'name': {'type': 'string'},
#      'age': {'type': 'integer'}
#        }
#     } 
```
