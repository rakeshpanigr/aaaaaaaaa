import datetime
import decimal

import json

def dict_converter(obj):
        if not  hasattr(obj,"__dict__"):
            return obj
        result = {}
        for key, val in obj.__dict__.items():
            if key.startswith("_"):
                continue
            element = []
            if isinstance(val, list):
                for item in val:
                    element.append(dict_converter(item))
            else:
                element = dict_converter(val)
            result[key] = element
        return result


class Identity:
    def __init__(self):
        self.name="abc name"
        self.first="abc first"
        self.addr=Addr()

class Addr:
    def __init__(self):
        self.street="sesame street"
        self.zip="13000"

class Doc:
    def __init__(self):
        self.identity=Identity()
        self.data="all data"
    


doc=Doc()

print("-Dictionary- \n")
print(dict_converter(doc))
print("\n-JSON- \n")
print(json.dumps(dict_converter(doc), sort_keys=True, indent=4))

