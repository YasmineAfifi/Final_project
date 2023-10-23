// assign the name of the user to navbar menu
const welcomeUser = document.getElementById("welcomeUser");
const logOutBtn = document.getElementById("logOutBtn");
welcomeUser.innerText = "welcome " + localStorage.getItem("userName");


// logout function to clear data from local storage
function logOut(){
    localStorage.clear();
    window.location.href = "http://127.0.0.1:5000/login"
}

// when click to the button call logout funtion
logOutBtn.addEventListener("click",logOut)