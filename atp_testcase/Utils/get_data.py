import json
import os


def get_data_path(case_path):
    file_name = os.path.dirname(case_path)
    test_data = file_name + os.sep + os.path.basename(case_path).replace('.py', '.json')
    return test_data

def get_config_path(current_path,config_path):
    file_name = os.path.dirname(current_path).split('Common', 1)
    config_data = file_name[0] + config_path
    return config_data

def get_log_path(current_path,path):
    file_name = os.path.dirname(current_path).split('Utils', 1)
    log_path = file_name[0] + path
    return log_path

def get_test_data(test_data_path):
    case = []
    headers = []
    querystring = []
    data = []
    expected = []
    with open(test_data_path, encoding='utf-8') as f:
        dat = json.loads(f.read())
        test = dat['test']
        for td in test:
            case.append(td['case'])
            headers.append(td.get('headers', {}))
            querystring.append(td.get('querystring', {}))
            data.append(td.get('data', {}))
            expected.append(td.get('expected', {}))
    list_parameters = list(zip(case, headers, querystring, data, expected))
    return case,list_parameters
