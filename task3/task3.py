import json

with open('tests.json', 'r') as file:
    tests_content = json.load(file)

with open('values.json', 'r') as file:
    values_content = json.load(file)

values_dict = {value['id']: value['value'] for value in values_content['values']}


def fill_values(test_structure):
    if 'id' in test_structure and test_structure['id'] in values_dict:
        test_structure['value'] = values_dict[test_structure['id']]
    if 'values' in test_structure:
        for sub_test in test_structure['values']:
            fill_values(sub_test)


report = {"tests": []}
for test in tests_content['tests']:
    test_copy = json.loads(json.dumps(test))
    fill_values(test_copy)
    report['tests'].append(test_copy)

with open('report.json', 'w') as report_file:
    json.dump(report, report_file, indent=4)
