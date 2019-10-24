import yaml


def read_yml():
    with open('../data/data.yml', 'r', encoding='utf-8') as f:
        arr = []
        for data in yaml.load(f).values():
            arr.append(tuple(data.values()))
        return arr
