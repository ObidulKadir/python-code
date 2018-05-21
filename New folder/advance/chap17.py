
import json
data = {
    'name' : "kadir",
    'age'  :23,
    'country' :"BD",
    'is_retired':True

}
json_encoded_str = json.dumps(data)
print(json_encoded_str)

json_decode = json.loads(json_encoded_str)
print(json_decode)