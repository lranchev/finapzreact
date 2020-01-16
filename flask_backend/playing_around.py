import pprint
import json

d = {"2019-08-23":{"1. open":"88.3300","2. high":"89.9571","3. low":"86.6800","4. close":"86.9900","5. volume":"1239091"},"2019-08-26":{"1. open":"88.4500","2. high":"88.4500","3. low":"87.0600","4. close":"87.8500","5. volume":"766175"},"2019-08-27":{"1. open":"88.6800","2. high":"89.2900","3. low":"87.2501","4. close":"88.2100","5. volume":"1126970"}}\

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results
a = []
for key, value in d.items():
    a.append(key)

print (a)
names = extract_values(d, "1. open")
print(names)


# file = 'C:/Users/lranchev/PycharmProjects/finapzreact/flask_backend/sample_data.txt'
# jsonn = json.dumps(file)


#with open(jsonn, 'r', encoding='utf-8') as f:

# for line in f:
#     eachline = line.split(',')
#     pprint.pprint(eachline)
#     # #        d[str(key)] = val
#     # jsondata = json.dumps(eachline)
#     # print(type(jsondata))
#     #
#     # a = json.loads(jsondata)
#     # print(type(a))
#     #
#     # print("end")