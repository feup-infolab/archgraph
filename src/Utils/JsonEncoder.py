from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def json_merge(json_a, json_b):
    json_a = json_a[:-1] + "," + json_b[1:]

    return json_a
