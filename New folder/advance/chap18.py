import json
data = {
    'name' : "kadir",
    'age'  :23,
    'country' :"BD",
    'is_retired':True

}
'''
json_encode_str = json.dumps(data)
print(json_encode_str)

json_decode = json.loads(json_encode_str)
print(json_decode)'''
with open('F:/DIU/phython wp/program/json_data.json','w') as obj:
    json.dump(data,obj)

with open('F:/DIU/phython wp/program/json_data.json','r') as obj:
    json_data = json.load(obj)
    print(json_data)
