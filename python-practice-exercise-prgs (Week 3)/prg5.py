import json

student_data = {'name': 'Alice',
        'score': 95, 
        'passed': True
}

json_string = json.dumps(student_data) # json_string = json.dumps(obj)
print(json_string)
