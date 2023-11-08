from last_id import get_last_id,write_json,json
from flask import render_template,redirect
# class of User
class User:
# constructor
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

    # add user data to json file
    def save_user_data(self):
        with open("./static/json/register.json") as json_file:
            last_id = get_last_id("register.json")
            id = last_id + 1
            is_found = False
            file_name="./static/json/register.json"
            data = json.load(json_file)
            temp =data["names"]
            for user in temp:
                if user["email"] == self.email:
                    is_found =True
                    break
        if is_found == True:
            return render_template("index.html",error="Email is Already exist")
        else:
            user={"id":id,"name":self.name,"email":self.email,"password":self.password}
            temp.append(user)
            write_json(data,file_name)
            return redirect("/login")
