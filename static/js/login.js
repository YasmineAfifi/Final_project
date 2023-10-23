// validation for login form when submit it 

const loginForm = document.getElementById("loginForm");
loginForm.addEventListener("submit",function(event){
    event.preventDefault();
    const email =document.getElementById("email").value;
    const password =document.getElementById("password").value;
    const emailError =document.getElementById("emailError");
    const passwordError =document.getElementById("passwordError");

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

if(emailError.innerText =="" && passwordError.innerText == ""){

    loginForm.submit();
}


})


