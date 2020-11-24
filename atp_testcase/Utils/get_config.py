import yaml


def get_test_host(test_data_path):
    with open(test_data_path,encoding='utf-8') as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        host = dat['host']
    return host

def get_config_data(test_data_path,field):
    with open(test_data_path) as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        pid = dat[field]
    return pid

def get_secretkey(test_data_path,field):
    with open(test_data_path) as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        secretkey = dat[field]
    return secretkey