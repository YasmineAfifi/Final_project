// user can't open this page he must login first  
if(localStorage.getItem("userName")==null && localStorage.getItem("userId")==null ){
    window.location.href = "http://127.0.0.1:5000/login"
}


// set the values of the user that stored in a local storage in the Reserve Car hidden inputs form

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





