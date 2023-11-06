import flask
import json
from flask import  redirect, render_template,request, url_for,session
app = flask.Flask(__name__)
app.secret_key = "security Key" #secret key for session

# class of User
class User:
# constructor
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

    # add user data to json file
    def UserData(self):
        with open("./static/json/register.json") as json_file:
            last_id = get_last_id("register.json")
            id = last_id + 1
            file_name="./static/json/register.json"
            data = json.load(json_file)
            temp =data["names"]
            user={"id":id,"name":self.name,"email":self.email,"password":self.password}
            temp.append(user)
            write_json(data,file_name)


# class of Car
class Car:
# constructor
    def __init__(self,brand,color,price,image):
        self.brand = brand
        self.color = color
        self.price = price
        self.image = image

# add car data to json file
    def carData(self,image_uploaded):
        with open("./static/json/cars.json") as json_file:
            data_file = json.load(json_file)
            All_cars_data = data_file["cars"]
            last_car_id = get_last_id("cars.json")
            id =last_car_id + 1
            file_name = "./static/json/cars.json"
            upload_path = "./static/images/"+self.image
            car_data = {"id":id,"brand":self.brand,"color":self.color,"price":self.price,"image":self.image}
            All_cars_data.append(car_data)
            if self.image !="":
                image_uploaded.save(upload_path)
                write_json(data_file,file_name)
                
# return all data for cars
    @staticmethod
    def Show_All_Cars():
 
        with open("./static/json/cars.json") as json_file:
            cars = json.load(json_file)
            All_cars = cars["cars"]
        return All_cars
    



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

# add data from register form to json file
@app.route("/register",methods = ["POST"])
def add_user():
    name = flask.request.form.get("name")
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    User_object = User(name,email,password)
    User_object.UserData()
    return redirect("/login")



#  function of login retrieve data and compare it with json file

@app.route("/login",methods=["GET","POST"])
def check_user_login():
    if request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        with open("./static/json/register.json") as json_file:
            data = json.load(json_file)
            all_Users = data["names"]
        for user in all_Users:
            if user["email"] == email and user["password"] == password:
                id = user["id"]
                name = user["name"]
                session["id"]=id
                session["name"]=name
                return redirect(url_for('home_page'))
        else:
            return redirect("/login")

    else:
        loginForm = get_html("login")
        return loginForm
    
# show the home page and pass the name and id of the user 
@app.route("/home")
def home_page():
    if(session.get("name")!= None and session.get("id") != None):
        name = session.get("name")
        id   = session.get("id")
        return render_template("home.html",id=id,name=name)
    else:
        return render_template("home.html")
   

    
# function for returning the add cars form html

@app.route("/addCars")
def add_cars_form():
    add_form = get_html("addCars")
    return add_form

# add cars to json file
@app.route("/cars",methods=["POST"])
def Add_cars():
    image_uploaded = request.files["img"]
    brand = flask.request.form.get("brand")
    color = flask.request.form.get("color")
    price = flask.request.form.get("price")
    img_name= image_uploaded.filename
    car_object = Car(brand,color,price,img_name)
    car_object.carData(image_uploaded)
    
    return redirect("/home")

# see all cars is available in json file
@app.route("/AllCars")
def All_Cars():
    cars = Car.Show_All_Cars()
    return cars


# function for reserve car
@app.route("/reserve",methods = ["POST"])
def reserve_car():
    file_name = "./static/json/reservation.json"
    user_Id = flask.request.form.get("userId")
    username = flask.request.form.get("userName")
    brand = flask.request.form.get("brand")
    color = flask.request.form.get("color")
    price = flask.request.form.get("price")
    
    with open("./static/json/reservation.json") as file_json:
       reserve_file = json.load(file_json)
       reserve_data = reserve_file["reservedCars"]
       new_reservation = {"user_Id":user_Id,"username":username,"brand":brand,"color":color,"price":price}
       reserve_data.append(new_reservation)
       write_json(reserve_file,file_name)
       return redirect("/reservation")

# show the car details html and pass car data in it
@app.route("/carDetails/<int:car_id>")
def getDetails(car_id):
    car_details = []
    with open("./static/json/cars.json") as file:
        allData = json.load(file)
        data_array = allData["cars"]
        for car in data_array:
            if car["id"] == car_id:
                car_details.append(car)
                return render_template("carDetails.html",car_details=car_details)
        else:
             return render_template("carDetails.html",no_id = "<div class='centerPage container'><div class = 'containerNoResult'><p class='NoResultText'>No Data For This Id</p></div></div>")
       



# search function for color and brand search
@app.route("/search")
def search():
    search_value = flask.request.args.get("search").lower()
    Search_result =""
    with open("./static/json/cars.json") as file:
        cars_data = json.load(file)
        cars_data_array = cars_data["cars"]
    
        for cars in cars_data_array:
            if cars["brand"].lower().find(search_value)!=-1 or cars["color"].lower().find(search_value)!=-1:
                 Search_result+="<div class='col mt-3 mb-3'><div class='card h-100'><div class='card-body'><div class='imgContainerCard'><img class='card-img-top cardImg' src='../static/images/"+cars['image']+"'></div><a class='titleCardDetails'href='/carDetails/"+str(cars['id'])+"'><h5 class='card-title py-3'>"+cars["brand"]+"</h5></a><div class='btnCardContainer pb-3'><a class='btn btn-primary detailsBtn'href='/carDetails/"+str(cars["id"])+"'>Details</a></div></div></div></div>"
        
    getSearch = get_html("searchResult")

    if Search_result =="":
         return getSearch.replace("$$search_Container$$","<div class='centerPage container'><div class = 'containerNoResult'><p class='NoResultText'>No Results Found</p></div></div>")
    else:
         return getSearch.replace("$$search_Container$$",Search_result)

# return the reservation html page and pass user reservation data
@app.route("/reservation")
def reservation_page():
    user_id = session.get("id")
    user_reservation = []
    with open("./static/json/reservation.json") as file_json:
        all_reservations = json.load(file_json)
        all_reservations_data = all_reservations["reservedCars"]
        for reservation in all_reservations_data:
            if reservation["user_Id"] == str(user_id):
                user_reservation.append(reservation)
        if user_reservation != []:
         return render_template("reservation.html",user_reservation = user_reservation)
        else:
         return render_template("reservation.html",no_data="<div class='centerPage container'><div class = 'containerNoResult'><p class='NoResultText'>No reservations Found</p></div></div>")


# return the reservation html page
@app.route("/addCar")
def add_car_page():
    return render_template("addCars.html")

# log out and clear session 
@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/login")



if __name__ =='__main__':
    app.run(debug=True)