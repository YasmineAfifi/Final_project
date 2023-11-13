
                                                            Final Project EPFL
                                                               Rent-Car App


## Table of contents
-[Project Description](#project-description)

-[The Features](#the-features)

-[Tools](#tools)

### Project Description

It is a simple application that allows the user to search for and reserve all available cars in the app.

### The Features

1-Register form for user to save his credentials in json file every user has unique email

2-login Form to enter the user to home page

3-Add cars 

4-view all available cars for rent

5-user can reserve any available car

6-Delete cars

### Tools

HTML

CSS

Javascript

Python

Flask 

Bootstrap 


### The Instructions to run the app with flask 

1-Install Python3 version 3.12.0 To check the version write in cmd python --version .
2-Install Flask by writing in the cmd pip3 install Flask.
3-Open the folder of the application(car_rent) .
4-In the terminal of VScode write flask --app car_rent.py run.
5-Open the browser and enter the URL http://127.0.0.1:5000.
6-The index page will open.


### The Instructions to run the app with Docker

1- In the powershell run this command to create image (docker build -t imagename .)
2- In the powershell run this command to create container 
(docker run --name containername -d -p 8000:5000 imagename)
3-open the docker desktop and run the container 
4-Open the browser and enter the URL http://localhost:8000