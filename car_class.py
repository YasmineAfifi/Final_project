from last_id import get_last_id,write_json,json

# class of Car
class Car:
# constructor
    def __init__(self,brand,color,price,image):
        self.brand = brand
        self.color = color
        self.price = price
        self.image = image

# add car data to json file
    def save_car_data(self,image_uploaded):
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
    

