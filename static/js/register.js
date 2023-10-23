// validation for register form when submit it 
const registerForm = document.getElementById("regiserForm");
registerForm.addEventListener("submit",function(event){
event.preventDefault();
const name =document.getElementById("name").value;
const email =document.getElementById("email").value;
const password =document.getElementById("password").value;
const nameError =document.getElementById("nameError");
const emailError =document.getElementById("emailError");
const passwordError =document.getElementById("passwordError");
// validation for user name
if(name.trim() == ""){
    nameError.innerText ="Name Is Required";
}else if(!(/^[a-zA-Z]+(\s[a-zA-Z]+)?$/).test(name)){
    nameError.innerText ="Name accepts alphabets only";

}else if(name.length<3){
    nameError.innerText ="Name must be more than 3 char";
}else if(name.length>20){
    nameError.innerText ="Name must be less than 20 char";
}else{
    nameError.innerText ="";
}


// validation for email

if(email.trim() == ""){
    emailError.innerText ="Email Is Required";

}else if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/).test(email)){
    emailError.innerText ="Invalid E-mail";

}else{
    emailError.innerText ="";
}

// validation for password

if(password.trim() == "")
{
    passwordError.innerText = "Password Is Required";
}else if(password.length<6 || password.length>15){
    passwordError.innerText = "Password must be between 6 to 15 char";

}else{
    passwordError.innerText = "";
}
// if there is no errors submit the form

if(nameError.innerText ==""&&emailError.innerText =="" &&passwordError.innerText == ""){

    registerForm.submit();
}


})
