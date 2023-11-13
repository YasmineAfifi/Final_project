import flask
import json
from user_class import User
from car_class import Car
from functions import write_json
from flask import  redirect, render_template,request, url_for,session
app = flask.Flask(__name__)
app.secret_key = "security Key" #secret key for session

# return the register form html
@app.route("/")
def register():
    return render_template("index.html")

# add data from register form to json file
@app.route("/register",methods = ["POST"])
def add_user():
    name = flask.request.form.get("name")
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    User_object = User(name,email,password)
    is_found = User_object.save_user_data()
    
    return is_found



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
            
            return render_template("login.html",error="Wrong Email or password")

    else:
        return render_template("login.html",error="")

    
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

@app.route("/addCar")
def add_cars_form():

    return render_template("addCars.html") 

# add cars to json file
@app.route("/cars",methods=["POST"])
def Add_cars():
    image_uploaded = request.files["img"]
    brand = flask.request.form.get("brand")
    color = flask.request.form.get("color")
    price = flask.request.form.get("price")
    img_name= image_uploaded.filename
    car_object = Car(brand,color,price,img_name)
    car_object.save_car_data(image_uploaded)
    
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
    dateFrom = flask.request.form.get("dateFrom")
    dateTo = flask.request.form.get("dateTo")

    with open("./static/json/reservation.json") as file_json:
       reserve_file = json.load(file_json)
       reserve_data = reserve_file["reservedCars"]
       new_reservation = {"user_Id":user_Id,"username":username,"brand":brand,"color":color,"price":price,"dateFrom":dateFrom,"dateTo":dateTo}
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
                 Search_result+="<div class='col mt-3 mb-3'><div class='card h-100'><div class='card-body'>\
       <div class='imgContainerCard'><img class='card-img-top cardImg' src='../static/images/"+cars['image']+"'>\
       </div><a class='titleCardDelete' href='/carDetails/"+str(cars['id'])+"'>\
            <h5 class='card-title py-3'>"+cars['brand']+"</h5></a>\
            <div class='btnCardContainer pb-3'>\
            <a class='btn btn-primary detailsBtn' href='/carDetails/"+str(cars['id'])+"'>Details</a>\
            <a type='button' class='btn btn-secondary deleteBtn' data-bs-toggle='modal' data-bs-target='#exampleModal_"+str(cars['id'])+"'>Delete</a>\
            </div></div></div></div>\
            <div class='modal fade' id='exampleModal_"+str(cars['id'])+"' tabindex='-1' aria-labelledby='exampleModalLabel' aria-hidden='true'>\
              <div class='modal-dialog'>\
                <div class='modal-content'>\
                  <div class='modal-header'>\
                    <h1 class='modal-title fs-5' id='exampleModalLabel'>Confirm</h1>\
                    <button type='button' class='btn-close' data-bs-dismiss='modal' aria-label='Close'></button>\
                  </div>\
                  <div class='modal-body'>\
                   Do you want to delete "+cars['brand']+"'?\
                  </div>\
                  <div class='modal-footer'>\
                    <button type='button' class='btn btn-secondary' data-bs-dismiss='modal'>Close</button>\
                    <form  action='/delete/"+str(cars['id'])+"' method='post'>\
                    <button class='btn btn-danger' type='submit'>Delete</button>\
                    </form></div></div></div></div>"
        
    if Search_result =="":
        return render_template("searchResult.html",Search_result="<div class='centerPage container'><div class = 'containerNoResult'><p class='NoResultText'>No Results Found</p></div></div>")
    else:
         return render_template("searchResult.html",Search_result=Search_result)
    
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




# log out and clear session 
@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/login")


# delete Car 
@app.route("/delete/<int:car_id>",methods = ["POST"])
def delete_car(car_id):
  file_name = "./static/json/cars.json"
  with open("./static/json/cars.json") as file:
      all_data = json.load(file)
      all_car_data = all_data["cars"]
      for car in all_car_data:
          if car["id"] == car_id:
              all_car_data.pop(car_id-1)
  write_json(all_data,file_name)
    
  return render_template("home.html")




if __name__ =='__main__':
    app.run(host="0.0.0.0",debug=True)