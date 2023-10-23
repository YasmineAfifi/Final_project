// user can't open this page he must login first  
if(localStorage.getItem("userName")==null && localStorage.getItem("userId")==null ){
    window.location.href = "http://127.0.0.1:5000/login";
}

// assign the name of the user to navbar menu
const welcomeUser = document.getElementById("welcomeUser");
const logOutBtn = document.getElementById("logOutBtn");
welcomeUser.innerText = "welcome " + localStorage.getItem("userName");


// logout function to clear data from local storage
function logOut(){
    localStorage.clear();
}

// when click to the button call logout funtion
logOutBtn.addEventListener("click",logOut);