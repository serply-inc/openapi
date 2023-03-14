import yaml, json; 

with open('serply_openapi.yml', 'r') as file:
    
    yml = yaml.safe_load(file)
    
    out_file = open("serply_openapi.json", "w")
    
    json.dump(yml, out_file, indent = 2)
    
    out_file.close()