import flask
import json
app = flask.Flask(__name__)

id =1
# function for returning the html pages
def get_html(page_name):
    html_page = open("Templetes/"+page_name+".html")
    page_content = html_page.read()
    html_page.close()
    return page_content

#  enter data to json file
def write_json(data,file_name="register.json"):
    with open(file_name,"w") as file:
        json.dump(data,file,indent=4)

# return the register form html
@app.route("/")
def register():
    gethtml = get_html("index")
    return gethtml

# add data from register form to json file
@app.route("/register",methods = ["POST"])
def call():
    name = flask.request.form.get("name")
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    print(name)
    with open("register.json") as json_file:
        global id
        data = json.load(json_file)
        temp =data["name"]
        y={"id":id,"Name":name,"email":email,"paswsword":password}
        temp.append(y)
        id= id + 1
        write_json(data)
    return "added"


# return the login form html
@app.route("/loginForm")
def login():
    gethtml = get_html("login")
    return gethtml


#  function of login retrieve data and compare it with json file

@app.route("/login",methods=["POST"])
def check_user_login():
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    print(email)
    print(password)
    with open("register.json") as json_file:
        data = json.load(json_file)
        all_Users = data["name"]
    for user in all_Users:
        if user["email"] == email and user["password"] == password:
            return "hello"
        else:
            return "fail"









if __name__ =='__main__':
    app.run(debug=True)