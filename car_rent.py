import flask
import json
import itertools
from flask import  render_template,request
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
        
# return all data for cars
    @staticmethod
    def Show_All_Cars():
 
        with open("cars.json") as json_file:
            cars = json.load(json_file)
            All_cars = cars["cars"]

        return All_cars

# function for returning the html pages
def get_html(page_name):
    html_page = open("templates/"+page_name+".html")
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
def add_user():
    name = flask.request.form.get("name")
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    with open("register.json") as json_file:
        global id
        file_name="register.json"
        data = json.load(json_file)
        temp =data["name"]
        y={"id":id,"name":name,"email":email,"paswsword":password}
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
            id = user["id"]
            name = user["name"]
            return render_template("home.html",id=id,name=name)
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
    image_uploaded = request.files["img"]

    brand = flask.request.form.get("brand")
    color = flask.request.form.get("color")
    price = flask.request.form.get("price")
    img_name= image_uploaded.filename
    upload_path = "static/images/"+img_name
    car_object = Car(brand,color,price)
    with open("cars.json") as json_file:
        data_file = json.load(json_file)
        All_cars_data = data_file["cars"]
        car_data = {"id":car_object.id,"brand":car_object.brand,"color":car_object.color,"price":car_object.price,"image":img_name}
        All_cars_data.append(car_data)
        if img_name !="":
            image_uploaded.save(upload_path)
            write_json(data_file,file_name)
        else:
            return "All elements are required"

    return "Added successfully"


# see all cars is available in json file
@app.route("/AllCars")
def All_Cars():
    cars = Car.Show_All_Cars()
    return cars

# show reserve form
@app.route("/reserveForm")
def show_reserve_form():
    get_form =get_html("reserveForm")
    return get_form

# function for reserve car
@app.route("/reserve",methods = ["POST"])
def reserve_car():
    file_name = "reservation.json"
    user_Id = flask.request.form.get("userId")
    username = flask.request.form.get("userName")
    brand = flask.request.form.get("brand")
    color = flask.request.form.get("color")
    price = flask.request.form.get("price")
    
    with open("reservation.json") as file_json:
       reserve_file = json.load(file_json)
       reserve_data = reserve_file["reservedCars"]
       new_reservation = {"user_Id":user_Id,"username":username,"brand":brand,"color":color,"price":price}
       reserve_data.append(new_reservation)
       write_json(reserve_file,file_name)
       return "reserved"









if __name__ =='__main__':
    app.run(debug=True)