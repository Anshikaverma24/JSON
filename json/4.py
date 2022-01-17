import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
print((json.dumps(a)))
with open ("myfile.json","w") as f:
    json.dump(a,f,sort_keys=True, indent=5)
    print(f)