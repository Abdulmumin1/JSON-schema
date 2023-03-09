import unittest
import json
from main import generate_schema

class TestGenerateSchema(unittest.TestCase):
    
    def test_generate_schema(self):
        # Test with a simple JSON object
        json_data = {'name':'Abdulmumin', 'age':18}
        expected_schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'age': {'type': 'integer'}
            }
        }
        self.assertEqual(generate_schema(json_data), expected_schema)
        
        # Test with a nested JSON object
        json_data = {'name': 'Abdulmumin', 'address': {'street': 'Sabon Gari', 'city': 'Zaria'}}
        expected_schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'address': {
                    'type': 'object',
                    'properties': {
                        'street': {'type': 'string'},
                        'city': {'type': 'string'}
                    }
                }
            }
        }
        self.assertEqual(generate_schema(json_data), expected_schema)
        
        # Test with a JSON array
        json_data =  {'name':'Abdulmumin', 'age':18, 'skills':['python', 'js', '']}
        expected_schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'age': {'type': 'integer'},
                'skills':{
                'type': 'array',
                'items': [
                    {'type': 'string'},
                    {'type': 'string'},
                    {'type': 'string'}
                ]}
            }
        }
        self.assertEqual(generate_schema(json_data), expected_schema)
        
        # Test with a JSON null value
        json_data = None
        expected_schema = {'type': 'null'}
        self.assertEqual(generate_schema(json_data), expected_schema)
        
        # Test with a mixed JSON object
        json_data = {
            'name': 'John',
            'age': 30,
            'is_employed': True,
            'hobbies': ['reading', 'running', 'swimming'],
            'address': {
                'street': '123 Main St',
                'city': 'Anytown',
                'state': 'CA',
                'zip': '12345'
            }
        }
        expected_schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'age': {'type': 'integer'},
                'is_employed': {'type': 'boolean'},
                'hobbies': {
                    'type': 'array',
                    'items': [
                        {'type': 'string'},
                        {'type': 'string'},
                        {'type': 'string'}
                    ]
                },
                'address': {
                    'type': 'object',
                    'properties': {
                        'street': {'type': 'string'},
                        'city': {'type': 'string'},
                        'state': {'type': 'string'},
                        'zip': {'type': 'string'}
                    }
                }
            }
        }
        self.assertEqual(generate_schema(json_data), expected_schema)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGenerateSchema)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_tests()