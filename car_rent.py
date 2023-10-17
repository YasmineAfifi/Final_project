import flask
import json
import itertools

from pprint import pprint
import inspect
app = flask.Flask(__name__)

# class Cars 
class Car:
    id_obj = itertools.count()

    def __init__(self,brand,color,price):
        self.id = next(Car.id_obj)
        self.brand = brand
        self.color = color
        self.price = price



# function for returning the html pages
def get_html(page_name):
    html_page = open("Templetes/"+page_name+".html")
    page_content = html_page.read()
    html_page.close()
    return page_content

#  enter data to json file
def write_json(data,file_name):
    with open(file_name,"w") as file:
        json.dump(data,file,indent=4)

# return the register form html
@app.route("/")
def register():
    gethtml = get_html("index")
    return gethtml

id =1
# add data from register form to json file
@app.route("/register",methods = ["POST"])
def call():
    name = flask.request.form.get("name")
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    with open("register.json") as json_file:
        global id
        file_name="register.json"
        data = json.load(json_file)
        temp =data["name"]
        y={"id":id,"Name":name,"email":email,"paswsword":password}
        temp.append(y)
        id= id + 1
        write_json(data,file_name)
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
    with open("register.json") as json_file:
        data = json.load(json_file)
        all_Users = data["name"]
    for user in all_Users:
        if user["email"] == email and user["password"] == password:
            return "hello"
        else:
            return "fail"

# function for returning the add cars form html

@app.route("/addCars")
def add_cars_form():
    add_form = get_html("addCars")
    return add_form

# add cars to json file
@app.route("/cars",methods=["POST"])
def Add_cars():
    file_name = "cars.json"
    brand = flask.request.form.get("brand")
    color = flask.request.form.get("color")
    price = flask.request.form.get("price")
    car_object = Car(brand,color,price)
    with open("cars.json") as json_file:
        data_file = json.load(json_file)
        All_cars_data = data_file["cars"]
        car_data = {"id":car_object.id,"brand":car_object.brand,"color":car_object.color,"price":car_object.price}
        All_cars_data.append(car_data)
        write_json(data_file,file_name)
    return "Added successfully"


# see all cars is available in json file
@app.route("/AllCars")
def Show_All_Cars():
 
    with open("cars.json") as json_file:
        cars = json.load(json_file)
        All_cars = cars["cars"]

    return All_cars


if __name__ =='__main__':
    app.run(debug=True)