import json
# return last id for user
def get_last_id(json_file):
    with open("./static/json/"+json_file) as file:
        alldata =json.load(file)
        if json_file == "register.json":
            data = alldata["names"]
            if data==[]:
                last_id = 0
            else:
                last_id = data[-1]["id"]  #get the last id as data[len-1]["id"]
        elif json_file == "cars.json":
            data = alldata["cars"]
            if data==[]:
                last_id = 0
            else:
                last_id = data[-1]["id"]

    return last_id


#  enter data to json file
def write_json(data,file_name):
    with open(file_name,"w") as file:
        json.dump(data,file,indent=4)