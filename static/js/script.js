
// set the value of local storage in the add Cars input form
const userIdInput = document.getElementById("userId");
const userNameInput =document.getElementById("userName");
if(localStorage.getItem("userId")!=null && localStorage.getItem("userName")!=null ){
    const userId =   localStorage.getItem("userId");
    const userName = localStorage.getItem("userName");
    // set hidden value with local storage value
    if( userNameInput!=null && userIdInput!=null){
        userNameInput.value = userName;
        userIdInput.value = userId;
    }
    }
   




// function Func() { 
//     fetch("./static/json/cars.json") 
//         .then((res) => { 
//         return res.json(); 
//     }).then((data) => {
//             for (let index = 0; index < data.cars.length; index++) {
//                 let element = data.cars[index];
//                 console.log(element);
//             }
//         })

//     // .then(({cars} = data) => {
//     //     console.log(cars)
//     //     for (let index = 0; index < cars.length; index++) {
//     //         let element = cars[index];
//     //         console.log(element);

//     //     }
//     // })
// }

// Func()


// validation for register form when submit it 
// const registerForm = document.getElementById("regiserForm");
// registerForm.addEventListener("submit",function(event){
// event.preventDefault();
// const name =document.getElementById("name").value;
// const email =document.getElementById("email").value;
// const password =document.getElementById("password").value;
// const nameError =document.getElementById("nameError");
// const emailError =document.getElementById("emailError");
// const passwordError =document.getElementById("passwordError");
// // validation for user name
// if(name.trim() == ""){
//     nameError.innerText ="Name Is Required";
// }else if(!(/^[a-zA-Z]+(\s[a-zA-Z]+)?$/).test(name)){
//     nameError.innerText ="Name accepts alphabets only";

// }else if(name.length<3){
//     nameError.innerText ="Name must be more than 3 char";
// }else if(name.length>20){
//     nameError.innerText ="Name must be less than 20 char";
// }else{
//     nameError.innerText ="";
// }


// // validation for email

// if(email.trim() == ""){
//     emailError.innerText ="Email Is Required";

// }else if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/).test(email)){
//     emailError.innerText ="Invalid E-mail";

// }else{
//     emailError.innerText ="";
// }

// // validation for password

// if(password.trim() == "")
// {
//     passwordError.innerText = "Password Is Required";
// }else if(password.length<6 || password.length>15){
//     passwordError.innerText = "Password must be between 6 to 15 char";

// }else{
//     passwordError.innerText = "";
// }
// // if there is no errors submit the form

// if(nameError.innerText ==""&&emailError.innerText =="" &&passwordError.innerText == ""){

//     registerForm.submit();
// }


// })





// validation for login form when submit it 


// const loginForm = document.getElementById("loginForm");
// loginForm.addEventListener("submit",function(event){
//     event.preventDefault();
//     const email =document.getElementById("email").value;
//     const password =document.getElementById("password").value;
//     const emailError =document.getElementById("emailError");
//     const passwordError =document.getElementById("passwordError");

// // validation for email

// if(email.trim() == ""){
//     emailError.innerText ="Email Is Required";

// }else if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/).test(email)){
//     emailError.innerText ="Invalid E-mail";

// }else{
//     emailError.innerText ="";
// }

// // validation for password

// if(password.trim() == "")
// {
//     passwordError.innerText = "Password Is Required";
// }else if(password.length<6 || password.length>15){
//     passwordError.innerText = "Password must be between 6 to 15 char";

// }else{
//     passwordError.innerText = "";
// }
// // if there is no errors submit the form

// if(emailError.innerText =="" && passwordError.innerText == ""){

//     loginForm.submit();
// }


// })





// validation for add car form when submit it 

const addCarForm = document.getElementById("addCarForm");
addCarForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const brand = document.getElementById("brand").value;
    const color = document.getElementById("color").value;
    const price = document.getElementById("price").value;
    const image = document.getElementById("image").value;
    const brandError = document.getElementById("brandError");
    const colorError = document.getElementById("colorError");
    const priceError =document.getElementById("priceError");
    const imageError =document.getElementById("imageError");

    if(brand.trim() == ""){
        brandError.innerText = "Brand Is Required";

    }else if(brand.length<3){
        brandError.innerText = "Brand must be more than 3 char ";
    }else{
        brandError.innerText ="";
    }


    if(color.trim() == ""){
        colorError.innerText = "Color Is Required";

    }else if(color.length<3){
        colorError.innerText = "color must be more than 3 char ";
    }else if(!(/^[a-zA-Z]+$/).test(color)){
        colorError.innerText ="Color accepts alphabets only";
    }else{
        colorError.innerText ="";
    }


    if(price.trim() == ""){
        priceError.innerText = "Price Is Required";

    }else if(!(/^[0-9]+$/).test(price)){
        priceError.innerText ="Price accepts Numbers only";
    }else{
        priceError.innerText ="";
    }

    if(image.trim() == ""){
        imageError.innerText = "Image Is Required";
    }else{
        imageError.innerText ="";
    }





if( brandError.innerText ==""&& colorError.innerText ==""&&priceError.innerText ==""&&imageError.innerText ==""){
    addCarForm.submit();
}



})


